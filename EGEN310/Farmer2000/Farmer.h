/* Header file for the Farmer library
 * Gage Hilyard, 11/18/2021
 */

#ifndef Farmer_h
#define Farmer_h

#include "Arduino.h"


//Class used to control individual motors through the H bridge motor driver
class Motor {
  public:
  //Variables
  int speed; //negative speed = reverse/counterclockwise
  
  //Constructor
  Motor(int in1, int in2);

  //Methods
  void killMotor();  //disable motorPins
  void setSpeed(int speed); //takes -255 - 255, changes PWM pin voltage

  private:
  int _pin1;
  int _pin2;
  
  
};

//Class to get strings from Bluetooth Controller
class BTController {
  public:
  //variables

  //Constructor
  BTController();

  //Methods
  String getString();
  

  private:
  //Possibly pins? serial?
  String _msgStr;
  int serial;
  
};

class MiniServo {
  public:
  //Variables
  int angle;

  //Constructor
  MiniServo(int in, int in_angle);

  //Methods
  void setAngle(int angle);

  private:
  int _pin;
};

#endif
