# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import inference_service_pb2 as inference__service__pb2


class InferenceServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.predict = channel.unary_unary(
        '/com.webank.ai.fate.api.serving.InferenceService/predict',
        request_serializer=inference__service__pb2.InferenceRequest.SerializeToString,
        response_deserializer=inference__service__pb2.InferenceResponse.FromString,
        )


class InferenceServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def predict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InferenceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'predict': grpc.unary_unary_rpc_method_handler(
          servicer.predict,
          request_deserializer=inference__service__pb2.InferenceRequest.FromString,
          response_serializer=inference__service__pb2.InferenceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.fate.api.serving.InferenceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
