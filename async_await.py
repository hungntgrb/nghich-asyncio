import time
import asyncio


async def myfunc(n):
    print(f'myfunc({n}) runs!')
    x = 0
    for i in range(n):
        x += i

    # Can cai nay tell this func's gonna suspend.
    await asyncio.sleep(0.02)
    # time.sleep(0.02)
    return x


async def main():
    t0 = time.time()
    await asyncio.wait([
        myfunc(100000),
        myfunc(10000),
        myfunc(1000),
    ])
    t1 = time.time()
    print(f"Took {(t1 - t0)*1000} ms.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
