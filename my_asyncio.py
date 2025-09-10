import asyncio


async def hello_world():
    print("Hello")
    await asyncio.sleep(2)
    print("World!")


async def square(x):
    await asyncio.sleep(1)
    print(x**2)


async def main():
    await asyncio.gather(
        hello_world(),
        square(8),
    )


asyncio.run(main())

input("Hit ENTER to exit")
