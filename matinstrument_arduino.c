#include <ArduinoBLE.h>
#include <Arduino_LSM6DSOX.h>

BLEService SendData("19B10000-E8F2-537E-4F6C-D104768A1214");
BLEIntCharacteristic SendCharacteristic("19B10001-E8F2-537E-4F6C-D104768A1214", BLERead | BLENotify);

void setup() {
  Serial.begin(9600);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
  }

  if(!BLE.begin()){
    Serial.println("BLE start failed");
  }

  BLE.setLocalName("TempData");
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
    //int temp = 43;
    int temp = 0;

    if(IMU.temperatureAvailable()){
      IMU.readTemperature(temp);
      Serial.println(temp);
      //Skicka datan
      SendCharacteristic.writeValue(temp);
    }

    
  }

  Serial.println("Central disconnected");


}
