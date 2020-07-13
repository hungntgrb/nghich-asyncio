import asyncio
import time

# Create a coroutine


async def hi(name):
    print(f'Hi {name}!')

# Call the function only create a coroutine object, not execute.
# print(hi('Hung'))
# <coroutine object hi at 0x000001DX8BA2JE40>
# To execute, do this:

# asyncio.run(hi('Hung'))

# Another coroutine


async def hello(name: str, delay: float) -> None:
    """Print 'Hello' then delay for x seconds"""
    print(f'Hello {name}!')
    await asyncio.sleep(delay)

# Main function


async def main():
    """Await one func at a time only make sure they run in order.
    Expected 5s.
    """
    print(f"Start at {time.strftime('%X')}")
    await hello('Hung', 2)
    await hello('Long', 3)
    print(f"Finish at {time.strftime('%X')}")

asyncio.run(main())
"""
Start at 23:27:59
Hello Hung!
Hello Long!
Finish at 23:28:04 --> 5s
"""


async def main2():
    """Await a Gathering will run the coroutines concurrently."""
    print(f"Start at {time.strftime('%X')}")
    await asyncio.gather(
        hello('Hung', 2),
        hello('Hung', 3)
    )
    print(f"Finish at {time.strftime('%X')}")

asyncio.run(main2())
"""Start at 23:32:50
Hello Hung!
Hello Hung!
Finish at 23:32:53 --> ~3s
"""
