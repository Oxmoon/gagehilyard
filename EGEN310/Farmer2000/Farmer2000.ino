/* Arduino Main File for EGEN 310 Group C1 Farmer2000
 * by Gage Hilyard
 */

#include "Farmer.h"

#define A1IN 3 //First two PWM pins
#define A2IN 5 
#define B1IN 6 //Second two PWM pins
#define B2IN 9
#define seedPin
#define rakePin

Motor leftMotor(A1IN, A2IN);
Motor rightMotor(B1IN, B2IN);

void setup() {
  
}

void loop() {

  leftMotor.setSpeed(255);
  delay(2000);
  leftMotor.setSpeed(-255);
  delay(2000);
  leftMotor.killMotor();

  rightMotor.setSpeed(255);
  delay(2000);
  rightMotor.setSpeed(-255);
  delay(2000);
  rightMotor.killMotor();
  
}
