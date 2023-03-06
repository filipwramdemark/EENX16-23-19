#include <ArduinoBLE.h>

BLEService SendData("64981768-2f1b-400e-8e75-e5a86c5434b8");
BLEFloatCharacteristic SendCharacteristic("64981768-2f1b-400e-8e75-e5a86c5434b8", BLERead | BLENotify);

void setup() {
  serial.Begin(9600);

  if(!BLE.Begin()){
    serial.println("BLE start failed");
  }

  BLE.setLocalName("Data sender");
  BLE.setAdvertisedService(BLEService);

  SendData.addCharacteristic(SendCharacteristic);

  BLE.addService(SendData);

  BLE.advertise();
  serial.println("Waiting for connection...");

}

void loop() {

  BLEDevice central = BLE.central();

  if(central){
    serial.println("Connected to central");
    serial.println(central.adress());
  }

  while(central.connected()){
    //Skriv kod för sensor data
    int temp = 1;

    //Skicka datan
    SendCharacteristics.writeValue(temp);
  }

  serial.println("Central disconnected");


}
