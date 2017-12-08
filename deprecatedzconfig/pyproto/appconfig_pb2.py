# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: appconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import devcommon_pb2 as devcommon__pb2
import network_pb2 as network__pb2
import storage_pb2 as storage__pb2
import vm_pb2 as vm__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='appconfig.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x61ppconfig.proto\x1a\x0f\x64\x65vcommon.proto\x1a\rnetwork.proto\x1a\rstorage.proto\x1a\x08vm.proto\"\x8f\x02\n\x11\x41ppInstanceConfig\x12\'\n\x0euuidandversion\x18\x01 \x01(\x0b\x32\x0f.UUIDandVersion\x12\x13\n\x0b\x64isplayname\x18\x02 \x01(\t\x12!\n\x0e\x66ixedresources\x18\x03 \x01(\x0b\x32\t.VmConfig\x12)\n\x11storageconfiglist\x18\x04 \x03(\x0b\x32\x0e.StorageConfig\x12\x10\n\x08\x61\x63tivate\x18\x05 \x01(\x08\x12-\n\x12overlaynetworklist\x18\x06 \x03(\x0b\x32\x11.EIDOverlayConfig\x12-\n\x13underlaynetworklist\x18\x07 \x03(\x0b\x32\x10.UnderlayNetworkBJ\n\x1f\x63om.zededa.cloud.uservice.protoZ\'github.com/zededa/api/deprecatedzconfigb\x06proto3')
  ,
  dependencies=[devcommon__pb2.DESCRIPTOR,network__pb2.DESCRIPTOR,storage__pb2.DESCRIPTOR,vm__pb2.DESCRIPTOR,])




_APPINSTANCECONFIG = _descriptor.Descriptor(
  name='AppInstanceConfig',
  full_name='AppInstanceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuidandversion', full_name='AppInstanceConfig.uuidandversion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayname', full_name='AppInstanceConfig.displayname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixedresources', full_name='AppInstanceConfig.fixedresources', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storageconfiglist', full_name='AppInstanceConfig.storageconfiglist', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activate', full_name='AppInstanceConfig.activate', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlaynetworklist', full_name='AppInstanceConfig.overlaynetworklist', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underlaynetworklist', full_name='AppInstanceConfig.underlaynetworklist', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=77,
  serialized_end=348,
)

_APPINSTANCECONFIG.fields_by_name['uuidandversion'].message_type = devcommon__pb2._UUIDANDVERSION
_APPINSTANCECONFIG.fields_by_name['fixedresources'].message_type = vm__pb2._VMCONFIG
_APPINSTANCECONFIG.fields_by_name['storageconfiglist'].message_type = storage__pb2._STORAGECONFIG
_APPINSTANCECONFIG.fields_by_name['overlaynetworklist'].message_type = network__pb2._EIDOVERLAYCONFIG
_APPINSTANCECONFIG.fields_by_name['underlaynetworklist'].message_type = network__pb2._UNDERLAYNETWORK
DESCRIPTOR.message_types_by_name['AppInstanceConfig'] = _APPINSTANCECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppInstanceConfig = _reflection.GeneratedProtocolMessageType('AppInstanceConfig', (_message.Message,), dict(
  DESCRIPTOR = _APPINSTANCECONFIG,
  __module__ = 'appconfig_pb2'
  # @@protoc_insertion_point(class_scope:AppInstanceConfig)
  ))
_sym_db.RegisterMessage(AppInstanceConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037com.zededa.cloud.uservice.protoZ\'github.com/zededa/api/deprecatedzconfig'))
# @@protoc_insertion_point(module_scope)
