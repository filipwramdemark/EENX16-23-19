const int PT1000_PIN = 0;
const float vt_factor = 3.05;
const float offset = -20.8;

float temp_c;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorvalue = analogRead(PT1000_PIN);
  float voltage = sensorvalue * (5.0 / 1023.0);
  temp_c = (((voltage * 100) / vt_factor) + offset);
  Serial.print(voltage);
  Serial.print(" V Temp: ");
  Serial.println(temp_c, 1);
  delay(500);
}


//0.63V vid 1000ohm
//3.68 vid 1385ohm
//3.68 - 0.63 = 3.05
