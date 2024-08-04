# grpc test repo
## install 
```
sudo pip install grpcio
sudo pip install grpcio-tools
```
## edit proto file
```
syntax = "proto3";

option java_multiple_files = true;
option java_package = "io.grpc.examples.helloworld";
option java_outer_classname = "HelloWorldProto";
option objc_class_prefix = "HLW";

package helloworld;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}

}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
  uint32 id = 2;
  repeated uint32 payload = 3;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
  uint32 id = 2;
  repeated uint32 payload = 3;
}

```
## generate methods
```
./generate.sh
```
```bash
rustam@rustam-ZenBook-UX431DA-UM431DA:~/grpc-test-project$ cat generate.sh 
#!/bin/bash -ex

mkdir -p gen_py
cp helloworld.proto ./gen_py/.
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./gen_py/helloworld.proto


```
## run
server
```
python3 greeter_server.py
```
client 
```
python3 greeter_client.py 

```
## deps
```
python3 -m grpc_tools.protoc --version
libprotoc 26.1

```
## Docker demo
build 
```bash
docker build -t grpc-test .
```
run container
```bash
docker run -it --rm --name test-grpc --network host grpc-test 
```
