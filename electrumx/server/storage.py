# Copyright (c) 2016-2017, the ElectrumX authors
#
# All rights reserved.
#
# See the file "LICENCE" for information about the copyright
# and warranty status of this software.

'''Backend database abstraction.'''

import os
import socket
from functools import partial

import electrumx.lib.util as util
import electrumx.server.messages_pb2 as messages_pb2

def db_class(name):
    '''Returns a DB engine class.'''
    for db_class in util.subclasses(Storage):
        if db_class.__name__.lower() == name.lower():
            db_class.import_module()
            return db_class
    raise RuntimeError('unrecognised DB engine "{}"'.format(name))


class Storage(object):
    '''Abstract base class of the DB backend abstraction.'''

    def __init__(self, name, for_sync):
        self.is_new = self.check_is_new()
        self.open(name, True)        
        self.for_sync = for_sync or self.is_new

    @classmethod
    def import_module(cls):
        '''Import the DB engine module.'''
        raise NotImplementedError

    def check_is_new(self):
        raise NotImplementedError

    def open(self, name, create):
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


class RocksDB(Storage):

    def __init__(self, name, for_sync):
        self.storename = name        
        super().__init__(name, for_sync)                        

    @classmethod
    def import_module(cls):
        pass

    def check_is_new(self):
        return not os.path.exists("/home/udev/tcprocks/rocksdata/" + self.storename)

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("localhost", 3333))

    def open(self, name, create):        
        self.connect()

        requestMessage = messages_pb2.OpenStore()
        requestMessage.name = self.storename
        msg = b'O' + requestMessage.SerializeToString()

        self.socket.send(len(msg).to_bytes(4, byteorder='big'))
        self.socket.send(msg)

        dataSizeBuf = self.socket.recv(4)        
        dataSize = int.from_bytes(dataSizeBuf, byteorder='big')
        self.socket.recv(dataSize)


    def close(self):
        self.socket.close()

    def get(self, key):
        requestMessage = messages_pb2.ByteArrayMessage()
        requestMessage.storename= self.storename
        requestMessage.data = key
        msg = b'G' + requestMessage.SerializeToString()


        self.socket.send(len(msg).to_bytes(4, byteorder='big'))
        self.socket.send(msg)

        dataSizeBuf = self.socket.recv(4)
        dataSize = int.from_bytes(dataSizeBuf, byteorder='big')
        data = self.socket.recv(dataSize)


        resultMessage = messages_pb2.GetResultMessage()
        resultMessage.ParseFromString(data)

        if resultMessage.found == 1:
            return resultMessage.data
        else:
            return None

    def put(self, key, value):
        requestMessage = messages_pb2.KeyValuePair()
        requestMessage.storename= self.storename
        requestMessage.key = key
        requestMessage.val = value
        msg = b'S' + requestMessage.SerializeToString()

        self.socket.send(len(msg).to_bytes(4, byteorder='big'))
        self.socket.send(msg)

        dataSizeBuf = self.socket.recv(4)
        dataSize = int.from_bytes(dataSizeBuf, byteorder='big')
        self.socket.recv(dataSize)


    def write_batch(self):
        return RocksDBWriteBatch(self)

    def iterator(self, prefix=b'', reverse=False):
        iter = RocksDBIterator(self, prefix, reverse)
        return iter


class RocksDBIterator(object):
    '''An iterator for MongoDB.'''

    def __init__(self, db, prefix, reverse):
        self.db = db
        self.prefix = prefix
        self.reverse = reverse
        self.loadData()

    def __iter__(self):
        return self

    def loadData(self):        
        requestMessage = messages_pb2.ByteArrayMessage()
        requestMessage.storename = self.db.storename
        requestMessage.data = self.prefix
        msg = b'P' + requestMessage.SerializeToString()

        self.db.socket.send(len(msg).to_bytes(4, byteorder='big'))
        self.db.socket.send(msg)

        dataSizeBuf = self.db.socket.recv(4)
        dataSize = int.from_bytes(dataSizeBuf, byteorder='big')
        data = self.db.socket.recv(dataSize)

        resultMessage = messages_pb2.SearchByPrefixResponse()
        resultMessage.ParseFromString(data)
        self.result = resultMessage.vals



        if self.reverse:
            self.index = len(self.result) - 1
        else:
            self.index = 0
        pass

    def __next__(self):

        if self.reverse:
            if self.index <= 0:
                raise StopIteration
            else:
                self.index -= 1
                l = self.result[self.index + 1]
                return (l.key, l.val)
        else:
            if (self.index) >= len(self.result) or len(self.result) == 0:
                raise StopIteration
            else:
                self.index += 1
                l = self.result[self.index - 1]
                return (l.key, l.val)


class RocksDBWriteBatchWriter(object):

    def __init__(self, db):
        self.db = db
        self.result = []

    def put(self, key, value):
        pair = messages_pb2.BatchElement()
        pair.key = key
        pair.val = value
        pair.operation = messages_pb2.BatchElement.UPDATE
        self.result.append(pair)

    def delete(self, key):
        pair = messages_pb2.BatchElement()
        pair.key = key
        pair.operation = messages_pb2.BatchElement.DELETE
        self.result.append(pair)


class RocksDBWriteBatch(object):
    '''A write batch for RocksDB.'''

    def __init__(self, db):
        self.batch = RocksDBWriteBatchWriter(db)
        self.db = db        

    def __enter__(self):
        return self.batch

    def __exit__(self, exc_type, exc_val, exc_tb):
        # pass
        if not exc_val:            
            # here should be async write
            requestMessage = messages_pb2.BatchCommand()
            requestMessage.storename = self.db.storename
            requestMessage.vals.extend(self.batch.result)
            msg = b'B' + requestMessage.SerializeToString() 
            print('Sending batch len=' + str(len(msg)))
            self.db.socket.send(len(msg).to_bytes(4, byteorder='big'))
            self.db.socket.send(msg)

            dataSizeBuf = self.db.socket.recv(4)
            dataSize = int.from_bytes(dataSizeBuf, byteorder='big')
            self.db.socket.recv(dataSize)
            print('Batch is processed len=' + str(dataSize))

            self.batch.result.clear()