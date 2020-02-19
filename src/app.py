import asyncio
from src.tasks import netscan 
from src.helpers import mylogger
import http.client
import aiohttp
def start(shared_memory):
    # init root logger
    logger = mylogger.create_logger('my-app')
    logger.info("Secondery App Starts")
    loop =  asyncio.new_event_loop()
    async def connect():
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post("http://localhost:3000/connect", json={"a":"b"}) as response:
                        print(response.status)
                        print(await response.json())
            except Exception as inst:
                logger.error(inst.args)
                await asyncio.sleep(5)
    async def net_scan():
        while True:
            shared_memory["net_faces"]=netscan.run_faces()
            logger.info(shared_memory["net_faces"])
            await asyncio.sleep(60*5)

    async def counter():
        i=0
        while True:
            print(i)
            i+=1
            await asyncio.sleep(1)

    net_scan_task = loop.create_task(net_scan())
    counter = loop.create_task(counter())
    connection = loop.create_task(connect())
    loop.run_forever()
    #loop.run_until_complete(net_scan())