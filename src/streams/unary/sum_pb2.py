# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sum.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsum.proto\"\x1b\n\x07Request\x12\x10\n\x08operands\x18\x01 \x03(\x03\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\x03\x32(\n\nSumService\x12\x1a\n\x03Sum\x12\x08.Request\x1a\t.Responseb\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'sum_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'sum_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

_SUMSERVICE = DESCRIPTOR.services_by_name['SumService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=13
  _REQUEST._serialized_end=40
  _RESPONSE._serialized_start=42
  _RESPONSE._serialized_end=68
  _SUMSERVICE._serialized_start=70
  _SUMSERVICE._serialized_end=110
# @@protoc_insertion_point(module_scope)
