#!/bin/bash -ex

action=${1:-create}

if [[ $action == "create" ]];
then
for i in {1..5};
  do docker run -d --cpus="0.${i}" --memory="64m" --name test-grpc-$i --network bridge -p "505${i}:50051" grpc-test;
done;
else
for i in {1..5};
  do docker stop test-grpc-$i && docker rm test-grpc-$i;
done;
fi
