import asyncio
from loguru import logger
import time
import grpc
from gen_py.helloworld_pb2 import HelloRequest
from gen_py.helloworld_pb2_grpc import GreeterStub


async def run(port):
    start_ = time.time()
    logger.info(f'start {port=} {start_=}')
    async with grpc.aio.insecure_channel(f"localhost:{port}") as channel:
        stub = GreeterStub(channel)
        response = await stub.SayHello(HelloRequest(name="you", id=23, payload=[1, 0, 0, 0]))
    logger.info("Greeter client received: " + f"\n{response=}")
    return time.time() - start_


async def main():
    tasks = []
    loop = asyncio.get_event_loop()
    for i in range(1, 6):
        port = f'505{i}'
        logger.info(f'create {port=}')
        task = run(port)
        tasks.append(task)
    logger.info('done')

    logger.info('start gather')
    times = await asyncio.gather(*tasks)
    logger.info(f'\n {times=}')


if __name__ == '__main__':
    asyncio.run(main())
