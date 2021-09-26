#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

int salida = 2;


void setup() {
    
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(180);
  servo5.write(180);
  tone (salida,2600,200);
  
  
  
  
  // Asignacion del pin digital para sonido.
  
  pinMode(salida,OUTPUT);
  
  // Asignacion de los pines analogicos a cada uno de los servos

  servo1.attach(A4); // Pin analogico para el dedo pulgar  ---> 'P'
  servo2.attach(A3); // Pin analogico para el dedo indice  ---> 'I'
  servo3.attach(A2); // Pin analogico para el dedo medio   ---> 'M'
  servo4.attach(A1); // Pin analogico para el dedo anular  ---> 'A'
  servo5.attach(A0); // Pin analogico para el dedo meñique ---> 'Q' 
  Serial.begin(9600);
}
// Funcion move, permite mover los dedos recibiendo como parametro el dedo y el status de movimiento.
void Move(String finger, String status_mov){
  if(status_mov == "false"){

    if(finger == "P"){
      servo1.write(180);
      tone (salida,1800,200);
    }else if(finger == "I"){
      servo2.write(180);
      tone (salida,2000,200);
    }else if(finger == "M"){
      servo3.write(180);
      tone (salida,2200,200);
    }else if(finger == "A"){
      servo4.write(0);
      tone (salida,2400,200);
    }else if(finger == "Q"){
      servo5.write(0);
      tone (salida,2600,200);
    }else if(finger == "T"){
      servo1.write(180);
      servo2.write(180);
      servo3.write(180);
      servo4.write(0);
      servo5.write(0);
      tone (salida,3000,200);
    }
  }else{
    if(finger == "P"){
      servo1.write(0);
      tone (salida,1800,200);
    }else if(finger == "I"){
      servo2.write(0);
      tone (salida,2000,200);
    }else if(finger == "M"){
      servo3.write(0);
      tone (salida,2200,200);
    }else if(finger == "A"){
      servo4.write(180);
      tone (salida,2400,200);
    }else if(finger == "Q"){
      servo5.write(180);
      tone (salida,2600,200);
    }else if(finger == "T"){
      servo1.write(0);
      servo2.write(0);
      servo3.write(0);
      servo4.write(180);
      servo5.write(180);
      tone (salida,3000,200);
    }
    
  }
  Serial.println("M"); 
}

// Recibe un timer que es la acnatidad de tiempo de delay y recibe una unidad.
void Create_delays(int timer, String unit){

  if(unit == "Seg"){
    delay(timer*1000);
  }else if(unit == "Min"){
      delay(timer*10000);
  }else{
    delay(timer);
  }
  Serial.println("D"); 
}



int pos4,pos5,pos6;
String action1,act2,act3;

String Convert_String(String cad){

  pos4 = cad.indexOf(',');
  pos5 = cad.indexOf(';');
  pos6 = cad.indexOf('/');
  action1 = cad.substring(0,pos4);
  act2 = cad.substring(pos4+1,pos5);
  act3 = cad.substring(pos5+1,pos6);

  return (action1 + "," + act2 + ";" + act3 + "/");
  }

int pos1,pos2,pos3,delay_time,cont,subline;
String cad,action,unit,finger,status_mov,txt,line,new_line;

void loop() {
   
  
  if(Serial.available()){
    tone (salida,6000,400);
    cad = Serial.readString(); // mov,T;false/ del,5000;Mil/
   
    new_line = Convert_String(cad);
    txt += String(new_line);   
   
    if (cad.toInt() == 1){
      tone (salida,4000,3000);
      cont = 0;
      subline = 0; 
      line = "Start";
      while (line.toInt() != 1){
          subline = txt.indexOf('/');
          line = txt.substring(cont,subline+1);
          pos1 = line.indexOf(',');
          pos2 = line.indexOf(';');
          pos3 = line.indexOf('/');
          action  = line.substring(0,pos1);
          if(action == "mov"){
            finger = line.substring(pos1+1,pos2);
            status_mov = line.substring(pos2+1,pos3);
            Move(finger,status_mov);
          }else if(action == "del"){
            delay_time = line.substring(pos1+1,pos2).toInt();
            unit = line.substring(pos2+1,pos3);
            Create_delays(delay_time,unit);
          }else{
            tone (salida,2600,300);
            delay(500);
            tone (salida,2600,300);
            delay(500);
            tone (salida,2600,300);
            delay(500);
            tone (salida,2600,300);
            delay(500);
        
          }
          
        cont = subline+1;
        txt = txt.substring(cont,txt.length());
        cont= 0;
      
        }

     }else{
      Serial.println("P");
     }
  }
}

    



  /**
   * tone (salida,1800,1000);
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
  
  
  tone (salida,2000,5000);
  delay(5000);
  
  delay(16000);
  Move("T","true");
  delay(1000);
  Move("P","false");
  delay(1166);
  Move("I","false"); 
  delay(1166);
  Move("M","false"); 
  delay(1166);
  Move("A", "false"); 
  delay(200);
  Move("Q","false");
  delay(3000);
  Move("T","true");
  delay(200);
  Move("P","false");
  delay(6000);
  Move("P","true");
  Move("I","false"); 
  delay(6000);
  Move("M","false"); 
  delay(6000);
  Move("I","true");
  Move("M","true");
  Move("A","false"); 
  delay(7000);
  Move("A","true");
  Move("Q","false"); 
  delay(13000); 
  Move("Q","true");
  delay(6000);
  Move("T","false");
   */
 
  
