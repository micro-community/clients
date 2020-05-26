# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: store/store.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='store/store.proto',
  package='go.micro.store',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11store/store.proto\x12\x0ego.micro.store\"4\n\x06Record\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\x03\"m\n\x0bReadOptions\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06prefix\x18\x03 \x01(\x08\x12\x0e\n\x06suffix\x18\x04 \x01(\x08\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\x0e\n\x06offset\x18\x06 \x01(\x04\"H\n\x0bReadRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x07options\x18\x02 \x01(\x0b\x32\x1b.go.micro.store.ReadOptions\"7\n\x0cReadResponse\x12\'\n\x07records\x18\x01 \x03(\x0b\x32\x16.go.micro.store.Record\"L\n\x0cWriteOptions\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\x03\x12\x0b\n\x03ttl\x18\x04 \x01(\x03\"e\n\x0cWriteRequest\x12&\n\x06record\x18\x01 \x01(\x0b\x32\x16.go.micro.store.Record\x12-\n\x07options\x18\x02 \x01(\x0b\x32\x1c.go.micro.store.WriteOptions\"\x0f\n\rWriteResponse\"0\n\rDeleteOptions\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\"L\n\rDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x07options\x18\x02 \x01(\x0b\x32\x1d.go.micro.store.DeleteOptions\"\x10\n\x0e\x44\x65leteResponse\"m\n\x0bListOptions\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x0e\n\x06suffix\x18\x04 \x01(\t\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\x0e\n\x06offset\x18\x06 \x01(\x04\";\n\x0bListRequest\x12,\n\x07options\x18\x01 \x01(\x0b\x32\x1b.go.micro.store.ListOptions\"\"\n\x0cListResponse\x12\x0c\n\x04keys\x18\x02 \x03(\tJ\x04\x08\x01\x10\x02\"\x12\n\x10\x44\x61tabasesRequest\"&\n\x11\x44\x61tabasesResponse\x12\x11\n\tdatabases\x18\x01 \x03(\t\"!\n\rTablesRequest\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\" \n\x0eTablesResponse\x12\x0e\n\x06tables\x18\x01 \x03(\t2\xc5\x03\n\x05Store\x12\x43\n\x04Read\x12\x1b.go.micro.store.ReadRequest\x1a\x1c.go.micro.store.ReadResponse\"\x00\x12\x46\n\x05Write\x12\x1c.go.micro.store.WriteRequest\x1a\x1d.go.micro.store.WriteResponse\"\x00\x12I\n\x06\x44\x65lete\x12\x1d.go.micro.store.DeleteRequest\x1a\x1e.go.micro.store.DeleteResponse\"\x00\x12\x45\n\x04List\x12\x1b.go.micro.store.ListRequest\x1a\x1c.go.micro.store.ListResponse\"\x00\x30\x01\x12R\n\tDatabases\x12 .go.micro.store.DatabasesRequest\x1a!.go.micro.store.DatabasesResponse\"\x00\x12I\n\x06Tables\x12\x1d.go.micro.store.TablesRequest\x1a\x1e.go.micro.store.TablesResponse\"\x00\x62\x06proto3'
)




_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='go.micro.store.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.store.Record.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='go.micro.store.Record.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='go.micro.store.Record.expiry', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=89,
)


_READOPTIONS = _descriptor.Descriptor(
  name='ReadOptions',
  full_name='go.micro.store.ReadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='go.micro.store.ReadOptions.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='go.micro.store.ReadOptions.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='go.micro.store.ReadOptions.prefix', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suffix', full_name='go.micro.store.ReadOptions.suffix', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='go.micro.store.ReadOptions.limit', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='go.micro.store.ReadOptions.offset', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=200,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='go.micro.store.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.store.ReadRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='go.micro.store.ReadRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=274,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='go.micro.store.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='go.micro.store.ReadResponse.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=331,
)


_WRITEOPTIONS = _descriptor.Descriptor(
  name='WriteOptions',
  full_name='go.micro.store.WriteOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='go.micro.store.WriteOptions.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='go.micro.store.WriteOptions.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='go.micro.store.WriteOptions.expiry', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='go.micro.store.WriteOptions.ttl', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=409,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='go.micro.store.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='go.micro.store.WriteRequest.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='go.micro.store.WriteRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=512,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='go.micro.store.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=529,
)


_DELETEOPTIONS = _descriptor.Descriptor(
  name='DeleteOptions',
  full_name='go.micro.store.DeleteOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='go.micro.store.DeleteOptions.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='go.micro.store.DeleteOptions.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=531,
  serialized_end=579,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='go.micro.store.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.store.DeleteRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='go.micro.store.DeleteRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=657,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='go.micro.store.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=675,
)


_LISTOPTIONS = _descriptor.Descriptor(
  name='ListOptions',
  full_name='go.micro.store.ListOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='go.micro.store.ListOptions.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='go.micro.store.ListOptions.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='go.micro.store.ListOptions.prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suffix', full_name='go.micro.store.ListOptions.suffix', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='go.micro.store.ListOptions.limit', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='go.micro.store.ListOptions.offset', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=677,
  serialized_end=786,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='go.micro.store.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='go.micro.store.ListRequest.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=788,
  serialized_end=847,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='go.micro.store.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='go.micro.store.ListResponse.keys', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=849,
  serialized_end=883,
)


_DATABASESREQUEST = _descriptor.Descriptor(
  name='DatabasesRequest',
  full_name='go.micro.store.DatabasesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=903,
)


_DATABASESRESPONSE = _descriptor.Descriptor(
  name='DatabasesResponse',
  full_name='go.micro.store.DatabasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='databases', full_name='go.micro.store.DatabasesResponse.databases', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=943,
)


_TABLESREQUEST = _descriptor.Descriptor(
  name='TablesRequest',
  full_name='go.micro.store.TablesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='go.micro.store.TablesRequest.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=945,
  serialized_end=978,
)


_TABLESRESPONSE = _descriptor.Descriptor(
  name='TablesResponse',
  full_name='go.micro.store.TablesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tables', full_name='go.micro.store.TablesResponse.tables', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=980,
  serialized_end=1012,
)

_READREQUEST.fields_by_name['options'].message_type = _READOPTIONS
_READRESPONSE.fields_by_name['records'].message_type = _RECORD
_WRITEREQUEST.fields_by_name['record'].message_type = _RECORD
_WRITEREQUEST.fields_by_name['options'].message_type = _WRITEOPTIONS
_DELETEREQUEST.fields_by_name['options'].message_type = _DELETEOPTIONS
_LISTREQUEST.fields_by_name['options'].message_type = _LISTOPTIONS
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['ReadOptions'] = _READOPTIONS
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['WriteOptions'] = _WRITEOPTIONS
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['DeleteOptions'] = _DELETEOPTIONS
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['ListOptions'] = _LISTOPTIONS
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['DatabasesRequest'] = _DATABASESREQUEST
DESCRIPTOR.message_types_by_name['DatabasesResponse'] = _DATABASESRESPONSE
DESCRIPTOR.message_types_by_name['TablesRequest'] = _TABLESREQUEST
DESCRIPTOR.message_types_by_name['TablesResponse'] = _TABLESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.Record)
  })
_sym_db.RegisterMessage(Record)

ReadOptions = _reflection.GeneratedProtocolMessageType('ReadOptions', (_message.Message,), {
  'DESCRIPTOR' : _READOPTIONS,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.ReadOptions)
  })
_sym_db.RegisterMessage(ReadOptions)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)

WriteOptions = _reflection.GeneratedProtocolMessageType('WriteOptions', (_message.Message,), {
  'DESCRIPTOR' : _WRITEOPTIONS,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.WriteOptions)
  })
_sym_db.RegisterMessage(WriteOptions)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)

DeleteOptions = _reflection.GeneratedProtocolMessageType('DeleteOptions', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOPTIONS,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.DeleteOptions)
  })
_sym_db.RegisterMessage(DeleteOptions)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

ListOptions = _reflection.GeneratedProtocolMessageType('ListOptions', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPTIONS,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.ListOptions)
  })
_sym_db.RegisterMessage(ListOptions)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

DatabasesRequest = _reflection.GeneratedProtocolMessageType('DatabasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATABASESREQUEST,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.DatabasesRequest)
  })
_sym_db.RegisterMessage(DatabasesRequest)

DatabasesResponse = _reflection.GeneratedProtocolMessageType('DatabasesResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATABASESRESPONSE,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.DatabasesResponse)
  })
_sym_db.RegisterMessage(DatabasesResponse)

TablesRequest = _reflection.GeneratedProtocolMessageType('TablesRequest', (_message.Message,), {
  'DESCRIPTOR' : _TABLESREQUEST,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.TablesRequest)
  })
_sym_db.RegisterMessage(TablesRequest)

TablesResponse = _reflection.GeneratedProtocolMessageType('TablesResponse', (_message.Message,), {
  'DESCRIPTOR' : _TABLESRESPONSE,
  '__module__' : 'store.store_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.store.TablesResponse)
  })
_sym_db.RegisterMessage(TablesResponse)



_STORE = _descriptor.ServiceDescriptor(
  name='Store',
  full_name='go.micro.store.Store',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1015,
  serialized_end=1468,
  methods=[
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='go.micro.store.Store.Read',
    index=0,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='go.micro.store.Store.Write',
    index=1,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_WRITERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='go.micro.store.Store.Delete',
    index=2,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='go.micro.store.Store.List',
    index=3,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Databases',
    full_name='go.micro.store.Store.Databases',
    index=4,
    containing_service=None,
    input_type=_DATABASESREQUEST,
    output_type=_DATABASESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Tables',
    full_name='go.micro.store.Store.Tables',
    index=5,
    containing_service=None,
    input_type=_TABLESREQUEST,
    output_type=_TABLESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORE)

DESCRIPTOR.services_by_name['Store'] = _STORE

# @@protoc_insertion_point(module_scope)
