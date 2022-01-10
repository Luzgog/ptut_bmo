#include <SoftwareSerial.h>
#include "VoiceRecognitionV3.h"

VR myVR(2,3);
uint8_t buf[64];
int ret;
bool menu;

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
  menu = HIGH;
  ret = myVR.recognize(buf, 50);
  if(ret>0){

    myVR.clear();
    myVR.load((uint8_t)1);//hey BMO

    if(buf[1] == 1){
        buf[1] = 0;
        delay(500);
        Serial.println("MENU");
        
        myVR.clear();
        myVR.load((uint8_t)5);//shutdown
        myVR.load((uint8_t)6);//test
        myVR.load((uint8_t)7);
        myVR.load((uint8_t)8);
        myVR.load((uint8_t)9);//mode
        myVR.load((uint8_t)10);//paramètre
        
        while(menu == HIGH){
          myVR.recognize(buf, 50);
          
          if(buf[1] == 5){
              Serial.println("Shutdown");
              menu = LOW;
          }
          if(buf[1] == 6){
              Serial.println("Simon");
              menu = LOW;
          }
          if(buf[1] == 9){
              Serial.println("Mode");
              menu = LOW;
          }        
          if(buf[1] == 10){
              Serial.println("Paramètre");
              menu = LOW;
          }

        }
      }
   }
}