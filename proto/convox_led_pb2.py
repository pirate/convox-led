# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: convox_led.proto

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
  name='convox_led.proto',
  package='org.convox.lights',
  serialized_pb=_b('\n\x10\x63onvox_led.proto\x12\x11org.convox.lights\"\xa8\x02\n\x11\x43onvoxLightConfig\x12:\n\x06\x63olors\x18\x01 \x03(\x0b\x32*.org.convox.lights.ConvoxLightConfig.Color\x12\x0e\n\x06period\x18\x02 \x01(\r\x12\x18\n\x10transition_steps\x18\x03 \x01(\r\x12\x1d\n\x12\x63ircle_compression\x18\x04 \x01(\x02:\x01\x31\x1a\x8d\x01\n\x05\x43olor\x12O\n\x0b\x63olor_space\x18\x01 \x01(\x0e\x32\x35.org.convox.lights.ConvoxLightConfig.Color.ColorSpace:\x03RGB\x12\x13\n\x0b\x63oordinates\x18\x02 \x03(\r\"\x1e\n\nColorSpace\x12\x07\n\x03RGB\x10\x01\x12\x07\n\x03HSV\x10\x02\x42\x1e\n\x11org.convox.lightsB\tConvoxLed')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CONVOXLIGHTCONFIG_COLOR_COLORSPACE = _descriptor.EnumDescriptor(
  name='ColorSpace',
  full_name='org.convox.lights.ConvoxLightConfig.Color.ColorSpace',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RGB', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HSV', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=306,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_CONVOXLIGHTCONFIG_COLOR_COLORSPACE)


_CONVOXLIGHTCONFIG_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='org.convox.lights.ConvoxLightConfig.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color_space', full_name='org.convox.lights.ConvoxLightConfig.Color.color_space', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coordinates', full_name='org.convox.lights.ConvoxLightConfig.Color.coordinates', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONVOXLIGHTCONFIG_COLOR_COLORSPACE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=336,
)

_CONVOXLIGHTCONFIG = _descriptor.Descriptor(
  name='ConvoxLightConfig',
  full_name='org.convox.lights.ConvoxLightConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='colors', full_name='org.convox.lights.ConvoxLightConfig.colors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='org.convox.lights.ConvoxLightConfig.period', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transition_steps', full_name='org.convox.lights.ConvoxLightConfig.transition_steps', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='circle_compression', full_name='org.convox.lights.ConvoxLightConfig.circle_compression', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONVOXLIGHTCONFIG_COLOR, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=336,
)

_CONVOXLIGHTCONFIG_COLOR.fields_by_name['color_space'].enum_type = _CONVOXLIGHTCONFIG_COLOR_COLORSPACE
_CONVOXLIGHTCONFIG_COLOR.containing_type = _CONVOXLIGHTCONFIG
_CONVOXLIGHTCONFIG_COLOR_COLORSPACE.containing_type = _CONVOXLIGHTCONFIG_COLOR
_CONVOXLIGHTCONFIG.fields_by_name['colors'].message_type = _CONVOXLIGHTCONFIG_COLOR
DESCRIPTOR.message_types_by_name['ConvoxLightConfig'] = _CONVOXLIGHTCONFIG

ConvoxLightConfig = _reflection.GeneratedProtocolMessageType('ConvoxLightConfig', (_message.Message,), dict(

  Color = _reflection.GeneratedProtocolMessageType('Color', (_message.Message,), dict(
    DESCRIPTOR = _CONVOXLIGHTCONFIG_COLOR,
    __module__ = 'convox_led_pb2'
    # @@protoc_insertion_point(class_scope:org.convox.lights.ConvoxLightConfig.Color)
    ))
  ,
  DESCRIPTOR = _CONVOXLIGHTCONFIG,
  __module__ = 'convox_led_pb2'
  # @@protoc_insertion_point(class_scope:org.convox.lights.ConvoxLightConfig)
  ))
_sym_db.RegisterMessage(ConvoxLightConfig)
_sym_db.RegisterMessage(ConvoxLightConfig.Color)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\021org.convox.lightsB\tConvoxLed'))
# @@protoc_insertion_point(module_scope)
