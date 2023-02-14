#define BRAKEVCC 0                  // определяем значение резкого тормоза
#define CW   1                      // определяем значение вращения по часовой стрелке
#define CCW  2                      // определяем значение вращения против часовой стрелки
#define BRAKEGND 3                  // определяем значение остановки

const uint8_t inApin[2] = {7, 4};   // определяем выводы ключей A
const uint8_t inBpin[2] = {8, 9};   // определяем выводы ключей B
const uint8_t pwmpin[2] = {5, 6};   // определяем выводы ШИМ
const uint8_t cspin[2]  = {A2, A3}; // определяем выводы считывания тока
const uint8_t enpin[2]  = {A0, A1}; // определяем выводы состояния ключей AB. Ключи открываются, если притянуть к 0.
void setup()
{
  Serial.begin(9600); 
  // переводим выводы управления в режим "выход"
  for (int i=0; i<2; i++)
  {
    pinMode(inApin[i], OUTPUT);     // выводы ключей A
    pinMode(inBpin[i], OUTPUT);     // выводы ключей B
    pinMode(pwmpin[i], OUTPUT);     // выводы ШИМ
  }
  // инициируем моторы выключенными
  motorOff(0);
  motorOff(1);
}

void loop()
{
  motorGo(0, CW, 32);               // мотор 0 по часовой стрелке, ШИМ 17,5%
  motorGo(1, CCW, 127);             // мотор 1 против часовой стрелки, ШИМ 50%
  delay(3000);                      // ждём 3 секунды, моторы вращаются
  Serial.print(analogRead(cspin[0]));
  Serial.print("\t");
  Serial.print(analogRead(cspin[1]));
  delay(3000);
// переводим вывод состояния ключей мотора 1 в режим "выход":
  pinMode(enpin[1], OUTPUT);
// выключаем мотор 1:   
  digitalWrite(enpin[1], LOW);
// на три секунды: 
  delay(3000);
// включаем мотор 1, 
// переводя вывод состояния ключей в режим "вход":             
  pinMode(enpin[1], INPUT); 
  delay(3000);   
  motorGo(0, BRAKEVCC, 32);         // останавливаем мотор 0 в режим "тормоз"
  motorGo(1, BRAKEGND, 32);         // останавливаем мотор 1 в режим "выключен"
  while(true);                      // скетч не выполняется дальше
  
}

// функция выключения мотора:
void motorOff(int motor)            
{
  for (int i=0; i<2; i++)
  {
    digitalWrite(inApin[i], LOW);
    digitalWrite(inBpin[i], LOW);
  }
  analogWrite(pwmpin[motor], 0);
}


// функция включения мотора:
void motorGo(uint8_t motor, uint8_t direct, uint8_t pwm)  
{
// если номер мотора правильный:
  if (motor <= 1)
  {
// если направление совпадает со значениями направлений:
    if (direct <=3)
    {
// если направление мотора по часовой или плавный стоп,
// устанавливаем соответствующие значения ключа А выбранного мотора:
      if (direct <=1)
        digitalWrite(inApin[motor], HIGH);
      else
        digitalWrite(inApin[motor], LOW);

// если направление мотора по часовой или резкий стоп,
// устанавливаем соответствующие значения ключа B выбранного мотора:
      if ((direct==0)||(direct==2))
        digitalWrite(inBpin[motor], HIGH);
      else
        digitalWrite(inBpin[motor], LOW);
// устанавливаем ШИМ выбранного мотора
      analogWrite(pwmpin[motor], pwm);
    }
  }
}
