# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures

import grpc
from gen_py.helloworld_pb2 import HelloReply
from gen_py.helloworld_pb2_grpc import add_GreeterServicer_to_server, GreeterServicer
from loguru import logger
from grpc_test_project.numpy_quaternion import quat_action

class Greeter(GreeterServicer):
    def SayHello(self, request, context):
        logger.info("in sender")
        logger.info(f"\n{request=}")
        ret_out = quat_action(request.payload)
        return HelloReply(
            message=f"Hello, {request.name}",
            id=request.id,
            payload=ret_out,
        )


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    logger.info("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
