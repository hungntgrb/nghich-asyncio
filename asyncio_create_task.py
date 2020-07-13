import asyncio
import time


async def delay(amount: float):
    print(f'Delay {amount} s')
    await asyncio.sleep(amount)


async def main():
    task1 = asyncio.create_task(delay(2.6))
    task2 = asyncio.create_task(delay(3.2))
    t0 = time.time()
    await task1
    await task2
    t1 = time.time()
    print(f'Overall took {t1 - t0:.4f} s')

asyncio.run(main())
# Delay 2.6 s
# Delay 3.2 s
# Overall took 3.2095 s
