# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/audit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nucliadb_protos import nodereader_pb2 as nucliadb__protos_dot_nodereader__pb2
try:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_noderesources__pb2
except AttributeError:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.noderesources_pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.utils_pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.utils_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nucliadb_protos/audit.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bnucliadb_protos/audit.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a nucliadb_protos/nodereader.proto\"\xf9\x02\n\x0c\x41uditRequest\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.AuditRequest.AuditType\x12\x0c\n\x04kbid\x18\x02 \x01(\t\x12\x0e\n\x06userid\x18\x04 \x01(\t\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ields\x18\x06 \x03(\t\x12)\n\x06search\x18\x07 \x01(\x0b\x32\x19.nodereader.SearchRequest\x12\x0e\n\x06timeit\x18\x08 \x01(\x02\x12\x0e\n\x06origin\x18\t \x01(\t\x12\x0b\n\x03rid\x18\n \x01(\t\x12\x0c\n\x04task\x18\x0b \x01(\t\x12\x11\n\tresources\x18\x0c \x01(\x05\"q\n\tAuditType\x12\x0b\n\x07VISITED\x10\x00\x12\x0c\n\x08MODIFIED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x07\n\x03NEW\x10\x03\x12\x0b\n\x07STARTED\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\n\n\x06SEARCH\x10\x06\x12\r\n\tPROCESSED\x10\x07\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,nucliadb__protos_dot_nodereader__pb2.DESCRIPTOR,])



_AUDITREQUEST_AUDITTYPE = _descriptor.EnumDescriptor(
  name='AuditType',
  full_name='AuditRequest.AuditType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VISITED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODIFIED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEARCH', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESSED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=363,
  serialized_end=476,
)
_sym_db.RegisterEnumDescriptor(_AUDITREQUEST_AUDITTYPE)


_AUDITREQUEST = _descriptor.Descriptor(
  name='AuditRequest',
  full_name='AuditRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='AuditRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kbid', full_name='AuditRequest.kbid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userid', full_name='AuditRequest.userid', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='AuditRequest.time', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='AuditRequest.fields', index=4,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='AuditRequest.search', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeit', full_name='AuditRequest.timeit', index=6,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin', full_name='AuditRequest.origin', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rid', full_name='AuditRequest.rid', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='AuditRequest.task', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resources', full_name='AuditRequest.resources', index=10,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUDITREQUEST_AUDITTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=476,
)

_AUDITREQUEST.fields_by_name['type'].enum_type = _AUDITREQUEST_AUDITTYPE
_AUDITREQUEST.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_AUDITREQUEST.fields_by_name['search'].message_type = nucliadb__protos_dot_nodereader__pb2._SEARCHREQUEST
_AUDITREQUEST_AUDITTYPE.containing_type = _AUDITREQUEST
DESCRIPTOR.message_types_by_name['AuditRequest'] = _AUDITREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuditRequest = _reflection.GeneratedProtocolMessageType('AuditRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUDITREQUEST,
  '__module__' : 'nucliadb_protos.audit_pb2'
  # @@protoc_insertion_point(class_scope:AuditRequest)
  })
_sym_db.RegisterMessage(AuditRequest)


# @@protoc_insertion_point(module_scope)
