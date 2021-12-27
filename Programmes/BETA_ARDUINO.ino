/*
CODE BETA PAS ENCORE SUR
Nino Nicolas BMO Gestion capteur to raspberry via i2c
pont diviseur de tention de la batterie sur la pin A2
code = 101 (pont diviseur de tention batterie)
*/
 
// Library :
#include <Wire.h>

///////////////////////////////////////////////////////////////////////
//variables : 
char c;
int envoie;
const int PDT_Batterie = A2; 
int Pourcent_Batterie;
int Anal_Batterie;

/////////////////////////////////////////////////////////////////////// 
void setup() {
  // Demarage du bus i2c et serie
  Wire.begin(0x8);
  Serial.begin(9600);
  
  // Declaration variable d'interuptions               
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvents);
}
/////////////////////////////////////////////////////////////////////// 
// Fonction lors de la reception d'une info sur le bus i2c
void receiveEvent(int howMany) {
  while (Wire.available()) { // boucle jusqu'a que tout les infos soit traiter
    c = Wire.read(); // stock l'info i2c dans le variable char c
      
      if (c == 101){
        Serial.println("recu 2"); //affiche 2 quand il recois 2 sur le bus i2c
        envoie = 101;
      }
      else{
        Serial.println("autre");
      }
    c = 0;
  }
}
///////////////////////////////////////////////////////////////////////
// Fonction lors de lors d'une requette d'envoie d'info sur le bus i2c
void requestEvents()
{
  Serial.println("envoie");
  if(envoie = 101){
    Wire.write(Pourcent_Batterie);
    Serial.println("pourcent_batterie envoyer");
    envoie = 0;
  }
}
///////////////////////////////////////////////////////////////////////
void loop() {
  delay(500);
//////////////////////////////////////////////////////////////////////
  //prend la valeur analogique de la pinA2 et la remape de 0->1023 pour une valeur de 0->100
  //afin de faciliter la lecture du pourcentage
  Anal_Batterie = analogRead(PDT_Batterie);
  Pourcent_Batterie = map(Anal_Batterie,655, 865, 0, 100);
  //Serial.println(Pourcent_Batterie);

//////////////////////////////////////////////////////////////////////

}//fin loop
//////////////////////////////////////////////////////////////////////
