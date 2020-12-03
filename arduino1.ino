int seq[8][4] = {{1, 0, 0, 0}, {1, 1, 0, 0}, {0, 1, 0, 0},
                 {0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 1, 1}, 
                 {0, 0, 0, 0}, {0, 0, 0, 0}};

int used_pin[4] = {2, 3, 4, 7};
int used_pin_2[4] = {8, 9, 12, 13};

int motorSpeed = 10;     //variable to set stepper speed

int seq_number = 0; // horizontal axis
int seq_number_2 = 0; // vertical axis

int h_degree;
int v_degree;

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
  pinMode(used_pin[0], OUTPUT); //motorPin1
  pinMode(used_pin[1], OUTPUT); //motorPin2
  pinMode(used_pin[2], OUTPUT); //motorPin3
  pinMode(used_pin[3], OUTPUT); //motorPin4
  
  pinMode(used_pin_2[0], OUTPUT); //motor2Pin1
  pinMode(used_pin_2[1], OUTPUT); //motor2Pin2
  pinMode(used_pin_2[2], OUTPUT); //motor2Pin3
  pinMode(used_pin_2[3], OUTPUT); //motor2Pin4
  
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
  if ( currentTime - lastReceiveTime > 1000 )
  {
    resetData();
  }
  checkEvent();
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):

  
 
  if(data.go_y<110)
  {
    int go = ((127-data.go_y)*2);
    if(data.go_x> 150){
        int turn = ((127-data.go_y)*2)-((data.go_x-128)*2);
        if(turn < 0){
          turn = 0;
        }
        analogWrite(3, go);
        analogWrite(9, turn);
        analogWrite(motorA, turn);
        analogWrite(motorB, go);
        analogWrite(motorA2, 0);
        analogWrite(motorB2, 0);
      }
    else if(data.go_x< 110){
        int turn2 = ((127-data.go_y)*2)-((127-data.go_x)*2);
        if(turn2 < 0){
          turn2 = 0;
        }
        analogWrite(3, turn2);
        analogWrite(9, go);
        analogWrite(motorA, go);
        analogWrite(motorB, turn2);
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
 else if(data.go_y>150)
 {
    int go2 = (data.go_y-128)*2;
    if(data.go_x > 150){
        int turn3 = ((data.go_y-128)*2)-(data.go_x-128)*2;
        if(turn3 < 0){
          turn3 = 0;
        }
        analogWrite(3, go2);
        analogWrite(9, turn3);
        analogWrite(motorA2, turn3);
        analogWrite(motorB2, go2);
        analogWrite(motorA, 0);
        analogWrite(motorB, 0);
      }
    else if(data.go_x<110){
        int turn4 = ((data.go_y-128)*2)-(127-data.go_x)*2;
        if(turn4 < 0){
          turn4 = 0;
        }
        analogWrite(3, turn4);
        analogWrite(9, go2);
        analogWrite(motorA2, go2);
        analogWrite(motorB2, turn4);
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

 // stepper motor for controlling orientation
  for(int i = 0; i <= 3; i++){
    digitalWrite(used_pin[i], seq[seq_number][i]);
  }
  
  for(int i = 0; i <= 3; i++){
    digitalWrite(used_pin_2[i], seq[seq_number_2][i]);
  }
  if(data.turn_y < 110 && h_degree < 1000){
    seq_number++;
    h_degree++;
  }
  if(data.turn_y > 150 && h_degree > -1000){
    seq_number--;
    h_degree--;
  }
  if(data.turn_x > 150 && v_degree < 1000){
    seq_number_2++;
    v_degree++;
  }
  if(data.turn_x < 110 && v_degree > -1000){
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
  delay(motorSpeed); 

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
  lastReceiveTime=millis();

}

void resetData()
{
  data={127,127,127,127,0,0,0,0};
  //Turn Off motors
//  digitalWrite(3,LOW);
//  digitalWrite(9,LOW);
  
}
