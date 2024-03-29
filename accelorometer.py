import asyncio
from bleak import BleakClient
from bleak import BleakScanner
import pandas as pd
import time


#ID för arduinons service
charachteristicID = '19B10021-E8F2-537E-4F6C-D104768A1214'
#charachteristicID1 = '19B10022-E8F2-537E-4F6C-D104768A1214'
#charachteristicID2 = '19B10023-E8F2-537E-4F6C-D104768A1214'
serviceID = "19B10020-E8F2-537E-4F6C-D104768A1214"

def temperatureCallback(handle, data):
  #Skriv ut temperaturvärdet i konsolen. Datan kommer som bytes så gör om de till int
#   print(float((int.from_bytes(data, byteorder='little', signed=True))))
    #print(data)
     #print(struct.unpack('<f', data))
    acc = int.from_bytes(data, byteorder='little', signed=True)/100
    df = pd.DataFrame(list(zip([acc], [time.time()])))

    df.to_csv('data/accData.csv', mode='a', index=False, header=False)
    
    # print(acc)

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
    
    
    await asyncio.sleep(30) # hur länge den kör.
    #Stoppa notify "servicen"
    await client.stop_notify(charachteristicID)




def getAccData():
  # clear the data file
  pd.DataFrame().to_csv("data/accData.csv", index=False, header=False)
  asyncio.run(main())