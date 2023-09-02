
int trigPin = 7;    // Trigger
int echoPin = 6;    // Echo
int buttonPin = 5; // Button
int redLed = 9;
int greenLed = 8;
long duration, cm, inches;
int loopc = 0;
int bt;

 
void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buttonPin, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(redLed,OUTPUT);
  pinMode(greenLed,OUTPUT);
  
}
 
bool sender() {
 
  digitalWrite(greenLed, HIGH);

  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  pinMode(echoPin, INPUT);
  float duration = pulseIn(echoPin, HIGH);
 
 
  float cm = (duration/2.0) / 29.1; 
  


  if (cm>= 50.0){
    Serial.print(loopc);
    Serial.print(",  ");
    Serial.println("NA");

  }
  else{
      Serial.print(loopc);
      Serial.print(", ");
      Serial.print(cm);     
      Serial.println();
  }
  
  loopc = loopc + 1;
  delay(10);
  digitalWrite(greenLed, LOW);
  
}


/* void loop(){
  while (digitalRead(buttonPin)== false)
  {
    delay(10);
  }
  Serial.print("begin");
  digitalWrite(LED_BUILTIN, HIGH);
  while (digitalRead(buttonPin)==0)
  {
    sender();
  }
  Serial.print("end");
  digitalWrite(LED_BUILTIN, LOW);



} */

bool debouncer(bool state){

  boolean stateNow = digitalRead(buttonPin);
  if (stateNow!=state)
  {
    delay(10);
    stateNow = digitalRead(buttonPin);
  }
  return stateNow;

}



void loop(){
      if (Serial.available() > 0) {
        char HHS = Serial.read();
        //Serial.println(HHS);
        if (HHS == 'a'){
          Serial.println('a');
      }
       }
      digitalWrite(redLed, HIGH);
      bool state = digitalRead(buttonPin);
      bool debounced = debouncer(state);
      if (debounced==1)
      { digitalWrite(redLed, LOW);
        Serial.println("begin");
        delay(250);
      Serial.print("No, ");
      Serial.print("cm");
      Serial.println();
        bt = true;
      }
      
      while ( bt == true)
      {
          sender();
          bool state = digitalRead(buttonPin);
          if (state == true)
          {
            bool debounced = debouncer(state);
          if (debounced==true)
          {
            Serial.println("end");
            loopc = 0;
            bt = false;
          }
          else{
            bt = true;
          }
          }
          
          
      }
      delay(250);
      
}
