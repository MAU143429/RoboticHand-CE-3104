#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;



void setup() {

/**
  pinMode(salida,OUTPUT);
  tone (salida,2000,1000);
  delay(1500);
  tone (salida,500,200);
  delay(300);
  tone (salida,500,200);
*/
  // Asignacion de los pines analogicos a cada uno de los servos

  servo1.attach(3); // Pin analogico para el dedo pulgar  ---> 'P'
  servo2.attach(4); // Pin analogico para el dedo indice  ---> 'I'
  servo3.attach(5); // Pin analogico para el dedo medio   ---> 'M'
  servo4.attach(6); // Pin analogico para el dedo anular  ---> 'A'
  servo5.attach(7); // Pin analogico para el dedo meñique ---> 'Q' 
  
  
}


void loop() {

 //Start System

 //SERVO1
 servo1.write(180);
 delay(2000);
 servo1.write(0);
 delay(2000);

 //SERVO2
 servo2.write(180);
 delay(2000);
 servo2.write(0);
 delay(2000);

 //SERVO3
 servo3.write(180);
 delay(2000);
 servo3.write(0);
 delay(2000);

 //SERVO4
 servo4.write(180);
 delay(2000);
 servo4.write(0);
 delay(2000);

 //SERVO5
 servo5.write(180);
 delay(2000);
 servo5.write(0);
 delay(2000);
 
}
