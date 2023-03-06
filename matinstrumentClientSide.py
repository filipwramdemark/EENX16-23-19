import asyncio
import sys
from bleak import BleakClient
from bleak import BleakScanner

#ID för arduinons service
charachteristicID = '19B10001-E8F2-537E-4F6C-D104768A1214'
serviceID = "19B10000-E8F2-537E-4F6C-D104768A1214"

def temperatureCallback(handle, data):
  #Skriv ut temperaturvärdet i konsolen. Datan kommer som bytes så gör om de till int
  print(int.from_bytes(data, byteorder='little', signed=True))

async def main():
  devices = await BleakScanner.discover()
  endProgram = 0
  for i in devices:
    #Leta upp vår enhet med namnet "TempData" och dess BLE adress
    if(i.name == "TempData"):
      address = i.address
      endProgram = 1
      print("Address:", address)
      print("Name:", i.name)
  
  #Avslutar program ifall enheten ej finnes
  if(endProgram == 0):
    print("Enheten hittas ej. Avlsutar program")
    exit()

  
  async with BleakClient(address) as client:
    if (not client.is_connected):
      raise "Client not connected"

    for i in client.services:
      if(i.uuid == serviceID.lower()):
        print("Service ID found!")

    await client.start_notify(charachteristicID, temperatureCallback)
    #Sleep i 3s
    await asyncio.sleep(10)
    #Stoppa notify "servicen"
    await client.stop_notify(charachteristicID)


asyncio.run(main())
