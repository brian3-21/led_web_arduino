int LED8 = 8;
char data;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED8, OUTPUT);
  Serial.begin(9600);


}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    data = Serial.read();
    if(data == 'P'){
      digitalWrite(LED8,HIGH);
    }
    if(data == 'N'){
      digitalWrite(LED8,LOW);
    }
  }
  

}
