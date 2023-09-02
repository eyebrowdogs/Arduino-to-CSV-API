

int buttonPin = D5; // Button
long duration, cm, inches;
int loopc = 0;
int bt;

 
void setup() {
  Serial.begin (9600);
  pinMode(buttonPin, INPUT);
}
 
void sender() {

   int cm = random(70);
  


  if (cm>= 50){
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
      bool state = digitalRead(buttonPin);
      bool debounced = debouncer(state);
      if (debounced==1)
      {
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
