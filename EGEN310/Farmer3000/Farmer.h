/* Header file for the Farmer library
 * Gage Hilyard, 11/18/2021
 */

#ifndef Farmer_h
#define Farmer_h

#include "Arduino.h"
#include <Servo.h>


//Class used to control individual motors through the H bridge motor driver
class Motor {
  public:
  //Variables
  int speed; //negative speed = reverse/counterclockwise
  
  //Constructor
  Motor(int in1, int in2){_PWM = in1; _DIR = in2;} //in1 is PWM, in2 is DIR
  Motor(const Motor &m1){_PWM = m1._PWM; _DIR= m1._DIR;}
  Motor();

  //Methods
  void killMotor();  //disable motorPins
  void setupMotor();
  void setSpeed(int speed); //takes -255 - 255, changes PWM pin voltage

  private:
  int _PWM;
  int _DIR;
  
  
};

//Class used to control motors and recieve strings from iOS
class BTController {
  public:
  //variables

  //Constructor
  BTController(Motor& in_m1, Motor& in_m2, Servo& in_ss, int in_serial){_m1 = in_m1; _m2 = in_m2; _ss = in_ss; _serial = in_serial;}
  BTController(const BTController &b1){_m1 = b1._m1; _m2 = b1._m2; _ss = b1._ss; _serial = b1._serial;}
  BTController();

  //Methods
  void setupCont(Motor& _m1, Motor& _m2, Servo& _ss, int _serial);
  void getString();
  

  private:
  Motor _m1;
  Motor _m2;
  Servo _ss;
  char _msgStr;
  int _serial;
  
};

#endif
