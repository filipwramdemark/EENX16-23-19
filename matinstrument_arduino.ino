#include <ArduinoBLE.h>
#include <dhtnew.h>

//BLE variables
BLEService SendData("19B10000-E8F2-537E-4F6C-D104768A1214");
BLEDoubleCharacteristic tempAndHum("19B10001-E8F2-537E-4F6C-D104768A1214", BLERead | BLENotify);

//Temperature variables
const int PT1000_SNOW = 0;
const int PT1000_AIR = 1;
const float vt_factor = 3.05;
const float offset_SNOW = -24;
const float offset_AIR = -31;
float temp_SNOW;
float temp_AIR;

//Humidity variables
DHTNEW airHumidity(11); //Connected to digital pin 11
DHTNEW snowHumidity(12);

void setup() {
  //Start serial monitor
  Serial.begin(9600);

  //Humidity sensor setup
  Serial.println("Before offset");
  delay(2000);
  airHumidity.read();
  snowHumidity.read();
  Serial.print("Air RH: "); Serial.print(airHumidity.getHumidity(), 1); Serial.println("%");
  Serial.print("Snow RH: "); Serial.print(snowHumidity.getHumidity(), 1); Serial.println("%");
  //Set potential offsets to calibrate
  airHumidity.setHumOffset(0);
  snowHumidity.setHumOffset(0);
  Serial.println("After offset");

  //BLUETOOTH SETUP
  if(!BLE.begin()){
    Serial.println("BLE start failed");
  }

  BLE.setLocalName("TempAndHumData");
  BLE.setAdvertisedService(SendData);
  //BLE.setAdvertisedService(SendData2);

  SendData.addCharacteristic(tempAndHum);
  //SendData2.addCharacteristic(tempAIR);

  BLE.addService(SendData);
  //BLE.addService(SendData2);

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
    //Temperature
    //SNOW calcs
    int sensorValSnow = analogRead(PT1000_SNOW);
    float voltageSnow = sensorValSnow * (5.0 / 1023.0);
    temp_SNOW = (((voltageSnow * 100) / vt_factor) + offset_SNOW);
    //AIR calcs
    int sensorValAir = analogRead(PT1000_AIR);
    float voltageAir = sensorValAir * (5.0 / 1023.0);
    temp_AIR = (((voltageAir * 100) / vt_factor) + offset_AIR);

    //Humidity
    if(millis() - airHumidity.lastRead() > 2000){ //Read new value if 2s has passed
      airHumidity.read();
      snowHumidity.read();
    }
    tempAndHum.writeValue(1000);
    tempAndHum.writeValue(temp_AIR);
    tempAndHum.writeValue(airHumidity.getHumidity());
    tempAndHum.writeValue(temp_SNOW);
    tempAndHum.writeValue(snowHumidity.getHumidity());

    //Loopa igenom varje variabel och advertisa dem en åt gången?
    
    delay(500);
  }
    //Temperature
    //SNOW calcs
    int sensorValSnow = analogRead(PT1000_SNOW);
    float voltageSnow = sensorValSnow * (5.0 / 1023.0);
    temp_SNOW = (((voltageSnow * 100) / vt_factor) + offset_SNOW);
    //AIR calcs
    int sensorValAir = analogRead(PT1000_AIR);
    float voltageAir = sensorValAir * (5.0 / 1023.0);
    temp_AIR = (((voltageAir * 100) / vt_factor) + offset_AIR);
    //Send the data
    Serial.print("SNOW: ");
    Serial.println(temp_SNOW);
    Serial.print("AIR: ");
    Serial.println(temp_AIR);

    if(millis() - airHumidity.lastRead() > 2000){
      airHumidity.read();
      snowHumidity.read();

      Serial.print("Air RH: "); Serial.print(airHumidity.getHumidity(), 1); Serial.println("%");
      Serial.print("Snow RH: "); Serial.print(snowHumidity.getHumidity(), 1); Serial.println("%");

    }
    delay(1000);

  //Serial.println("Central disconnected");


}
