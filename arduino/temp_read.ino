/*
  HS300x - Read Sensors

  Reads from the Temperature, Humidity
*/

#include <Arduino_HS300x.h>
#include <Arduino_LPS22HB.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!HS300x.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }
}

void loop() {
  // read all the temperature sensor values
  float temperature = HS300x.readTemperature();
  // output values, comma seperatad
  Serial.print(temperature);

  delay(1000);
}
