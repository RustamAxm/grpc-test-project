# performance docker containers with supported tools
## benchmark quat rotation
```python
def quat_action(to_proc):
    logger.info(f'{to_proc=}')
    for i in range(10000000):
        inst = np.quaternion(*to_proc)
        rotate = np.quaternion(0.0, -0.75, 0.0, 0.75)
        new_inst = inst * rotate
    to_ret = quaternion.as_float_array(new_inst).tolist()
    logger.info(f'{to_ret=}')
    return to_ret
```
## without container
```bash
2024-08-25 16:41:34.692 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 16:41:39.065 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]
```
## default run 
4 second operation 
```bash
docker run -it --rm --name test-grpc --network host grpc-test                                                                                           

2024-08-25 13:36:24.306 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 13:36:28.971 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```
## cpus

```bash 
docker run -it --rm --cpus=".5" --name test-grpc --network host grpc-test 
2024-08-25 14:13:35.019 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:13:46.171 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```
```bash
docker run -it --rm --cpus="1" --name test-grpc --network host grpc-test 
2024-08-25 14:16:30.699 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:16:35.439 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
docker run -it --rm --cpus="2" --name test-grpc --network host grpc-test 
2024-08-25 14:18:20.845 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:18:25.697 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```
```bash
docker run -it --rm --cpus="3" --name test-grpc --network host grpc-test 
2024-08-25 14:19:37.731 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:19:42.443 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```
```bash
docker run -it --rm --cpus="0.1" --name test-grpc --network host grpc-test 
2024-08-25 14:21:32.015 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:23:29.413 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
 docker run -it --rm --cpus="0.25" --name test-grpc --network host grpc-test 
2024-08-25 14:24:02.144 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:24:27.970 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

## memory
```bash
docker run -it --rm --cpus="0.5" --memory="512m" --name test-grpc --network host grpc-test 

2024-08-25 14:31:56.201 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:32:06.940 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
docker run -it --rm --cpus="0.5" --memory="256m" --name test-grpc --network host grpc-test 

2024-08-25 14:33:18.129 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:33:29.297 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
docker run -it --rm --cpus="0.5" --memory="128m" --name test-grpc --network host grpc-test 

2024-08-25 14:35:25.159 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:35:36.149 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
docker run -it --rm --cpus="0.5" --memory="64m" --name test-grpc --network host grpc-test 

2024-08-25 14:36:57.086 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:37:07.940 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
 docker run -it --rm --cpus="0.5" --memory="32m" --name test-grpc --network host grpc-test 
 
2024-08-25 14:38:21.084 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:38:31.825 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
docker run -it --rm --cpus="0.5" --memory="16m" --name test-grpc --network host grpc-test

2024-08-25 14:39:56.269 | INFO     | grpc_test_project.numpy_quaternion:quat_action:21 - to_proc=[1.0, 0.0, 0.0, 0.0]
2024-08-25 14:40:07.026 | INFO     | grpc_test_project.numpy_quaternion:quat_action:27 - to_ret=[0.0, -0.75, 0.0, 0.75]

```

```bash
docker run -it --rm --cpus="0.5" --memory="8m" --name test-grpc --network host grpc-test - too small
```