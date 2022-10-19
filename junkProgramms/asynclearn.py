import asyncio

user=['user0','user1','user2']


async def getUser(pk):
    print(f'getting the user with the pk {pk}\n')
    return user[pk]
async def printnums():
    for i in range(30):
        print(f'printing 18 numbers {i}')
        await asyncio.sleep(0.5)

async def main():
    fetch_task=asyncio.create_task(getUser(1))#a task runs asynchronuasly
    print_task=asyncio.create_task(printnums())
    data=await fetch_task#we wait for the task to finish to return us the value returned by the routine
    await print_task
    print(f'the data is {data}')
asyncio.run(main())


### notes 
#we can play with the await inside the main routine (the event loop)
#which will enable us to wait for a routine to finish 
