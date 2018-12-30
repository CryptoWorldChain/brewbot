# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tx.proto',
  package='org.csc.evmapi.gens',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x08tx.proto\x12\x13org.csc.evmapi.gens\"\xb8\x01\n\x10MultiTransaction\x12\x0e\n\x06txHash\x18\x01 \x01(\t\x12\x39\n\x06txBody\x18\x02 \x01(\x0b\x32).org.csc.evmapi.gens.MultiTransactionBody\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x39\n\x06txNode\x18\x04 \x01(\x0b\x32).org.csc.evmapi.gens.MultiTransactionNode\x12\x0e\n\x06result\x18\x05 \x01(\x0c\"\xa5\x02\n\x14MultiTransactionBody\x12:\n\x06inputs\x18\x01 \x03(\x0b\x32*.org.csc.evmapi.gens.MultiTransactionInput\x12<\n\x07outputs\x18\x02 \x03(\x0b\x32+.org.csc.evmapi.gens.MultiTransactionOutput\x12\x0e\n\x06\x65xdata\x18\x03 \x01(\x0c\x12\x42\n\nsignatures\x18\x04 \x03(\x0b\x32..org.csc.evmapi.gens.MultiTransactionSignature\x12\x10\n\x08\x64\x65legate\x18\x05 \x03(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x11\n\ttimestamp\x18\x07 \x01(\x03\x12\x0c\n\x04type\x18\x08 \x01(\x05\"{\n\x15MultiTransactionInput\x12\r\n\x05nonce\x18\x01 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x0c\x12\r\n\x05token\x18\x07 \x01(\t\x12\x0e\n\x06symbol\x18\x08 \x01(\t\x12\x13\n\x0b\x63ryptoToken\x18\t \x01(\x0c\"^\n\x16MultiTransactionOutput\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x0c\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x13\n\x0b\x63ryptoToken\x18\x04 \x01(\x0c\".\n\x19MultiTransactionSignature\x12\x11\n\tsignature\x18\x01 \x01(\x0c\"D\n\x14MultiTransactionNode\x12\x0c\n\x04node\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\x12\r\n\x05\x62\x63uid\x18\x03 \x01(\t\":\n\x17\x42roadcastTransactionMsg\x12\x0e\n\x06txHash\x18\x01 \x03(\x0c\x12\x0f\n\x07txDatas\x18\x02 \x03(\x0c\"]\n\x0f\x43ryptoTokenData\x12\r\n\x05total\x18\x01 \x01(\x03\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0f\n\x07\x65xtData\x18\x03 \x01(\x0c\x12\x0c\n\x04name\x18\x04 \x03(\t\x12\x0c\n\x04\x63ode\x18\x05 \x03(\t\"X\n\x10UnionAccountData\x12\x0b\n\x03max\x18\x01 \x01(\x0c\x12\x11\n\tacceptMax\x18\x02 \x01(\x0c\x12\x13\n\x0b\x61\x63\x63\x65ptLimit\x18\x03 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x03(\x0c\"G\n\x0cSanctionData\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x16\n\x0e\x65ndBlockHeight\x18\x02 \x01(\x03\x12\x0e\n\x06result\x18\x03 \x01(\x0c\x62\x06proto3')
)




_MULTITRANSACTION = _descriptor.Descriptor(
  name='MultiTransaction',
  full_name='org.csc.evmapi.gens.MultiTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txHash', full_name='org.csc.evmapi.gens.MultiTransaction.txHash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txBody', full_name='org.csc.evmapi.gens.MultiTransaction.txBody', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='org.csc.evmapi.gens.MultiTransaction.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txNode', full_name='org.csc.evmapi.gens.MultiTransaction.txNode', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='org.csc.evmapi.gens.MultiTransaction.result', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=34,
  serialized_end=218,
)


_MULTITRANSACTIONBODY = _descriptor.Descriptor(
  name='MultiTransactionBody',
  full_name='org.csc.evmapi.gens.MultiTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='org.csc.evmapi.gens.MultiTransactionBody.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='org.csc.evmapi.gens.MultiTransactionBody.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exdata', full_name='org.csc.evmapi.gens.MultiTransactionBody.exdata', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='org.csc.evmapi.gens.MultiTransactionBody.signatures', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegate', full_name='org.csc.evmapi.gens.MultiTransactionBody.delegate', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='org.csc.evmapi.gens.MultiTransactionBody.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='org.csc.evmapi.gens.MultiTransactionBody.timestamp', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='org.csc.evmapi.gens.MultiTransactionBody.type', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=221,
  serialized_end=514,
)


_MULTITRANSACTIONINPUT = _descriptor.Descriptor(
  name='MultiTransactionInput',
  full_name='org.csc.evmapi.gens.MultiTransactionInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='org.csc.evmapi.gens.MultiTransactionInput.nonce', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='org.csc.evmapi.gens.MultiTransactionInput.address', index=1,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='org.csc.evmapi.gens.MultiTransactionInput.amount', index=2,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='org.csc.evmapi.gens.MultiTransactionInput.token', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='org.csc.evmapi.gens.MultiTransactionInput.symbol', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cryptoToken', full_name='org.csc.evmapi.gens.MultiTransactionInput.cryptoToken', index=5,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=516,
  serialized_end=639,
)


_MULTITRANSACTIONOUTPUT = _descriptor.Descriptor(
  name='MultiTransactionOutput',
  full_name='org.csc.evmapi.gens.MultiTransactionOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='org.csc.evmapi.gens.MultiTransactionOutput.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='org.csc.evmapi.gens.MultiTransactionOutput.amount', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='org.csc.evmapi.gens.MultiTransactionOutput.symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cryptoToken', full_name='org.csc.evmapi.gens.MultiTransactionOutput.cryptoToken', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=641,
  serialized_end=735,
)


_MULTITRANSACTIONSIGNATURE = _descriptor.Descriptor(
  name='MultiTransactionSignature',
  full_name='org.csc.evmapi.gens.MultiTransactionSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='org.csc.evmapi.gens.MultiTransactionSignature.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=737,
  serialized_end=783,
)


_MULTITRANSACTIONNODE = _descriptor.Descriptor(
  name='MultiTransactionNode',
  full_name='org.csc.evmapi.gens.MultiTransactionNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='org.csc.evmapi.gens.MultiTransactionNode.node', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='org.csc.evmapi.gens.MultiTransactionNode.address', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bcuid', full_name='org.csc.evmapi.gens.MultiTransactionNode.bcuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=785,
  serialized_end=853,
)


_BROADCASTTRANSACTIONMSG = _descriptor.Descriptor(
  name='BroadcastTransactionMsg',
  full_name='org.csc.evmapi.gens.BroadcastTransactionMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txHash', full_name='org.csc.evmapi.gens.BroadcastTransactionMsg.txHash', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txDatas', full_name='org.csc.evmapi.gens.BroadcastTransactionMsg.txDatas', index=1,
      number=2, type=12, cpp_type=9, label=3,
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
  serialized_start=855,
  serialized_end=913,
)


_CRYPTOTOKENDATA = _descriptor.Descriptor(
  name='CryptoTokenData',
  full_name='org.csc.evmapi.gens.CryptoTokenData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='org.csc.evmapi.gens.CryptoTokenData.total', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='org.csc.evmapi.gens.CryptoTokenData.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extData', full_name='org.csc.evmapi.gens.CryptoTokenData.extData', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.csc.evmapi.gens.CryptoTokenData.name', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='org.csc.evmapi.gens.CryptoTokenData.code', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=915,
  serialized_end=1008,
)


_UNIONACCOUNTDATA = _descriptor.Descriptor(
  name='UnionAccountData',
  full_name='org.csc.evmapi.gens.UnionAccountData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max', full_name='org.csc.evmapi.gens.UnionAccountData.max', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceptMax', full_name='org.csc.evmapi.gens.UnionAccountData.acceptMax', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceptLimit', full_name='org.csc.evmapi.gens.UnionAccountData.acceptLimit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='org.csc.evmapi.gens.UnionAccountData.address', index=3,
      number=4, type=12, cpp_type=9, label=3,
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
  serialized_start=1010,
  serialized_end=1098,
)


_SANCTIONDATA = _descriptor.Descriptor(
  name='SanctionData',
  full_name='org.csc.evmapi.gens.SanctionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='org.csc.evmapi.gens.SanctionData.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endBlockHeight', full_name='org.csc.evmapi.gens.SanctionData.endBlockHeight', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='org.csc.evmapi.gens.SanctionData.result', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1100,
  serialized_end=1171,
)

_MULTITRANSACTION.fields_by_name['txBody'].message_type = _MULTITRANSACTIONBODY
_MULTITRANSACTION.fields_by_name['txNode'].message_type = _MULTITRANSACTIONNODE
_MULTITRANSACTIONBODY.fields_by_name['inputs'].message_type = _MULTITRANSACTIONINPUT
_MULTITRANSACTIONBODY.fields_by_name['outputs'].message_type = _MULTITRANSACTIONOUTPUT
_MULTITRANSACTIONBODY.fields_by_name['signatures'].message_type = _MULTITRANSACTIONSIGNATURE
DESCRIPTOR.message_types_by_name['MultiTransaction'] = _MULTITRANSACTION
DESCRIPTOR.message_types_by_name['MultiTransactionBody'] = _MULTITRANSACTIONBODY
DESCRIPTOR.message_types_by_name['MultiTransactionInput'] = _MULTITRANSACTIONINPUT
DESCRIPTOR.message_types_by_name['MultiTransactionOutput'] = _MULTITRANSACTIONOUTPUT
DESCRIPTOR.message_types_by_name['MultiTransactionSignature'] = _MULTITRANSACTIONSIGNATURE
DESCRIPTOR.message_types_by_name['MultiTransactionNode'] = _MULTITRANSACTIONNODE
DESCRIPTOR.message_types_by_name['BroadcastTransactionMsg'] = _BROADCASTTRANSACTIONMSG
DESCRIPTOR.message_types_by_name['CryptoTokenData'] = _CRYPTOTOKENDATA
DESCRIPTOR.message_types_by_name['UnionAccountData'] = _UNIONACCOUNTDATA
DESCRIPTOR.message_types_by_name['SanctionData'] = _SANCTIONDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MultiTransaction = _reflection.GeneratedProtocolMessageType('MultiTransaction', (_message.Message,), dict(
  DESCRIPTOR = _MULTITRANSACTION,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.MultiTransaction)
  ))
_sym_db.RegisterMessage(MultiTransaction)

MultiTransactionBody = _reflection.GeneratedProtocolMessageType('MultiTransactionBody', (_message.Message,), dict(
  DESCRIPTOR = _MULTITRANSACTIONBODY,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.MultiTransactionBody)
  ))
_sym_db.RegisterMessage(MultiTransactionBody)

MultiTransactionInput = _reflection.GeneratedProtocolMessageType('MultiTransactionInput', (_message.Message,), dict(
  DESCRIPTOR = _MULTITRANSACTIONINPUT,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.MultiTransactionInput)
  ))
_sym_db.RegisterMessage(MultiTransactionInput)

MultiTransactionOutput = _reflection.GeneratedProtocolMessageType('MultiTransactionOutput', (_message.Message,), dict(
  DESCRIPTOR = _MULTITRANSACTIONOUTPUT,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.MultiTransactionOutput)
  ))
_sym_db.RegisterMessage(MultiTransactionOutput)

MultiTransactionSignature = _reflection.GeneratedProtocolMessageType('MultiTransactionSignature', (_message.Message,), dict(
  DESCRIPTOR = _MULTITRANSACTIONSIGNATURE,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.MultiTransactionSignature)
  ))
_sym_db.RegisterMessage(MultiTransactionSignature)

MultiTransactionNode = _reflection.GeneratedProtocolMessageType('MultiTransactionNode', (_message.Message,), dict(
  DESCRIPTOR = _MULTITRANSACTIONNODE,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.MultiTransactionNode)
  ))
_sym_db.RegisterMessage(MultiTransactionNode)

BroadcastTransactionMsg = _reflection.GeneratedProtocolMessageType('BroadcastTransactionMsg', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTTRANSACTIONMSG,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.BroadcastTransactionMsg)
  ))
_sym_db.RegisterMessage(BroadcastTransactionMsg)

CryptoTokenData = _reflection.GeneratedProtocolMessageType('CryptoTokenData', (_message.Message,), dict(
  DESCRIPTOR = _CRYPTOTOKENDATA,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.CryptoTokenData)
  ))
_sym_db.RegisterMessage(CryptoTokenData)

UnionAccountData = _reflection.GeneratedProtocolMessageType('UnionAccountData', (_message.Message,), dict(
  DESCRIPTOR = _UNIONACCOUNTDATA,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.UnionAccountData)
  ))
_sym_db.RegisterMessage(UnionAccountData)

SanctionData = _reflection.GeneratedProtocolMessageType('SanctionData', (_message.Message,), dict(
  DESCRIPTOR = _SANCTIONDATA,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:org.csc.evmapi.gens.SanctionData)
  ))
_sym_db.RegisterMessage(SanctionData)


# @@protoc_insertion_point(module_scope)
