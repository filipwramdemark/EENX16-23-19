

#include <ArduinoBLE.h>
#include <Arduino_LSM6DSOX.h>
float x, y, z;
BLEService SendData("19B10020-E8F2-537E-4F6C-D104768A1214");
BLEIntCharacteristic SendCharacteristic("19B10021-E8F2-537E-4F6C-D104768A1214", BLERead | BLENotify);
//BLEIntCharacteristic SendCharacteristicY("19B10022-E8F2-537E-4F6C-D104768A1214", BLERead | BLENotify);
//BLEIntCharacteristic SendCharacteristicZ("19B10023-E8F2-537E-4F6C-D104768A1214", BLERead | BLENotify);

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
  //SendData.addCharacteristic(SendCharacteristicY);
  //SendData.addCharacteristic(SendCharacteristicZ);


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
      // Calibrate the IMU
      

      // Set acceleration offset
      //float x_offset = 0.1;
      //float y_offset = 0.2;
      //float z_offset = 0.3;
      //IMU.setAccOffset(x_offset, y_offset, z_offset);


      if (IMU.accelerationAvailable()) {
        IMU.readAcceleration(x,y,z);
        
        //Serial.println(x, y, z)
      //Skicka datan
        //SendCharacteristic.writeValue(x, y, z);
        SendCharacteristic.writeValue(x*100);
        SendCharacteristic.writeValue(y*100);
        SendCharacteristic.writeValue(z*100);
    }

    
  }

  Serial.println("Central disconnected");


}