/* Arduino Main File for EGEN 310 Group C1 Farmer2000
 * by Gage Hilyard
 * Completed 11/29/2021
 */

#include "Farmer.h"
#include <Servo.h>

int PWM1 = 3; //First two PWM pins
int DIR1 = 2; 
int PWM2 = 5; //Second two PWM pins
int DIR2 = 4;
int seedPin = 10;
int serialval = 9600;

Servo seed;
Motor rightMotor(PWM1, DIR1);
Motor leftMotor(PWM2, DIR2);
BTController cont(leftMotor, rightMotor, seed, serialval);

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(serialval);
  Serial.setTimeout(250);
  seed.attach(seedPin);
  //required to setup pinMode
  rightMotor.setupMotor();
  leftMotor.setupMotor();
  cont.setupCont(leftMotor, rightMotor, seed, serialval);
}

void loop() {
  cont.getString();
}
