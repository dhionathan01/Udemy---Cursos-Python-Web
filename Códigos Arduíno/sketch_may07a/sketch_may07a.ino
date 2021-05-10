// Projeto - Piscar Led
int ledPin = 9; // Atribui o valor 9 a variável inteira ledPin, que irá representar o pino digital 9

void setup() {

    pinMode(ledPin, OUTPUT); // Define ledpin (pino 9) como saída
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin, HIGH); // Coloa ledPin em nível alto(5V)
  delay(100); // Espera 100 milissegundos (0.1 segundo)
  digitalWrite(ledPin, LOW); // Coloca ledPin em nível baixo (0V)
  delay(100); // Espera 100 milissegundos (0.1 segundo)

}
