// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var registry_registry_pb = require('../registry/registry_pb.js');

function serialize_go_micro_registry_EmptyResponse(arg) {
  if (!(arg instanceof registry_registry_pb.EmptyResponse)) {
    throw new Error('Expected argument of type go.micro.registry.EmptyResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_EmptyResponse(buffer_arg) {
  return registry_registry_pb.EmptyResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_go_micro_registry_GetRequest(arg) {
  if (!(arg instanceof registry_registry_pb.GetRequest)) {
    throw new Error('Expected argument of type go.micro.registry.GetRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_GetRequest(buffer_arg) {
  return registry_registry_pb.GetRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_go_micro_registry_GetResponse(arg) {
  if (!(arg instanceof registry_registry_pb.GetResponse)) {
    throw new Error('Expected argument of type go.micro.registry.GetResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_GetResponse(buffer_arg) {
  return registry_registry_pb.GetResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_go_micro_registry_ListRequest(arg) {
  if (!(arg instanceof registry_registry_pb.ListRequest)) {
    throw new Error('Expected argument of type go.micro.registry.ListRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_ListRequest(buffer_arg) {
  return registry_registry_pb.ListRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_go_micro_registry_ListResponse(arg) {
  if (!(arg instanceof registry_registry_pb.ListResponse)) {
    throw new Error('Expected argument of type go.micro.registry.ListResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_ListResponse(buffer_arg) {
  return registry_registry_pb.ListResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_go_micro_registry_Result(arg) {
  if (!(arg instanceof registry_registry_pb.Result)) {
    throw new Error('Expected argument of type go.micro.registry.Result');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_Result(buffer_arg) {
  return registry_registry_pb.Result.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_go_micro_registry_Service(arg) {
  if (!(arg instanceof registry_registry_pb.Service)) {
    throw new Error('Expected argument of type go.micro.registry.Service');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_Service(buffer_arg) {
  return registry_registry_pb.Service.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_go_micro_registry_WatchRequest(arg) {
  if (!(arg instanceof registry_registry_pb.WatchRequest)) {
    throw new Error('Expected argument of type go.micro.registry.WatchRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_go_micro_registry_WatchRequest(buffer_arg) {
  return registry_registry_pb.WatchRequest.deserializeBinary(new Uint8Array(buffer_arg));
}


var RegistryService = exports.RegistryService = {
  getService: {
    path: '/go.micro.registry.Registry/GetService',
    requestStream: false,
    responseStream: false,
    requestType: registry_registry_pb.GetRequest,
    responseType: registry_registry_pb.GetResponse,
    requestSerialize: serialize_go_micro_registry_GetRequest,
    requestDeserialize: deserialize_go_micro_registry_GetRequest,
    responseSerialize: serialize_go_micro_registry_GetResponse,
    responseDeserialize: deserialize_go_micro_registry_GetResponse,
  },
  register: {
    path: '/go.micro.registry.Registry/Register',
    requestStream: false,
    responseStream: false,
    requestType: registry_registry_pb.Service,
    responseType: registry_registry_pb.EmptyResponse,
    requestSerialize: serialize_go_micro_registry_Service,
    requestDeserialize: deserialize_go_micro_registry_Service,
    responseSerialize: serialize_go_micro_registry_EmptyResponse,
    responseDeserialize: deserialize_go_micro_registry_EmptyResponse,
  },
  deregister: {
    path: '/go.micro.registry.Registry/Deregister',
    requestStream: false,
    responseStream: false,
    requestType: registry_registry_pb.Service,
    responseType: registry_registry_pb.EmptyResponse,
    requestSerialize: serialize_go_micro_registry_Service,
    requestDeserialize: deserialize_go_micro_registry_Service,
    responseSerialize: serialize_go_micro_registry_EmptyResponse,
    responseDeserialize: deserialize_go_micro_registry_EmptyResponse,
  },
  listServices: {
    path: '/go.micro.registry.Registry/ListServices',
    requestStream: false,
    responseStream: false,
    requestType: registry_registry_pb.ListRequest,
    responseType: registry_registry_pb.ListResponse,
    requestSerialize: serialize_go_micro_registry_ListRequest,
    requestDeserialize: deserialize_go_micro_registry_ListRequest,
    responseSerialize: serialize_go_micro_registry_ListResponse,
    responseDeserialize: deserialize_go_micro_registry_ListResponse,
  },
  watch: {
    path: '/go.micro.registry.Registry/Watch',
    requestStream: false,
    responseStream: true,
    requestType: registry_registry_pb.WatchRequest,
    responseType: registry_registry_pb.Result,
    requestSerialize: serialize_go_micro_registry_WatchRequest,
    requestDeserialize: deserialize_go_micro_registry_WatchRequest,
    responseSerialize: serialize_go_micro_registry_Result,
    responseDeserialize: deserialize_go_micro_registry_Result,
  },
};

exports.RegistryClient = grpc.makeGenericClientConstructor(RegistryService);
