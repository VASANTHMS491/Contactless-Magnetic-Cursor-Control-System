int pins[5] = {32, 33, 25, 26, 27};

void setup() {
  Serial.begin(115200);
  analogSetAttenuation(ADC_11db);
}

// 0.2 sec averaging
int readAverage(int pin) {
  long sum = 0;
  int count = 0;

  unsigned long start = millis();
  while (millis() - start < 200) {
    sum += analogRead(pin);
    count++;
    delay(2);
  }

  return sum / count;
}

void loop() {

  for (int i = 0; i < 5; i++) {

    int val = readAverage(pins[i]);

    // 👉 Print GPIO39 values always
    if (pins[i] == 39) {
      Serial.print("GPIO 39 VALUE: ");
      Serial.println(val);
    }

    // 👉 Your original condition
    if (val == 0) {
      Serial.print("MAGNET DETECTED on GPIO ");
      Serial.println(pins[i]);
    }
  }

  delay(200);
}
