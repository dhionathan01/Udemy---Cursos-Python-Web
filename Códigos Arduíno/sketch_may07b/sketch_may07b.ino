// C++ code
//
int redpin = 12;
int bluepin = 10;
int greenpin = 9;
int potenciometro = 5;

void setup()
{
  Serial.begin(9600);
  pinMode(redpin, OUTPUT);
  pinMode(bluepin, OUTPUT);
  pinMode(greenpin, OUTPUT);
}

void redfunction(){
  digitalWrite(bluepin, LOW);
  digitalWrite(greenpin, LOW);
  digitalWrite(redpin, HIGH);
  
}

void bluefunction(){
  digitalWrite(bluepin, HIGH);
  digitalWrite(greenpin, LOW);
  digitalWrite(redpin, LOW);
  
}

void greenfunction(){
  digitalWrite(bluepin, LOW);
  digitalWrite(greenpin, HIGH);
  digitalWrite(redpin, LOW);
  
}




void loop()
{
  float sinal;
  sinal = analogRead(potenciometro);
  Serial.println(sinal);
  
  if(sinal >= 0 && sinal <= 400)
    bluefunction();
  else if(sinal > 400 && sinal <= 800)
    greenfunction();
  
    else if(sinal > 800 && sinal <= 1200)
      redfunction();
  
}
