import asyncio
import sys
from bleak import BleakClient
from bleak import BleakScanner
import struct
import pandas as pd

#ID för arduinons service
tempSNOW_ID = '19B10001-E8F2-537E-4F6C-D104768A1214'
tempAIR_ID = '19B10002-E8F2-537E-4F6C-D104768A1214'
serviceID = "19B10000-E8F2-537E-4F6C-D104768A1214"
FILENAME = "tempAndHum.csv"

def tempAIRCallback(handle, data):
  print("Air temperature: ", int.from_bytes(data, byteorder='little', signed=True))

def tempSNOWCallback(handle, data):
  #Skriv ut temperaturvärdet i konsolen. Datan kommer som bytes så gör om de till int
  #print(int.from_bytes(data, byteorder="big", signed=True))
  data = struct.unpack('d', data)[0]
  tempAndHum_df = pd.DataFrame([data])
  print(data)

  tempAndHum_df.to_csv(FILENAME, mode="a", index=False, header=False)
  #Data kommer i ordningen: snötemperatur, snöfuktighet, lufttemperatur, luftfuktighet

  if(data == 1000):
    file = open(FILENAME, "w")
    file.truncate()
    file.close()

async def main():
  devices = await BleakScanner.discover()
  endProgram = 0
  for i in devices:
    #Leta upp vår enhet med namnet "TempData" och dess BLE adress
    if(i.name == "TempAndHumData"):
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

    await client.start_notify(tempSNOW_ID, tempSNOWCallback)
    #await client.start_notify(tempAIR_ID, tempAIRCallback)
    #Sleep i x antal ms
    await asyncio.sleep(5)

def getData():
  asyncio.run(main())
