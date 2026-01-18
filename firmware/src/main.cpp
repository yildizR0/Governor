//USB to Servo Interface
//18.01.2026
//m.efeyildiz@icloud.com

#include <Arduino.h>
#include <Servo.h>

Servo main_governor;     
Servo side_governor; 

int HM = 5;
int NM = 6;

void setup()
{
  Serial.begin(115200);
  main_governor.attach(HM,1000,2000);
  side_governor.attach(NM,1000,2000);
}

void loop() {
  if (Serial.available()) {
    String serial = Serial.readStringUntil('\n');
    int commaIndex = serial.indexOf(',');
    if (commaIndex > 0) {
      int mainVal = serial.substring(0, commaIndex).toInt();
      int sideVal = serial.substring(commaIndex + 1).toInt();
      
      main_governor.writeMicroseconds(mainVal);
      side_governor.writeMicroseconds(sideVal);
    }
  }
}
