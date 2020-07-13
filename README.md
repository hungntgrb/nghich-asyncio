# AsyncIO module

> Nguyen Thanh Hung - here I share what I learned.

## Create a coroutine

```python
async def hi(name):
    print(f'Hi {name}!')

# Call the function only create a coroutine object, not execute.
corou = hi('Hung')
print(corou)
# <coroutine object hi at 0x00001DF6BA2AE40>
```

To execute:

```python
# 'run' that coroutine
asyncio.run(hi('Hung'))
```

## To run coroutines concurrently

### you have to `gather()` to create a future. `await` a future runs corous in order.

```python
async def main():
    await asyncio.gather(hi('Superman'), hi('Batman'))

asyncio.run(main())
# Remember to pass a corou in by calling the func.
```

### or `await` the tasks

```python
async def main2():
    task1 = asyncio.create_task(hi('Hung'))
    task2 = asyncio.create_task(hi('Alice'))
    await task1
    await task2

asyncio.run(main2())
# Simple as that! :)
```
