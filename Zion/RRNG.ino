// Programa para controle de motor por comando serial
// Autor: Gustavo Cesário

int PINO_MOTOR = 6;
int PINO_MOTOR_INVERSO = 7;

boolean teste = false;

void setup()
{
  Serial.begin(9600);
  pinMode(PINO_MOTOR, OUTPUT);
  pinMode(PINO_MOTOR_INVERSO, OUTPUT);
  digitalWrite(PINO_MOTOR, LOW);
  digitalWrite(PINO_MOTOR_INVERSO, LOW);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop()
{
  if (Serial.available() <= 0 && !teste)
    return;

  String comando = Serial.readStringUntil(';');
  comando.trim();

  if (comando == "RODAR_DADO" || teste) {
    digitalWrite(PINO_MOTOR, HIGH);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1500);
    digitalWrite(PINO_MOTOR, LOW);
    digitalWrite(PINO_MOTOR_INVERSO, HIGH);
    digitalWrite(LED_BUILTIN, LOW);
    delay(700);
    digitalWrite(PINO_MOTOR_INVERSO, LOW);
  }
}
