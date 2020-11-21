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


void setup() {

  //declare the motor pins as outputs

  pinMode(3, OUTPUT); //motorPin1
  pinMode(4, OUTPUT); //motorPin2
  pinMode(5, OUTPUT); //motorPin3
  pinMode(6, OUTPUT); //motorPin4
  
  pinMode(8, OUTPUT); //motor2Pin1
  pinMode(9, OUTPUT); //motor2Pin2
  pinMode(10, OUTPUT); //motor2Pin3
  pinMode(11, OUTPUT); //motor2Pin4

  Serial.begin(9600);

}


void loop(){
  if(Serial.available() > 0){
  char input = Serial.read();
      if(input == 'r'){
    right = true;
    left = false;
  }
  else if(input == 'l'){
    left = true;
    right = false;
  }
  else if(input == 'u'){
    up = true;
    down = false;
  }
  else if(input == 'd'){
    down = true;
    up = false;
  }
  else if(input == '0'){
    right = false;
    left = false;
    up = false;
    down = false;
  } 
  
  }
  for(int i = 0; i <= 3; i++){
    digitalWrite(i+3, seq[seq_number][i]);
  }
  
  for(int i = 0; i <= 3; i++){
    digitalWrite(i+8, seq[seq_number_2][i]);
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
  delay(motorSpeed);
}
