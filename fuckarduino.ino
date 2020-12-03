unsigned long lastReceiveTime = 0;
unsigned long currentTime = 0;
int motorA = 5;
int motorA2 = 6;
int motorB = 10;
int motorB2 = 11;


struct data_package
{
  int go_x; //Right and left control
  int go_y ; //Forward and backward control
  int turn_x ; //Camera Control right and left
  int turn_y ; //Camera Control up and down
  int square;
  int x;
  int o;
  int triangle;   
};

int incoming[8];
data_package data;

void setup() 
{
  Serial.begin(9600);
  Serial.println("Ready"); // print "Ready" once
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(motorA, OUTPUT);
  pinMode(motorA2,OUTPUT);
  pinMode(motorB, OUTPUT);
  pinMode(motorB2,OUTPUT);
  resetData();
  
}



void loop() 
{ 
  
   //Check whether we keep receving data, or we have a connection between the two modules
  currentTime = millis();
  if(currentTime-lastReceiveTime>1000)
  {
    resetData();
  }
  
  checkEvent();
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):

  
 
  if(data.go_y>=150)
  {
    int go = ((data.go_y-128)*2);
    if(data.go_x> 150){
        int turn = ((data.go_y-128)*2)-((data.go_x-128)*2);
        if(turn < 0){
          turn = 0;
        }
        analogWrite(3, go);
        analogWrite(9, turn);
        analogWrite(motorA, go);
        analogWrite(motorB, turn);
        analogWrite(motorA2, 0);
        analogWrite(motorB2, 0);
      }
    else if(data.go_x< 110){
        int turn2 = ((data.go_y-128)*2)-((127-data.go_x)*2);
        if(turn2 < 0){
          turn2 = 0;
        }
        analogWrite(3, turn2);
        analogWrite(9, go);
        analogWrite(motorA, turn2);
        analogWrite(motorB, go);
        analogWrite(motorA2, 0);
        analogWrite(motorB2, 0);
      }
    else{
        analogWrite(3, go);
        analogWrite(9, go);
        analogWrite(motorA, go);
        analogWrite(motorB, go);
        analogWrite(motorA2, 0);
        analogWrite(motorB2, 0);
      }
   }
 else if(data.go_y<110 )
 {
    int go2 = (127-data.go_y)*2;
    if(data.go_x > 150){
        int turn3 = ((127-data.go_y)*2)-(data.go_x-128)*2;
        if(turn3 < 0){
          turn3 = 0;
        }
        analogWrite(3, go2);
        analogWrite(9, turn3);
        analogWrite(motorA2, go2);
        analogWrite(motorB2, turn3);
        analogWrite(motorA, 0);
        analogWrite(motorB, 0);
      }
    else if(data.go_x<110){
        int turn4 = ((127-data.go_y)*2)-(127-data.go_x)*2;
        if(turn4 < 0){
          turn4 = 0;
        }
        analogWrite(3, turn4);
        analogWrite(9, go2);
        analogWrite(motorA2, turn4);
        analogWrite(motorB2, go2);
        analogWrite(motorA, 0);
        analogWrite(motorB, 0); 
        }
    else{
        analogWrite(3, go2);
        analogWrite(9, go2);
        analogWrite(motorA2, go2);
        analogWrite(motorB2, go2);
        analogWrite(motorA, 0);
        analogWrite(motorB, 0);
    }
 }

 else
 {
    analogWrite(3, 0);
    analogWrite(9, 0);
    analogWrite(motorA, 0);
    analogWrite(motorB, 0);
    analogWrite(motorA2, 0);
    analogWrite(motorB2, 0);
 }
 


    
  

}

void checkEvent()
{
    while(Serial.available()>=8)
  {
    
    for (int i = 0; i < 8; i++)
    {
      incoming[i] = Serial.read();
    }
    
    data={incoming[0],incoming[1],incoming[2],incoming[3],incoming[4],incoming[5],incoming[6],incoming[7]};
    
  }
  lastReceiveTime = millis();
  

}

void resetData()
{
  data={127,127,127,127,0,0,0,0};
  //Turn Off motors
//  digitalWrite(3,LOW);
//  digitalWrite(9,LOW);
  
}
