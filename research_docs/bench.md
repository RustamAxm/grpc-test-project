# test for docker cpus usage
run container  [creator](../run_conteiners.sh)
```bash 
rustam@nb-ubuntu-02:~/grpc-test-project$ ./run_conteiners.sh create
+ action=create
+ [[ create == \c\r\e\a\t\e ]]
+ for i in {1..5}
+ docker run -d --cpus=0.1 --memory=64m --name test-grpc-1 --network bridge -p 5051:50051 grpc-test
218833d20c5b6911e55d574bcad6a7b9cde43928d33cdb929701ae8bdc1b1c0d
+ for i in {1..5}
+ docker run -d --cpus=0.2 --memory=64m --name test-grpc-2 --network bridge -p 5052:50051 grpc-test
42e9992db0b767ed637b9583329d92d2b0f05df2e1c60b8ffe087a78b3583626
+ for i in {1..5}
+ docker run -d --cpus=0.3 --memory=64m --name test-grpc-3 --network bridge -p 5053:50051 grpc-test
3299a53e56d7b8b1004bf6003730c40cdb2d954e954ba95d25d22ad04db32b7f
+ for i in {1..5}
+ docker run -d --cpus=0.4 --memory=64m --name test-grpc-4 --network bridge -p 5054:50051 grpc-test
7d1e333b1a8a33dfc4ba3b4fb4c8125f6725852923a31ae3ad8ac52bc8db76d4
+ for i in {1..5}
+ docker run -d --cpus=0.5 --memory=64m --name test-grpc-5 --network bridge -p 5055:50051 grpc-test
8603eaa5be4368b13bff33a355aba4d4f9c9e5d88eeeb96b7d676b0558902757
```
check ports 
```bash 
rustam@nb-ubuntu-02:~/grpc-test-project$ docker ps
CONTAINER ID   IMAGE                                       COMMAND                  CREATED              STATUS              PORTS                                         NAMES
d4ec63818b98   grpc-test                                   "python /app/grpc_te…"   About a minute ago   Up About a minute   0.0.0.0:5055->50051/tcp, :::5055->50051/tcp   test-grpc-5
033209b8a209   grpc-test                                   "python /app/grpc_te…"   About a minute ago   Up About a minute   0.0.0.0:5054->50051/tcp, :::5054->50051/tcp   test-grpc-4
c2c5540e2b4d   grpc-test                                   "python /app/grpc_te…"   About a minute ago   Up About a minute   0.0.0.0:5053->50051/tcp, :::5053->50051/tcp   test-grpc-3
65376e61d18e   grpc-test                                   "python /app/grpc_te…"   About a minute ago   Up About a minute   0.0.0.0:5052->50051/tcp, :::5052->50051/tcp   test-grpc-2
d1831720cdd7   grpc-test                                   "python /app/grpc_te…"   About a minute ago   Up About a minute   0.0.0.0:5051->50051/tcp, :::5051->50051/tcp   test-grpc-1

```
run bench 

```bash 
2024-09-01 15:36:42.634 | INFO     | __main__:run_bench:51 - total: 
 ports=['5051', '5052', '5053', '5054', '5055'] 
 times=[116.99554181098938, 35.52334523200989, 19.87320375442505, 14.459768772125244, 10.743802070617676]
```