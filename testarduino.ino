
int incoming[8];

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
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
  pinMode(8, OUTPUT);
  

}
void loop() 
{
  checkEVENT();
 if(data.go_x>=128)
 {
  digitalWrite(8, HIGH);
 }
 else
 {
  digitalWrite(8, LOW);
 }
 
 delay(100);
}

void checkEVENT()
{
   if(Serial.available()>0)
  { // only send data back if data has been sent
//    digitalWrite(8, HIGH);
   for (int i = 0; i < 8; i++)
   {
    incoming[i] = Serial.read(); // read the incoming data
   }
   data={incoming[0],incoming[1],incoming[2],incoming[3],incoming[4],incoming[5],incoming[6],incoming[7]}; 
//   Serial.println(data.go_x);
   Serial.println(incoming[0]);
  }
  
  delay(10); // delay for 1/10 of a second
}
