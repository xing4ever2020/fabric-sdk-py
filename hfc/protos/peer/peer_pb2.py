# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/peer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.peer import proposal_pb2 as hfc_dot_protos_dot_peer_dot_proposal__pb2
from hfc.protos.peer import proposal_response_pb2 as hfc_dot_protos_dot_peer_dot_proposal__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/peer.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x1ahfc/protos/peer/peer.proto\x12\x06protos\x1a\x1ehfc/protos/peer/proposal.proto\x1a\'hfc/protos/peer/proposal_response.proto\"\x16\n\x06PeerID\x12\x0c\n\x04name\x18\x01 \x01(\t\";\n\x0cPeerEndpoint\x12\x1a\n\x02id\x18\x01 \x01(\x0b\x32\x0e.protos.PeerID\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t2Q\n\x08\x45ndorser\x12\x45\n\x0fProcessProposal\x12\x16.protos.SignedProposal\x1a\x18.protos.ProposalResponse\"\x00\x42+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
  ,
  dependencies=[hfc_dot_protos_dot_peer_dot_proposal__pb2.DESCRIPTOR,hfc_dot_protos_dot_peer_dot_proposal__response__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PEERID = _descriptor.Descriptor(
  name='PeerID',
  full_name='protos.PeerID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protos.PeerID.name', index=0,
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
  serialized_start=111,
  serialized_end=133,
)


_PEERENDPOINT = _descriptor.Descriptor(
  name='PeerEndpoint',
  full_name='protos.PeerEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protos.PeerEndpoint.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='protos.PeerEndpoint.address', index=1,
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
  serialized_start=135,
  serialized_end=194,
)

_PEERENDPOINT.fields_by_name['id'].message_type = _PEERID
DESCRIPTOR.message_types_by_name['PeerID'] = _PEERID
DESCRIPTOR.message_types_by_name['PeerEndpoint'] = _PEERENDPOINT

PeerID = _reflection.GeneratedProtocolMessageType('PeerID', (_message.Message,), dict(
  DESCRIPTOR = _PEERID,
  __module__ = 'hfc.protos.peer.peer_pb2'
  # @@protoc_insertion_point(class_scope:protos.PeerID)
  ))
_sym_db.RegisterMessage(PeerID)

PeerEndpoint = _reflection.GeneratedProtocolMessageType('PeerEndpoint', (_message.Message,), dict(
  DESCRIPTOR = _PEERENDPOINT,
  __module__ = 'hfc.protos.peer.peer_pb2'
  # @@protoc_insertion_point(class_scope:protos.PeerEndpoint)
  ))
_sym_db.RegisterMessage(PeerEndpoint)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/hyperledger/fabric/protos/peer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class EndorserStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.ProcessProposal = channel.unary_unary(
          '/protos.Endorser/ProcessProposal',
          request_serializer=hfc_dot_protos_dot_peer_dot_proposal__pb2.SignedProposal.SerializeToString,
          response_deserializer=hfc_dot_protos_dot_peer_dot_proposal__response__pb2.ProposalResponse.FromString,
          )


  class EndorserServicer(object):

    def ProcessProposal(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_EndorserServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ProcessProposal': grpc.unary_unary_rpc_method_handler(
            servicer.ProcessProposal,
            request_deserializer=hfc_dot_protos_dot_peer_dot_proposal__pb2.SignedProposal.FromString,
            response_serializer=hfc_dot_protos_dot_peer_dot_proposal__response__pb2.ProposalResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'protos.Endorser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaEndorserServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def ProcessProposal(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaEndorserStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def ProcessProposal(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    ProcessProposal.future = None


  def beta_create_Endorser_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('protos.Endorser', 'ProcessProposal'): hfc_dot_protos_dot_peer_dot_proposal__pb2.SignedProposal.FromString,
    }
    response_serializers = {
      ('protos.Endorser', 'ProcessProposal'): hfc_dot_protos_dot_peer_dot_proposal__response__pb2.ProposalResponse.SerializeToString,
    }
    method_implementations = {
      ('protos.Endorser', 'ProcessProposal'): face_utilities.unary_unary_inline(servicer.ProcessProposal),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Endorser_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('protos.Endorser', 'ProcessProposal'): hfc_dot_protos_dot_peer_dot_proposal__pb2.SignedProposal.SerializeToString,
    }
    response_deserializers = {
      ('protos.Endorser', 'ProcessProposal'): hfc_dot_protos_dot_peer_dot_proposal__response__pb2.ProposalResponse.FromString,
    }
    cardinalities = {
      'ProcessProposal': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'protos.Endorser', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
