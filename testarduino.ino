#include <string.h>
#include "SerialTransfer.h"


SerialTransfer myTransfer;
unsigned long lastReceiveTime = 0;
unsigned long currentTime = 0;
int motorA = 9;
int motorB = 10;
struct data_package
{
  int go_x;
  int go_y ;
  int turn_x ;
  int turn_y ;
  bool square;
  bool x;
  bool o;
  bool triangle;   
};

data_package data;


void setup() 
{
  Serial.begin(9600);
  myTransfer.begin(Serial);
  Serial.println("Ready"); // print "Ready" once
  pinMode(9, OUTPUT);
  pinMode(10,OUTPUT);
  

}
void loop() 
{ 

  // Check whether we keep receving data, or we have a connection between the two modules
  currentTime = millis();
  checkEvent();
  if ( currentTime - lastReceiveTime > 1000 ) 
  { // If current time is more then 1 second since we have recived the last data, that means we have lost connection
    resetData(); // If connection is lost, reset the data.
  }
 
  
 if(data.go_x>=150 )
 {

  analogWrite(motorA, (data.go_x-150)*2);
  analogWrite(motorB, 0);
 }
 else if(data.go_x<110 )
 {
  analogWrite(motorA, 0);
  analogWrite(motorB, (110-data.go_x)*2);
 }
 else
 {
  analogWrite(motorA, 0);
  analogWrite(motorB, 0);

 }


    
  

}

void checkEvent()
{
    if(myTransfer.available())
  {
    myTransfer.rxObj(data);
    lastReceiveTime = millis();
  }

}

void resetData()
{
  data={127,127,127,127,false,false,false,false};
}
