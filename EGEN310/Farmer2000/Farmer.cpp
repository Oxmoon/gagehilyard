/* cpp file for the Farmer2000
 * Gage Hilyard 11/18/2021
 */

#include "Farmer.h"

//Motor init
Motor::Motor(int in1, int in2) {
  _pin1 = in1;
  _pin2 = in2;
  pinMode(_pin1, OUTPUT);
  pinMode(_pin2, OUTPUT);
  digitalWrite(_pin1, LOW);
  digitalWrite(_pin2, LOW);
  
  int speed = 0;
}

void Motor::killMotor(){
  digitalWrite(_pin1, LOW);
  digitalWrite(_pin2, LOW);
}

void Motor::setSpeed(int speed){
  //Puts motor in reverse
  if (speed < 0) {
    analogWrite(_pin1, abs(speed));
    digitalWrite(_pin2, LOW);
  }
  //Puts motor in drive
  else if (speed > 0) {
    digitalWrite(_pin1, LOW);
    analogWrite(_pin2, speed);
  }
  else {
    killMotor();
  }
}

//MiniServo init
MiniServo::MiniServo(int in, int in_angle) {
  _pin = in;
  angle = in_angle;
  pinMode(_pin, OUTPUT);
  digitalWrite(_pin, angle);
}

void MiniServo::setAngle(int in_angle) {
  digitalWrite(_pin, angle);
}
