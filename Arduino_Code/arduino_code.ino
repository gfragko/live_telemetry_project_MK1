int analogPin = 3;     
int data = 0;           
char userInput;

void setup(){
  Serial.begin(9600);                        //  setup serial
}

void loop(){
    if(Serial.available()> 0){         // Check if there is data available to read from the serial port
        userInput = Serial.read();     // Read the character received from serial input
        
        if(userInput == 'g'){                  // if we get expected value ('g')
            data = analogRead(analogPin);      // Read the analog sensor connected to pin 3 and store the value in 'data'
            Serial.println(data);              // Send the sensor reading over serial communication               
        } 
    } 
} 