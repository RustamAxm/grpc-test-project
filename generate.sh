#!/bin/bash -ex

mkdir -p gen_py
cp helloworld.proto ./gen_py/.
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./gen_py/helloworld.proto

