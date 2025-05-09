// ====== SETUP ======
void setup() {
  Serial.begin(9600); 
}

// ====== MAIN LOOP ======
void loop() {
  // ====== READ SOIL MOISTURE SENSORS ======
  int soilMoisture1 = analogRead(A0); // Sensor 1
  int soilMoisture2 = analogRead(A1); // Sensor 2 (subsurface)
  int soilMoisture3 = analogRead(A2); // Sensor 3

  // ====== CHECK IF SENSORS ARE DISCONNECTED ======
  bool sensor1Connected = true;
  bool sensor2Connected = true;
  bool sensor3Connected = true;

  if (soilMoisture1 < 50 || soilMoisture1 > 1000) {
    sensor1Connected = false;
  }
  if (soilMoisture2 < 50 || soilMoisture2 > 1000) {
    sensor2Connected = false;
  }
  if (soilMoisture3 < 50 || soilMoisture3 > 1000) {
    sensor3Connected = false;
  }

  // ====== PRINT DATA AS JSON ======
  Serial.print("{");

  // Soil Moisture Sensor 1
  Serial.print("\"soil_moisture_1\":");
  if (sensor1Connected) {
    Serial.print(soilMoisture1);
  } else {
    Serial.print("\"disconnected\"");
  }

  Serial.print(",");

  // Subsurface Soil Moisture Sensor 2
  Serial.print("\"subsurface_soil_moisture_2\":");
  if (sensor2Connected) {
    Serial.print(soilMoisture2);
  } else {
    Serial.print("\"disconnected\"");
  }

  Serial.print(",");

  // Soil Moisture Sensor 3
  Serial.print("\"soil_moisture_3\":");
  if (sensor3Connected) {
    Serial.print(soilMoisture3);
  } else {
    Serial.print("\"disconnected\"");
  }

  Serial.println("}");

  // ====== WAIT BEFORE NEXT READING ======
  delay(5000); // Wait for 5 seconds
}
