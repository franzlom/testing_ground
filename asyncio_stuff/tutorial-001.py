import asyncio
import time

a = [123, 321, 123]


async def another_function():
    return a


async def run():
    print('what')
    await asyncio.sleep(1)
    a = await another_function()
    print(a)
    print('now')


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(run())
    print("--- %s seconds ---" % (time.time() - start_time))
