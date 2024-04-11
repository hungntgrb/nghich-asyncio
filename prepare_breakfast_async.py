from time import perf_counter
import asyncio


async def brewCoffee():
    print('Start brewCoffee()')
    await asyncio.sleep(3)
    print('  Stop brewCoffee()')
    return '\tCoffee done!'


async def toastBread():
    print('Start toastBread()')
    await asyncio.sleep(2)
    print('  Stop toastBread()')
    return '\tBread done!'


async def fryEggsAndHam():
    print('Start fryEggsAndHam()')
    await asyncio.sleep(4)
    print('  Stop fryEggsAndHam()')
    return '\tEggs and Ham done!'


async def main_gather():
    t1 = perf_counter()

    batch = asyncio.gather(brewCoffee(), toastBread(), fryEggsAndHam())
    coffee_result, bread_result, eggs_ham_result = await batch

    t2 = perf_counter()

    print(coffee_result)
    print(bread_result)
    print(eggs_ham_result)
    print(f'It took {t2 - t1:.2f} seconds!')


async def main_create_tasks():
    t1 = perf_counter()

    coffee_task = asyncio.create_task(brewCoffee())
    bread_task = asyncio.create_task(toastBread())
    eggs_ham_task = asyncio.create_task(fryEggsAndHam())

    coffee_result = await coffee_task
    print(coffee_result)
    bread_result = await bread_task
    print(bread_result)
    eggs_ham_result = await eggs_ham_task
    print(eggs_ham_result)

    t2 = perf_counter()

    print(f'It took {t2 - t1:.2f} seconds!')


if __name__ == '__main__':
    asyncio.run(main_create_tasks())
    # asyncio.run(main_gather())
