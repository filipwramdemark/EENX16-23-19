#include <ArduinoBLE.h>

BLEService SendData("64981768-2f1b-400e-8e75-e5a86c5434b8");
BLEFloatCharacteristic SendCharacteristic("64981768-2f1b-400e-8e75-e5a86c5434b8", BLERead | BLENotify);

void setup() {
  Serial.begin(9600);

  if(!BLE.begin()){
    Serial.println("BLE start failed");
  }

  BLE.setLocalName("Data sender");
  BLE.setAdvertisedService(SendData);

  SendData.addCharacteristic(SendCharacteristic);

  BLE.addService(SendData);

  BLE.advertise();
  Serial.println("Waiting for connection...");

}

void loop() {

  BLEDevice central = BLE.central();

  if(central){
    Serial.println("Connected to central");
    Serial.println(central.address());
  }

  while(central.connected()){
    //Skriv kod för sensor data
    int temp = 1;

    //Skicka datan
    SendCharacteristic.writeValue(temp);
  }

  Serial.println("Central disconnected");


}
