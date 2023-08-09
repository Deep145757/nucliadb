"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import nucliadb_protos.standalone_pb2

class StandaloneClusterServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    NodeAction: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.standalone_pb2.NodeActionRequest,
        nucliadb_protos.standalone_pb2.NodeActionResponse,
    ]
    NodeInfo: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.standalone_pb2.NodeInfoRequest,
        nucliadb_protos.standalone_pb2.NodeInfoResponse,
    ]

class StandaloneClusterServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def NodeAction(
        self,
        request: nucliadb_protos.standalone_pb2.NodeActionRequest,
        context: grpc.ServicerContext,
    ) -> nucliadb_protos.standalone_pb2.NodeActionResponse: ...
    @abc.abstractmethod
    def NodeInfo(
        self,
        request: nucliadb_protos.standalone_pb2.NodeInfoRequest,
        context: grpc.ServicerContext,
    ) -> nucliadb_protos.standalone_pb2.NodeInfoResponse: ...

def add_StandaloneClusterServiceServicer_to_server(servicer: StandaloneClusterServiceServicer, server: grpc.Server) -> None: ...