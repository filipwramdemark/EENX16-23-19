import asyncio
import sys
from bleak import BleakClient
from bleak import BleakScanner

#ID för arduinons service
charachteristicID = '19B10001-E8F2-537E-4F6C-D104768A1214'
serviceID = "19B10000-E8F2-537E-4F6C-D104768A1214"



async def main():
  devices = await BleakScanner.discover()
  endProgram = 0
  for i in devices:
    #Leta upp vår enhet med namnet "TempData" och dess BLE adress
    if(i.name == "TempData"):
      address = i.address
      endProgram = 1
      print("Address:", address)
  
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

    tempData = await client.read_gatt_char(charachteristicID)
    #Skriv ut värdet på datan som advertisas av arduinon
    print("Temp data: ", int.from_bytes(tempData, byteorder='little'))
    #client.start_notify(charachteristicID, callback)


if __name__ == "__main__":
  asyncio.run(main())
