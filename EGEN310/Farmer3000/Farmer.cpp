/* cpp file for the Farmer2000
 * Gage Hilyard 11/18/2021
 */

#include "Farmer.h"
#include <Servo.h>

//Motor init
Motor::Motor() {
}

//Required to call in setup
void Motor::setupMotor(){
  pinMode(_PWM, OUTPUT);
  pinMode(_DIR, OUTPUT);
  int speed = 0;
}

//Shuts down motor
void Motor::killMotor(){
  digitalWrite(_PWM, LOW);
  digitalWrite(_DIR, LOW);
  delay(100);
}

//Sets speed forward or reverse
void Motor::setSpeed(int speed){
  //Puts motor in reverse
  if (speed < 0) {
    digitalWrite(9, HIGH);
    digitalWrite(_DIR, HIGH);
    analogWrite(_PWM, abs(speed));
  }
  //Puts motor in drive
  else if (speed > 0) {
    digitalWrite(_DIR, LOW);
    analogWrite(_PWM, speed);
  }
  else {
    killMotor();
  }
}

//BTController init
BTController::BTController() {
}

//Required to call in setup
void BTController::setupCont(Motor& in_m1, Motor& in_m2, Servo& in_ss, int in_serial) {
  //_m1 is right motor, _m2 is left motor
  _m1 = in_m1;
  _m2 = in_m2;
  _ss = in_ss;
  _serial = in_serial;
  _msgStr = '0';
}

//Gets char from Bluetooth Module
void BTController::getString() {
  if(Serial.available() > 0){
    _msgStr = Serial.read();
    Serial.print(_msgStr);
    Serial.print("\n");
    _ss.write(0);

    
    //Ch is "*" (Farmer Button ON) Displays Tractor
    while(_msgStr == '*') {
      Serial.println(_msgStr);
      // Get String
      int pos = 0;
      for(pos = 0; pos <= 150; pos +=1) {
        _m1.setSpeed(pos);
        _m2.setSpeed(pos);
        delay(10);
      }
      _m1.killMotor();
      _m2.killMotor();
      _ss.write(180);
      delay(2000);
      _ss.write(0);
      delay(1000);

      //checks for exit
      if(Serial.read() == '0'){
        _msgStr = Serial.read();
      }
    }

    //Ch is "f" (Forward Button held)
    if(_msgStr == 'f') {
      int pos = 0;
      for(pos = 0; pos <= 255; pos +=1) {
        _msgStr = Serial.read();
        if(_msgStr == '0') {
              _m1.killMotor();
              _m2.killMotor();
              _ss.write(0);
              break;     
            }
        _m1.setSpeed(pos);
        _m2.setSpeed(pos);
        delay(10);
      }
    }

    //String is "r" (Right Button held)
    if(_msgStr == 'r') {
      int pos = 0;
      for(pos = 0; pos <= 255; pos +=1) {
        _msgStr = Serial.read();
        if(_msgStr == '0') {
              _m1.killMotor();
              _m2.killMotor();
              _ss.write(0);
              break;    
            }
        _m1.setSpeed(-pos);
        _m2.setSpeed(pos);
        delay(10);
      }
    }
    //String is "b" (Back Button held)
    if(_msgStr == 'b') {
      int pos = 0;
      for(pos = 0; pos <= 255; pos +=1) {
        _msgStr = Serial.read();
        if(_msgStr == '0') {
              _m1.killMotor();
              _m2.killMotor();
              _ss.write(0);
              break;     
            }
        _m1.setSpeed(-pos);
        _m2.setSpeed(-pos);
        delay(10);
      }
    }
    //String is "l" (Left Button held)
    if(_msgStr == 'l') {
      int pos = 0;
      for(pos = 0; pos <= 255; pos +=1) {
        _msgStr = Serial.read();
        if(_msgStr == '0') {
          _m1.killMotor();
          _m2.killMotor();
          _ss.write(0);
          break;    
        }
        _m1.setSpeed(pos);
        _m2.setSpeed(-pos);
        delay(10);
      }
    }
    
    //String is "0" (Farmer Button OFF) Displays Farmer
    if(_msgStr == '0') {
      _m1.killMotor();
      _m2.killMotor();
      _ss.write(0);     
    }
  }
}
