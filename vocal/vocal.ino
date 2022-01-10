#include <SoftwareSerial.h>
#include "VoiceRecognitionV3.h"
VR myVR(2,3);
uint8_t buf[64];

#define onRecord    (0)
#define offRecord   (1)

void setup() { 
    myVR.begin(9600);
    Serial.begin(115200);

    if(myVR.clear() == 0){
      Serial.println("Recognizer cleared.");
    }
    else{
      Serial.println("Not find VoiceRecognitionModule.");
      Serial.println("Please check connection and restart Arduino.");
      while(1);
    }
    if(myVR.load((uint8_t)onRecord) >= 0){
      Serial.println("onRecord loaded");
    }
  
    if(myVR.load((uint8_t)offRecord) >= 0){
      Serial.println("offRecord loaded");
    }
}

void loop() {
  int ret;
  ret = myVR.recognize(buf, 50);
  if(ret>0){
      
    myVR.clear();
    myVR.load((uint8_t)1);
    myVR.load((uint8_t)6);
    myVR.load((uint8_t)69);

    if(buf[1] == 1){
        Serial.println("hey BMO");    
    }
    if(buf[1] == 6){
        Serial.println("SEIGNEUR SEVEN");    
    }
    if(buf[1] == 69){
        Serial.println("COCHON VA !");    
    }
  }
}