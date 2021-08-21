#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
int salida = 2;


void setup() {
  

  pinMode(salida,OUTPUT);
  // Asignacion de los pines analogicos a cada uno de los servos

  servo1.attach(A4); // Pin analogico para el dedo pulgar  ---> 'P'
  servo2.attach(A3); // Pin analogico para el dedo indice  ---> 'I'
  servo3.attach(A2); // Pin analogico para el dedo medio   ---> 'M'
  servo4.attach(A1); // Pin analogico para el dedo anular  ---> 'A'
  servo5.attach(A0); // Pin analogico para el dedo meñique ---> 'Q' 
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(180);
  servo5.write(180);
  
  
}

void Move(char finger, bool status){
  if(status == true){

    if(finger == 'P'){
      servo1.write(180);
      tone (salida,1800,200);
    }else if(finger == 'I'){
      servo2.write(180);
      tone (salida,2000,200);
    }else if(finger == 'M'){
      servo3.write(180);
      tone (salida,2200,200);
    }else if(finger == 'A'){
      servo4.write(0);
      tone (salida,2400,200);
    }else if(finger == 'Q'){
      servo5.write(0);
      tone (salida,2600,200);
    }else if(finger == 'T'){
      servo1.write(180);
      servo2.write(180);
      servo3.write(180);
      servo4.write(0);
      servo5.write(0);
      tone (salida,3000,200);
    }
  }else{
    if(finger == 'P'){
      servo1.write(0);
      tone (salida,1800,200);
    }else if(finger == 'I'){
      servo2.write(0);
      tone (salida,2000,200);
    }else if(finger == 'M'){
      servo3.write(0);
      tone (salida,2200,200);
    }else if(finger == 'A'){
      servo4.write(180);
      tone (salida,2400,200);
    }else if(finger == 'Q'){
      servo5.write(180);
      tone (salida,2600,200);
    }else if(finger == 'T'){
      servo1.write(0);
      servo2.write(0);
      servo3.write(0);
      servo4.write(180);
      servo5.write(180);
      tone (salida,3000,200);
    } 
  }
}

void loop() {
  /**
  tone (salida,1800,1000);
  servo1.write(180);
  delay(2000);
  servo1.write(0);
  delay(2000);

 //SERVO2
  tone (salida,2000,1000);
  servo2.write(180);
  delay(2000);
  servo2.write(0);
  delay(2000);

 //SERVO3
   tone (salida,2200,1000);
  servo3.write(180);
  delay(2000);
  servo3.write(0);
  delay(2000);

 //SERVO4
  tone (salida,2400,1000);
  servo4.write(180);
  delay(2000);
  servo4.write(0);
  delay(2000);

 //SERVO5
  tone (salida,2600,1000);
  servo5.write(180);
  delay(2000);
  servo5.write(0);
  delay(2000);
  */
  
  tone (salida,2000,5000);
  delay(5000);
  
  delay(16000);
  Move('T',true);
  delay(1000);
  Move('P',false);
  delay(1166);
  Move('I',false); 
  delay(1166);
  Move('M',false); 
  delay(1166);
  Move('A', false); 
  delay(200);
  Move('Q',false);
  delay(3000);
  Move('T',true);
  delay(200);
  Move('P',false);
  delay(6000);
  Move('P',true);
  Move('I',false); 
  delay(6000);
  Move('M',false); 
  delay(6000);
  Move('I',true);
  Move('M',true);
  Move('A',false); 
  delay(7000);
  Move('A',true);
  Move('Q',false); 
  delay(13000); 
  Move('Q',true);
  delay(6000);
  Move('T',false);
  
 
}
