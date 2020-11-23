#include <string.h>
#include "SerialTransfer.h"


SerialTransfer myTransfer;


struct data_package
{
  int go_x;
  int go_y ;
  int turn_x ;
  int turn_y ;
  int square;
  int x;
  int o;
  int triangle;   
};

data_package data;


void setup() 
{
  Serial.begin(9600);
  myTransfer.begin(Serial);
  Serial.println("Ready"); // print "Ready" once
  pinMode(8, OUTPUT);
  pinMode(9,OUTPUT);
  

}
void loop() 
{
  checkEvent();
  
 if(data.go_x>=150 )
 {

  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
 }
 else if(data.go_x<100 )
 {
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
 }
 else
 {
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);

 }
 
 delay(100);
}

void checkEvent()
{
    if(myTransfer.available())
  {
    myTransfer.rxObj(data);
  }
}
