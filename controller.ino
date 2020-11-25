#include <string.h>
#include <SerialTransfer.h>


SerialTransfer myTransfer;
unsigned long lastReceiveTime = 0;
unsigned long currentTime = 0;
int motorA = 5;
int motorA2 = 4;
int motorB = 3;
int motorB2 = 2;
int seq[8][4] = {{1, 0, 0, 0}, {1, 1, 0, 0}, {0, 1, 0, 0},
                 {0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 1, 1}, 
                 {0, 0, 0, 0}, {0, 0, 0, 0}};          
int motorSpeed = 10;     //variable to set stepper speed

int seq_number = 0; // horizontal axis
int seq_number_2 = 0; // vertical axis

int h_degree;
int v_degree;

bool left = false;
bool right = false;
bool up = false;
bool down = false;
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
  pinMode(5, OUTPUT);
  pinMode(3,OUTPUT);
  
  pinMode(6, OUTPUT); //motorPin1
  pinMode(7, OUTPUT); //motorPin2
  pinMode(8, OUTPUT); //motorPin3
  pinMode(9, OUTPUT); //motorPin4
  
  pinMode(10, OUTPUT); //motor2Pin1
  pinMode(11, OUTPUT); //motor2Pin2
  pinMode(12, OUTPUT); //motor2Pin3
  pinMode(13, OUTPUT); //motor2Pin4

  

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
  if(data.turn_x>=150){
    right = true;
    left = false;
  }
  else if(data.turn_x<110){
    left = true;
    right = false;
  }
  else if(data.turn_y>=150){
    up = true;
    down = false;
  }
  else if(data.turn_y<110){
    down = true;
    up = false;
  }
  else{
    right = false;
    left = false;
    up = false;
    down = false;
  } 
  
  
  for(int i = 0; i <= 3; i++){
    digitalWrite(i+6, seq[seq_number][i]);
  }
  
  for(int i = 0; i <= 3; i++){
    digitalWrite(i+10, seq[seq_number_2][i]);
  }
  
  if(right == true && h_degree < 128){
    seq_number++;
    h_degree++;
  }
  if(left == true && h_degree > -128){
    seq_number--;
    h_degree--;
  }
  if(up == true && v_degree < 128){
    seq_number_2++;
    v_degree++;
  }
  if(down == true && v_degree > -128){
    seq_number_2--;
    v_degree--;
  }
  
  if (seq_number > 7){
    seq_number = 0;
  }
  if (seq_number < 0){
    seq_number = 7;
  }
  if (seq_number_2 > 7){
    seq_number_2 = 0;
  }
  if (seq_number_2 < 0){
    seq_number_2 = 7;
  }
  Serial.print("v_degree ");
  Serial.print(v_degree);
  Serial.print(" h_degree ");
  Serial.println(h_degree);
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
