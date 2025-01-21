import asyncio

async def birinci_fonk():
    print('birinci fonksiyon çalıştı')
    await asyncio.sleep(5)
    print('birinci fonksiyon bitti')
    return 5

async def ikinci_fonk():
    print('ikinci fonksiyon çalıştı')
    await asyncio.sleep(5)
    print('ikinci fonksiyon bitti')
    return 10


async def main():

    task1 = asyncio.create_task(birinci_fonk())
    task2 = asyncio.create_task(ikinci_fonk())

    x = await task1
    y = await task2

    print(x)
    print(y)

if __name__ == '__main__':
    asyncio.run(main())


