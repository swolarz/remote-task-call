# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: taskcall.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='taskcall.proto',
  package='pl.put.swolarz.remotetaskcall',
  syntax='proto3',
  serialized_options=b'\n\'pl.put.swolarz.remotetaskcall.generatedP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0etaskcall.proto\x12\x1dpl.put.swolarz.remotetaskcall\"\x1b\n\x08TaskCall\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\"\x19\n\tTaskInput\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x90\x01\n\x0bTaskRequest\x12\x39\n\x05input\x18\x01 \x01(\x0b\x32(.pl.put.swolarz.remotetaskcall.TaskInputH\x00\x12\x37\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\'.pl.put.swolarz.remotetaskcall.TaskCallH\x00\x42\r\n\x0bRequestType\"\x88\x02\n\nTaskResult\x12=\n\theartbeat\x18\x01 \x01(\x0b\x32(.pl.put.swolarz.remotetaskcall.HeartbeatH\x00\x12\x37\n\x03std\x18\x02 \x01(\x0b\x32(.pl.put.swolarz.remotetaskcall.StdOutputH\x00\x12\x37\n\x03\x65rr\x18\x03 \x01(\x0b\x32(.pl.put.swolarz.remotetaskcall.ErrOutputH\x00\x12;\n\x06status\x18\x04 \x01(\x0b\x32).pl.put.swolarz.remotetaskcall.ExitStatusH\x00\x42\x0c\n\nOutputType\"\x0b\n\tHeartbeat\"\x19\n\tStdOutput\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x19\n\tErrOutput\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x1a\n\nExitStatus\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x32\x7f\n\x14TaskExecutionService\x12g\n\nLaunchTask\x12*.pl.put.swolarz.remotetaskcall.TaskRequest\x1a).pl.put.swolarz.remotetaskcall.TaskResult(\x01\x30\x01\x42+\n\'pl.put.swolarz.remotetaskcall.generatedP\x01\x62\x06proto3'
)




_TASKCALL = _descriptor.Descriptor(
  name='TaskCall',
  full_name='pl.put.swolarz.remotetaskcall.TaskCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='pl.put.swolarz.remotetaskcall.TaskCall.command', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=49,
  serialized_end=76,
)


_TASKINPUT = _descriptor.Descriptor(
  name='TaskInput',
  full_name='pl.put.swolarz.remotetaskcall.TaskInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='pl.put.swolarz.remotetaskcall.TaskInput.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=78,
  serialized_end=103,
)


_TASKREQUEST = _descriptor.Descriptor(
  name='TaskRequest',
  full_name='pl.put.swolarz.remotetaskcall.TaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='pl.put.swolarz.remotetaskcall.TaskRequest.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='call', full_name='pl.put.swolarz.remotetaskcall.TaskRequest.call', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='RequestType', full_name='pl.put.swolarz.remotetaskcall.TaskRequest.RequestType',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=106,
  serialized_end=250,
)


_TASKRESULT = _descriptor.Descriptor(
  name='TaskResult',
  full_name='pl.put.swolarz.remotetaskcall.TaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heartbeat', full_name='pl.put.swolarz.remotetaskcall.TaskResult.heartbeat', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='std', full_name='pl.put.swolarz.remotetaskcall.TaskResult.std', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='err', full_name='pl.put.swolarz.remotetaskcall.TaskResult.err', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='pl.put.swolarz.remotetaskcall.TaskResult.status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='OutputType', full_name='pl.put.swolarz.remotetaskcall.TaskResult.OutputType',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=253,
  serialized_end=517,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='Heartbeat',
  full_name='pl.put.swolarz.remotetaskcall.Heartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=519,
  serialized_end=530,
)


_STDOUTPUT = _descriptor.Descriptor(
  name='StdOutput',
  full_name='pl.put.swolarz.remotetaskcall.StdOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='pl.put.swolarz.remotetaskcall.StdOutput.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=532,
  serialized_end=557,
)


_ERROUTPUT = _descriptor.Descriptor(
  name='ErrOutput',
  full_name='pl.put.swolarz.remotetaskcall.ErrOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='pl.put.swolarz.remotetaskcall.ErrOutput.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=559,
  serialized_end=584,
)


_EXITSTATUS = _descriptor.Descriptor(
  name='ExitStatus',
  full_name='pl.put.swolarz.remotetaskcall.ExitStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pl.put.swolarz.remotetaskcall.ExitStatus.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=586,
  serialized_end=612,
)

_TASKREQUEST.fields_by_name['input'].message_type = _TASKINPUT
_TASKREQUEST.fields_by_name['call'].message_type = _TASKCALL
_TASKREQUEST.oneofs_by_name['RequestType'].fields.append(
  _TASKREQUEST.fields_by_name['input'])
_TASKREQUEST.fields_by_name['input'].containing_oneof = _TASKREQUEST.oneofs_by_name['RequestType']
_TASKREQUEST.oneofs_by_name['RequestType'].fields.append(
  _TASKREQUEST.fields_by_name['call'])
_TASKREQUEST.fields_by_name['call'].containing_oneof = _TASKREQUEST.oneofs_by_name['RequestType']
_TASKRESULT.fields_by_name['heartbeat'].message_type = _HEARTBEAT
_TASKRESULT.fields_by_name['std'].message_type = _STDOUTPUT
_TASKRESULT.fields_by_name['err'].message_type = _ERROUTPUT
_TASKRESULT.fields_by_name['status'].message_type = _EXITSTATUS
_TASKRESULT.oneofs_by_name['OutputType'].fields.append(
  _TASKRESULT.fields_by_name['heartbeat'])
_TASKRESULT.fields_by_name['heartbeat'].containing_oneof = _TASKRESULT.oneofs_by_name['OutputType']
_TASKRESULT.oneofs_by_name['OutputType'].fields.append(
  _TASKRESULT.fields_by_name['std'])
_TASKRESULT.fields_by_name['std'].containing_oneof = _TASKRESULT.oneofs_by_name['OutputType']
_TASKRESULT.oneofs_by_name['OutputType'].fields.append(
  _TASKRESULT.fields_by_name['err'])
_TASKRESULT.fields_by_name['err'].containing_oneof = _TASKRESULT.oneofs_by_name['OutputType']
_TASKRESULT.oneofs_by_name['OutputType'].fields.append(
  _TASKRESULT.fields_by_name['status'])
_TASKRESULT.fields_by_name['status'].containing_oneof = _TASKRESULT.oneofs_by_name['OutputType']
DESCRIPTOR.message_types_by_name['TaskCall'] = _TASKCALL
DESCRIPTOR.message_types_by_name['TaskInput'] = _TASKINPUT
DESCRIPTOR.message_types_by_name['TaskRequest'] = _TASKREQUEST
DESCRIPTOR.message_types_by_name['TaskResult'] = _TASKRESULT
DESCRIPTOR.message_types_by_name['Heartbeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['StdOutput'] = _STDOUTPUT
DESCRIPTOR.message_types_by_name['ErrOutput'] = _ERROUTPUT
DESCRIPTOR.message_types_by_name['ExitStatus'] = _EXITSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskCall = _reflection.GeneratedProtocolMessageType('TaskCall', (_message.Message,), {
  'DESCRIPTOR' : _TASKCALL,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.TaskCall)
  })
_sym_db.RegisterMessage(TaskCall)

TaskInput = _reflection.GeneratedProtocolMessageType('TaskInput', (_message.Message,), {
  'DESCRIPTOR' : _TASKINPUT,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.TaskInput)
  })
_sym_db.RegisterMessage(TaskInput)

TaskRequest = _reflection.GeneratedProtocolMessageType('TaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _TASKREQUEST,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.TaskRequest)
  })
_sym_db.RegisterMessage(TaskRequest)

TaskResult = _reflection.GeneratedProtocolMessageType('TaskResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESULT,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.TaskResult)
  })
_sym_db.RegisterMessage(TaskResult)

Heartbeat = _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEAT,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.Heartbeat)
  })
_sym_db.RegisterMessage(Heartbeat)

StdOutput = _reflection.GeneratedProtocolMessageType('StdOutput', (_message.Message,), {
  'DESCRIPTOR' : _STDOUTPUT,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.StdOutput)
  })
_sym_db.RegisterMessage(StdOutput)

ErrOutput = _reflection.GeneratedProtocolMessageType('ErrOutput', (_message.Message,), {
  'DESCRIPTOR' : _ERROUTPUT,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.ErrOutput)
  })
_sym_db.RegisterMessage(ErrOutput)

ExitStatus = _reflection.GeneratedProtocolMessageType('ExitStatus', (_message.Message,), {
  'DESCRIPTOR' : _EXITSTATUS,
  '__module__' : 'taskcall_pb2'
  # @@protoc_insertion_point(class_scope:pl.put.swolarz.remotetaskcall.ExitStatus)
  })
_sym_db.RegisterMessage(ExitStatus)


DESCRIPTOR._options = None

_TASKEXECUTIONSERVICE = _descriptor.ServiceDescriptor(
  name='TaskExecutionService',
  full_name='pl.put.swolarz.remotetaskcall.TaskExecutionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=614,
  serialized_end=741,
  methods=[
  _descriptor.MethodDescriptor(
    name='LaunchTask',
    full_name='pl.put.swolarz.remotetaskcall.TaskExecutionService.LaunchTask',
    index=0,
    containing_service=None,
    input_type=_TASKREQUEST,
    output_type=_TASKRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKEXECUTIONSERVICE)

DESCRIPTOR.services_by_name['TaskExecutionService'] = _TASKEXECUTIONSERVICE

# @@protoc_insertion_point(module_scope)
