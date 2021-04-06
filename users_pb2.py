# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='users.proto',
  package='users',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0busers.proto\x12\x05users\x1a\x1bgoogle/protobuf/empty.proto\"3\n\rLoginResponse\x12\"\n\x06status\x18\x01 \x01(\x0e\x32\x12.users.LoginStatus\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t*!\n\x0bLoginStatus\x12\x06\n\x02OK\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\x46\n\x05Users\x12=\n\x0c\x41uthenticate\x12\x13.users.LoginRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_LOGINSTATUS = _descriptor.EnumDescriptor(
  name='LoginStatus',
  full_name='users.LoginStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=186,
)
_sym_db.RegisterEnumDescriptor(_LOGINSTATUS)

LoginStatus = enum_type_wrapper.EnumTypeWrapper(_LOGINSTATUS)
OK = 0
FAILED = 1



_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='users.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='users.LoginResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=51,
  serialized_end=102,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='users.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='users.LoginRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='users.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=104,
  serialized_end=151,
)

_LOGINRESPONSE.fields_by_name['status'].enum_type = _LOGINSTATUS
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.enum_types_by_name['LoginStatus'] = _LOGINSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)



_USERS = _descriptor.ServiceDescriptor(
  name='Users',
  full_name='users.Users',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=188,
  serialized_end=258,
  methods=[
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='users.Users.Authenticate',
    index=0,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERS)

DESCRIPTOR.services_by_name['Users'] = _USERS

# @@protoc_insertion_point(module_scope)
