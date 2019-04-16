# Copyright (c) 2016-2017, the ElectrumX authors
#
# All rights reserved.
#
# See the file "LICENCE" for information about the copyright
# and warranty status of this software.

'''Backend database abstraction.'''

import os
from functools import partial
import re

import electrumx.lib.util as util


def db_class(name):
    '''Returns a DB engine class.'''
    for db_class in util.subclasses(Storage):
        if db_class.__name__.lower() == name.lower():
            db_class.import_module()
            return db_class
    raise RuntimeError('unrecognised DB engine "{}"'.format(name))


class Storage(object):
    '''Abstract base class of the DB backend abstraction.'''

    def __init__(self, name, for_sync, read_only):
        self.is_new = not os.path.exists(name)
        self.for_sync = for_sync or self.is_new
        self.open(name, create=self.is_new, read_only=read_only)

    @classmethod
    def import_module(cls):
        '''Import the DB engine module.'''
        raise NotImplementedError

    def open(self, name, create, read_only):
        '''Open an existing database or create a new one.'''
        raise NotImplementedError

    def close(self):
        '''Close an existing database.'''
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError

    def write_batch(self):
        '''Return a context manager that provides `put` and `delete`.

        Changes should only be committed when the context manager
        closes without an exception.
        '''
        raise NotImplementedError

    def iterator(self, prefix=b'', reverse=False):
        '''Return an iterator that yields (key, value) pairs from the
        database sorted by key.

        If `prefix` is set, only keys starting with `prefix` will be
        included.  If `reverse` is True the items are returned in
        reverse order.
        '''
        raise NotImplementedError


class MongoDB(Storage):
    @classmethod
    def import_module(cls):
        import pymongo
        cls.mongo = pymongo

    def __init__(self, name, for_sync, read_only):
        super().__init__(name, for_sync, read_only)
        self.read_only = read_only
        self.db = self.mongo.MongoClient().database

    def open(self, name, create, read_only):
        pass

    def close(self):
        self.db.close()

    def get(self, key):
        val = self.db.mytable.find_one({'_id':  str(key,"utf-8")})
        if val is None:
            return None
        return bytes(val['value'],'utf-8')

    def put(self, key, value):
        self.result = self.db.mytable.replace_one({'_id':  str(key,"utf-8")}, {'_id':  str(key,"utf-8"), 'value': str(value,"utf-8")},upsert=True)

    def write_batch(self):
        return MongoDBWriteBatch(self.db, self.read_only)

    def iterator(self, prefix=b'', reverse=False):
        return MongoDbIterator(self.db, prefix, reverse)

    def close(self):
        pass


class MongoDbIterator(object):
    '''An iterator for MongoDB.'''

    def __init__(self, db, prefix, reverse):

        self.prefix = prefix

        # db.mytable.find({"_id": {'$regex': "^" + "b\\'abc"}})
        self.result = list(db.mytable.find({"_id": {'$regex': "^" + str(prefix,"utf-8")}}))
        self.reverse = reverse
        if reverse:
            self.index = len(self.result)
        else:
            self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.reverse:
            if self.index <= 0:
                raise StopIteration
            else:
                self.index -= 1
                l = self.result[self.index+1]
                return bytes(l['_id'],'utf-8'), bytes(l['value'],'utf-8')
        else:
            if (self.index) >= len(self.result) or len(self.result) == 0:
                raise StopIteration
            else:
                self.index += 1
                l = self.result[self.index-1]
                return bytes(l['_id'],'utf-8'), bytes(l['value'],'utf-8')

# class LevelDB(Storage):
#     '''LevelDB database engine.'''
#
#     @classmethod
#     def import_module(cls):
#         import plyvel
#         cls.module = plyvel
#
#     def open(self, name, create, read_only):
#         mof = 512 if self.for_sync else 128
#         # Use snappy compression (the default)
#         self.db = self.module.DB(name, create_if_missing=create,
#                                  max_open_files=mof)
#         self.close = self.db.close
#         self.get = self.db.get
#         self.put = self.db.put
#         self.iterator = self.db.iterator
#         if not read_only:
#             self.write_batch = partial(self.db.write_batch, transaction=True,
#                                        sync=True)


# class RocksDB(Storage):
#     '''RocksDB database engine.'''
#
#     @classmethod
#     def import_module(cls):
#         import rocksdb
#         cls.module = rocksdb
#
#     def open(self, name, create, read_only):
#         mof = 512 if self.for_sync else 128
#         # Use snappy compression (the default)
#         options = self.module.Options(create_if_missing=create,
#                                       use_fsync=True,
#                                       target_file_size_base=33554432,
#                                       max_open_files=mof)
#         self.db = self.module.DB(name, options, read_only=read_only)
#         self.read_only = read_only
#         self.get = self.db.get
#         self.put = self.db.put
#
#     def close(self):
#         # PyRocksDB doesn't provide a close method; hopefully this is enough
#         self.db = self.get = self.put = None
#         import gc
#         gc.collect()
#
#     def write_batch(self):
#         return RocksDBWriteBatch(self.db, self.read_only)
#
#     def iterator(self, prefix=b'', reverse=False):
#         return RocksDBIterator(self.db, prefix, reverse)


class MongoDBWriteBatchWriter(object):

    def __init__(self, db):
        self.db = db

    def put(self, key, value):
        self.result = self.db.mytable.replace_one({'_id': key}, {'value': value})

    def delete(self,key):
        self.db.mytable.delete_one({'_id': key})


class MongoDBWriteBatch(object):
    '''A write batch for RocksDB.'''

    def __init__(self, db, read_only):
        self.batch = MongoDBWriteBatchWriter(db)
        self.db = db
        self.read_only = read_only

    def __enter__(self):
        return self.batch

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # if not exc_val:
        #     if not self.read_only:
        #         self.db.mytable.insert_many(self.batch)

# class RocksDBWriteBatch(object):
#     '''A write batch for RocksDB.'''
#
#     def __init__(self, db, read_only):
#         self.batch = RocksDB.module.WriteBatch()
#         self.db = db
#         self.read_only = read_only
#
#     def __enter__(self):
#         return self.batch
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if not exc_val:
#             if not self.read_only:
#                 self.db.write(self.batch)
#
#
#
# class RocksDBIterator(object):
#     '''An iterator for RocksDB.'''
#
#     def __init__(self, db, prefix, reverse):
#         self.prefix = prefix
#         if reverse:
#             self.iterator = reversed(db.iteritems())
#             nxt_prefix = util.increment_byte_string(prefix)
#             if nxt_prefix:
#                 self.iterator.seek(nxt_prefix)
#                 try:
#                     next(self.iterator)
#                 except StopIteration:
#                     self.iterator.seek(nxt_prefix)
#             else:
#                 self.iterator.seek_to_last()
#         else:
#             self.iterator = db.iteritems()
#             self.iterator.seek(prefix)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         k, v = next(self.iterator)
#         if not k.startswith(self.prefix):
#             raise StopIteration
#         return k, v
