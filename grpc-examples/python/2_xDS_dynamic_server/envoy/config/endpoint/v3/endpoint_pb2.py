# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: envoy/config/endpoint/v3/endpoint.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'envoy/config/endpoint/v3/endpoint.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.endpoint.v3 import endpoint_components_pb2 as envoy_dot_config_dot_endpoint_dot_v3_dot_endpoint__components__pb2
from envoy.type.v3 import percent_pb2 as envoy_dot_type_dot_v3_dot_percent__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'envoy/config/endpoint/v3/endpoint.proto\x12\x18\x65nvoy.config.endpoint.v3\x1a\x32\x65nvoy/config/endpoint/v3/endpoint_components.proto\x1a\x1b\x65nvoy/type/v3/percent.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xb7\x07\n\x15\x43lusterLoadAssignment\x12\x1d\n\x0c\x63luster_name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12@\n\tendpoints\x18\x02 \x03(\x0b\x32-.envoy.config.endpoint.v3.LocalityLbEndpoints\x12\\\n\x0fnamed_endpoints\x18\x05 \x03(\x0b\x32\x43.envoy.config.endpoint.v3.ClusterLoadAssignment.NamedEndpointsEntry\x12\x46\n\x06policy\x18\x04 \x01(\x0b\x32\x36.envoy.config.endpoint.v3.ClusterLoadAssignment.Policy\x1a\x90\x04\n\x06Policy\x12[\n\x0e\x64rop_overloads\x18\x02 \x03(\x0b\x32\x43.envoy.config.endpoint.v3.ClusterLoadAssignment.Policy.DropOverload\x12\x46\n\x17overprovisioning_factor\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x07\xfa\x42\x04*\x02 \x00\x12\x41\n\x14\x65ndpoint_stale_after\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02*\x00\x12 \n\x18weighted_priority_health\x18\x06 \x01(\x08\x1a\xa3\x01\n\x0c\x44ropOverload\x12\x19\n\x08\x63\x61tegory\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x39\n\x0f\x64rop_percentage\x18\x02 \x01(\x0b\x32 .envoy.type.v3.FractionalPercent:=\x9a\xc5\x88\x1e\x38\n6envoy.api.v2.ClusterLoadAssignment.Policy.DropOverload:0\x9a\xc5\x88\x1e+\n)envoy.api.v2.ClusterLoadAssignment.PolicyJ\x04\x08\x01\x10\x02J\x04\x08\x05\x10\x06R\x18\x64isable_overprovisioning\x1aY\n\x13NamedEndpointsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".envoy.config.endpoint.v3.Endpoint:\x02\x38\x01:)\x9a\xc5\x88\x1e$\n\"envoy.api.v2.ClusterLoadAssignmentB\x8d\x01\n&io.envoyproxy.envoy.config.endpoint.v3B\rEndpointProtoP\x01ZJgithub.com/envoyproxy/go-control-plane/envoy/config/endpoint/v3;endpointv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.endpoint.v3.endpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&io.envoyproxy.envoy.config.endpoint.v3B\rEndpointProtoP\001ZJgithub.com/envoyproxy/go-control-plane/envoy/config/endpoint/v3;endpointv3\272\200\310\321\006\002\020\002'
  _globals['_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD'].fields_by_name['category']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD'].fields_by_name['category']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD']._serialized_options = b'\232\305\210\0368\n6envoy.api.v2.ClusterLoadAssignment.Policy.DropOverload'
  _globals['_CLUSTERLOADASSIGNMENT_POLICY'].fields_by_name['overprovisioning_factor']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT_POLICY'].fields_by_name['overprovisioning_factor']._serialized_options = b'\372B\004*\002 \000'
  _globals['_CLUSTERLOADASSIGNMENT_POLICY'].fields_by_name['endpoint_stale_after']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT_POLICY'].fields_by_name['endpoint_stale_after']._serialized_options = b'\372B\005\252\001\002*\000'
  _globals['_CLUSTERLOADASSIGNMENT_POLICY']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT_POLICY']._serialized_options = b'\232\305\210\036+\n)envoy.api.v2.ClusterLoadAssignment.Policy'
  _globals['_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY']._serialized_options = b'8\001'
  _globals['_CLUSTERLOADASSIGNMENT'].fields_by_name['cluster_name']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT'].fields_by_name['cluster_name']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_CLUSTERLOADASSIGNMENT']._loaded_options = None
  _globals['_CLUSTERLOADASSIGNMENT']._serialized_options = b'\232\305\210\036$\n\"envoy.api.v2.ClusterLoadAssignment'
  _globals['_CLUSTERLOADASSIGNMENT']._serialized_start=306
  _globals['_CLUSTERLOADASSIGNMENT']._serialized_end=1257
  _globals['_CLUSTERLOADASSIGNMENT_POLICY']._serialized_start=595
  _globals['_CLUSTERLOADASSIGNMENT_POLICY']._serialized_end=1123
  _globals['_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD']._serialized_start=872
  _globals['_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD']._serialized_end=1035
  _globals['_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY']._serialized_start=1125
  _globals['_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY']._serialized_end=1214
# @@protoc_insertion_point(module_scope)
