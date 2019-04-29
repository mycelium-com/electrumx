# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='rocksmessages',
  syntax='proto3',
  serialized_pb=_b('\n\x0emessages.proto\x12\rrocksmessages\"\x19\n\tOpenStore\x12\x0c\n\x04name\x18\x01 \x01(\t\";\n\x0cKeyValuePair\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x0b\n\x03val\x18\x02 \x01(\x0c\x12\x11\n\tstorename\x18\x03 \x01(\t\"e\n\x16SearchByPrefixResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x05\x12)\n\x04vals\x18\x02 \x03(\x0b\x32\x1b.rocksmessages.KeyValuePair\x12\x11\n\tstorename\x18\x03 \x01(\t\"\x87\x01\n\x0c\x42\x61tchElement\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x0b\n\x03val\x18\x02 \x01(\x0c\x12\x38\n\toperation\x18\x03 \x01(\x0e\x32%.rocksmessages.BatchElement.Operation\"#\n\tOperation\x12\n\n\x06UPDATE\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01\"\\\n\x0c\x42\x61tchCommand\x12)\n\x04vals\x18\x01 \x03(\x0b\x32\x1b.rocksmessages.BatchElement\x12\x0e\n\x06\x64\x62name\x18\x02 \x01(\t\x12\x11\n\tstorename\x18\x03 \x01(\t\"3\n\x10\x42yteArrayMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x11\n\tstorename\x18\x02 \x01(\t\"/\n\x10GetResultMessage\x12\r\n\x05\x66ound\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BATCHELEMENT_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='rocksmessages.BatchElement.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=325,
  serialized_end=360,
)
_sym_db.RegisterEnumDescriptor(_BATCHELEMENT_OPERATION)


_OPENSTORE = _descriptor.Descriptor(
  name='OpenStore',
  full_name='rocksmessages.OpenStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rocksmessages.OpenStore.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=58,
)


_KEYVALUEPAIR = _descriptor.Descriptor(
  name='KeyValuePair',
  full_name='rocksmessages.KeyValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='rocksmessages.KeyValuePair.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val', full_name='rocksmessages.KeyValuePair.val', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='storename', full_name='rocksmessages.KeyValuePair.storename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=119,
)


_SEARCHBYPREFIXRESPONSE = _descriptor.Descriptor(
  name='SearchByPrefixResponse',
  full_name='rocksmessages.SearchByPrefixResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='found', full_name='rocksmessages.SearchByPrefixResponse.found', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vals', full_name='rocksmessages.SearchByPrefixResponse.vals', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='storename', full_name='rocksmessages.SearchByPrefixResponse.storename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=222,
)


_BATCHELEMENT = _descriptor.Descriptor(
  name='BatchElement',
  full_name='rocksmessages.BatchElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='rocksmessages.BatchElement.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val', full_name='rocksmessages.BatchElement.val', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='rocksmessages.BatchElement.operation', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BATCHELEMENT_OPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=360,
)


_BATCHCOMMAND = _descriptor.Descriptor(
  name='BatchCommand',
  full_name='rocksmessages.BatchCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vals', full_name='rocksmessages.BatchCommand.vals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbname', full_name='rocksmessages.BatchCommand.dbname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='storename', full_name='rocksmessages.BatchCommand.storename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=454,
)


_BYTEARRAYMESSAGE = _descriptor.Descriptor(
  name='ByteArrayMessage',
  full_name='rocksmessages.ByteArrayMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='rocksmessages.ByteArrayMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='storename', full_name='rocksmessages.ByteArrayMessage.storename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=507,
)


_GETRESULTMESSAGE = _descriptor.Descriptor(
  name='GetResultMessage',
  full_name='rocksmessages.GetResultMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='found', full_name='rocksmessages.GetResultMessage.found', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='rocksmessages.GetResultMessage.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=556,
)

_SEARCHBYPREFIXRESPONSE.fields_by_name['vals'].message_type = _KEYVALUEPAIR
_BATCHELEMENT.fields_by_name['operation'].enum_type = _BATCHELEMENT_OPERATION
_BATCHELEMENT_OPERATION.containing_type = _BATCHELEMENT
_BATCHCOMMAND.fields_by_name['vals'].message_type = _BATCHELEMENT
DESCRIPTOR.message_types_by_name['OpenStore'] = _OPENSTORE
DESCRIPTOR.message_types_by_name['KeyValuePair'] = _KEYVALUEPAIR
DESCRIPTOR.message_types_by_name['SearchByPrefixResponse'] = _SEARCHBYPREFIXRESPONSE
DESCRIPTOR.message_types_by_name['BatchElement'] = _BATCHELEMENT
DESCRIPTOR.message_types_by_name['BatchCommand'] = _BATCHCOMMAND
DESCRIPTOR.message_types_by_name['ByteArrayMessage'] = _BYTEARRAYMESSAGE
DESCRIPTOR.message_types_by_name['GetResultMessage'] = _GETRESULTMESSAGE

OpenStore = _reflection.GeneratedProtocolMessageType('OpenStore', (_message.Message,), dict(
  DESCRIPTOR = _OPENSTORE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:rocksmessages.OpenStore)
  ))
_sym_db.RegisterMessage(OpenStore)

KeyValuePair = _reflection.GeneratedProtocolMessageType('KeyValuePair', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUEPAIR,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:rocksmessages.KeyValuePair)
  ))
_sym_db.RegisterMessage(KeyValuePair)

SearchByPrefixResponse = _reflection.GeneratedProtocolMessageType('SearchByPrefixResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBYPREFIXRESPONSE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:rocksmessages.SearchByPrefixResponse)
  ))
_sym_db.RegisterMessage(SearchByPrefixResponse)

BatchElement = _reflection.GeneratedProtocolMessageType('BatchElement', (_message.Message,), dict(
  DESCRIPTOR = _BATCHELEMENT,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:rocksmessages.BatchElement)
  ))
_sym_db.RegisterMessage(BatchElement)

BatchCommand = _reflection.GeneratedProtocolMessageType('BatchCommand', (_message.Message,), dict(
  DESCRIPTOR = _BATCHCOMMAND,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:rocksmessages.BatchCommand)
  ))
_sym_db.RegisterMessage(BatchCommand)

ByteArrayMessage = _reflection.GeneratedProtocolMessageType('ByteArrayMessage', (_message.Message,), dict(
  DESCRIPTOR = _BYTEARRAYMESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:rocksmessages.ByteArrayMessage)
  ))
_sym_db.RegisterMessage(ByteArrayMessage)

GetResultMessage = _reflection.GeneratedProtocolMessageType('GetResultMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETRESULTMESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:rocksmessages.GetResultMessage)
  ))
_sym_db.RegisterMessage(GetResultMessage)


# @@protoc_insertion_point(module_scope)
