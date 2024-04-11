int analogPin = 3;     
int data = 0;           
char userInput;

void setup(){
  Serial.begin(115200);                        //  setup serial
}

void loop(){
    float time = micros() / 1e6;
    int sensorVal1= analogRead(A0);
    int sensorVal2= analogRead(A1);
    delay(100);

    Serial.print(time);
    Serial.print(", ");
    Serial.print(sensorVal1);
    Serial.print(", ");
    Serial.print(sensorVal2);
} 