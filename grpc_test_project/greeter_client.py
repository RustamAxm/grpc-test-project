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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import time

from loguru import logger

import grpc
from gen_py.helloworld_pb2 import HelloRequest
from gen_py.helloworld_pb2_grpc import GreeterStub


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    logger.info("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = GreeterStub(channel)
        response = stub.SayHello(HelloRequest(name="you", id=23, payload=[1, 0, 0, 0]))
    logger.info("Greeter client received: " + f"\n{response=}")

def run_bench():
    logger.info("Will try to greet world ...")
    times = []
    ports = []
    for i in range(1, 6):
        start_  = time.time()
        port = f'505{i}'
        ports.append(port)
        with grpc.insecure_channel(f"localhost:{port}") as channel:
            stub = GreeterStub(channel)
            response = stub.SayHello(HelloRequest(name="you", id=23, payload=[1, 0, 0, 0]))
        times.append(time.time() - start_)
        logger.info("Greeter client received: " + f"\n{response=}")

    logger.info(f'total: \n {ports=} \n {times=}')


if __name__ == "__main__":
    run()
