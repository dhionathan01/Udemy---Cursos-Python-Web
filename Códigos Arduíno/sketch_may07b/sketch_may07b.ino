// Projeto ligar e Desligar Led com um botão do tipo Push
int buttonPin = 7;//Define buttonPin no pino digital 7
int ledPin = 10;//Define ledPin no pino digital 10
int estadoButton = 0;//Variável responsável por armazenar o estado do botão
void setup(){
pinMode(ledPin , OUTPUT);//Define ledPin (pino 10) como saída
pinMode(buttonPin , INPUT);//Define buttonPin (pino 7) como entrada
}
void loop(){
estadoButton = digitalRead(buttonPin);//Lê o valor de buttonPin e
if (estadoButton == HIGH) {//Se estadoButton for igual a HIGH ou 1
digitalWrite(ledPin , HIGH);//Define ledPin como HIGH, ligando o LED
delay(10000);//Intervalo de 100 milissegundos
}
else { //Senão = estadoButton for igual a LOW ou 0
digitalWrite(ledPin, LOW);//Define ledPin como LOW, desligando o LED
}
}
