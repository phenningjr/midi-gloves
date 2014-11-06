// Music Bender Gloves v1
//#include <stdio.h>

// PIN SETUP
#define SENSOR1 A3
//#define SENSOR2 A1
//#define SENSOR3 A2
//#define SENSOR4 A3
//#define SENSOR5 A4

#define BUZZER 9

#define SLIDER A0

#define FLEXTHRESHOLD 370


// F: SETUP
// Setup function initializes the pin modes and other variables.

void setup()
{
  pinMode(SENSOR1, INPUT);

  pinMode(BUZZER,OUTPUT);
  
  Serial.begin(9600);
  
}


// F: LOOP
// Main code functioning: calls the other necessary functions and such.
void loop()
{
  
  int flexSensor1 = analogRead(SENSOR1);
  
  if (flexSensor1 < FLEXTHRESHOLD)
    tone(BUZZER, 480);
  else
    noTone(BUZZER);
  
  Serial.println(flexSensor1);
 
  delay(150);
}


