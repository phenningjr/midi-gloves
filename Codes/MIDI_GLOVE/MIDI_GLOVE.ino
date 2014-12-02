
#define NOTE_B0  31
#define NOTE_C1  33
#define NOTE_CS1 35
#define NOTE_D1  37
#define NOTE_DS1 39
#define NOTE_E1  41
#define NOTE_F1  44
#define NOTE_FS1 46
#define NOTE_G1  49
#define NOTE_GS1 52
#define NOTE_A1  55
#define NOTE_AS1 58
#define NOTE_B1  62
#define NOTE_C2  65
#define NOTE_CS2 69
#define NOTE_D2  73
#define NOTE_DS2 78
#define NOTE_E2  82
#define NOTE_F2  87
#define NOTE_FS2 93
#define NOTE_G2  98
#define NOTE_GS2 104
#define NOTE_A2  110
#define NOTE_AS2 117
#define NOTE_B2  123
#define NOTE_C3  131
#define NOTE_CS3 139
#define NOTE_D3  147
#define NOTE_DS3 156
#define NOTE_E3  165
#define NOTE_F3  175
#define NOTE_FS3 185
#define NOTE_G3  196
#define NOTE_GS3 208
#define NOTE_A3  220
#define NOTE_AS3 233
#define NOTE_B3  247
#define NOTE_C4  262
#define NOTE_CS4 277
#define NOTE_D4  294
#define NOTE_DS4 311
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_FS4 370
#define NOTE_G4  392
#define NOTE_GS4 415
#define NOTE_A4  440
#define NOTE_AS4 466
#define NOTE_B4  494
#define NOTE_C5  523
#define NOTE_CS5 554
#define NOTE_D5  587
#define NOTE_DS5 622
#define NOTE_E5  659
#define NOTE_F5  698
#define NOTE_FS5 740
#define NOTE_G5  784
#define NOTE_GS5 831
#define NOTE_A5  880
#define NOTE_AS5 932
#define NOTE_B5  988
#define NOTE_C6  1047
#define NOTE_CS6 1109
#define NOTE_D6  1175
#define NOTE_DS6 1245
#define NOTE_E6  1319
#define NOTE_F6  1397
#define NOTE_FS6 1480
#define NOTE_G6  1568
#define NOTE_GS6 1661
#define NOTE_A6  1760
#define NOTE_AS6 1865
#define NOTE_B6  1976
#define NOTE_C7  2093
#define NOTE_CS7 2217
#define NOTE_D7  2349
#define NOTE_DS7 2489
#define NOTE_E7  2637
#define NOTE_F7  2794
#define NOTE_FS7 2960
#define NOTE_G7  3136
#define NOTE_GS7 3322
#define NOTE_A7  3520
#define NOTE_AS7 3729
#define NOTE_B7  3951
#define NOTE_C8  4186
#define NOTE_CS8 4435
#define NOTE_D8  4699
#define NOTE_DS8 4978

int vout = 2;
int vout2 = 4;
int vout3 = 7;
int vout4 = 8;
int vout5 = 13;
int buzzer = 12;

int threshold = 350;
int threshold2 = 350;
int threshold3 = 330;
int threshold4 = 320;
int threshold5 = 380;

boolean Down = false;
boolean Down2 = false;
boolean Down3 = false;
boolean Down4 = false;
boolean Down5 = false;
boolean allDown = false;

int modeJustChanged = 0;

int notes[8] = {
  NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5, NOTE_D5, NOTE_E5, NOTE_FS5, NOTE_G5};
int octave = 0;

int mode = 0;


void setup() 
{
  Serial.begin(9600);

  pinMode(vout, OUTPUT);
  pinMode(vout2, OUTPUT);
  pinMode(vout3, OUTPUT);
  pinMode(vout4, OUTPUT);
  pinMode(vout5, OUTPUT);

  digitalWrite(vout, HIGH);
  digitalWrite(vout2, HIGH);
  digitalWrite(vout3, HIGH);
  digitalWrite(vout4, HIGH);
  digitalWrite(vout5, HIGH);

}

void loop() 
{
  int notePlaying = 0;
  int reading = 0;
  int reading2 = 0;
  int reading3 = 0;
  int reading4 = 0;
  int reading5 = 0;

  reading = analogRead(2);
  reading2 = analogRead(5);
  reading3 = analogRead(1);
  reading4 = analogRead(4);
  reading5 = analogRead(3);

  if (reading < threshold)
  {
    Down = true;
  } 
  else
  {
    Down = false; 
    modeJustChanged = 0;
  }
  if (reading2 < threshold2)
  {
    Down2 = true;
  } 
  else
  {
    Down2 = false; 
    modeJustChanged = 0;
  }
  if (reading3 < threshold3)
  {
    Down3 = true;
  } 
  else
  {
    Down3 = false; 
    modeJustChanged = 0;
  }
  if (reading4 < threshold4)
  {
    Down4 = true;
  } 
  else
  {
    Down4 = false; 
    modeJustChanged = 0;
  }
  if (reading5 < threshold5 && Down5 == false)
  {
    Down5 = true;
    octave = 1; 


  } 
  else if (reading5 > threshold5 && Down5 == true)
  {
    Down5 = false; 
    octave = 0;
  }

  if (Down && Down2 && Down3 && Down4 && allDown == false)
  {
    allDown = true;
    if (mode == 0) 
      mode = 1;
    else if (mode == 1) 
      mode = 2;
    else if (mode == 2)
      mode = 0; 
    modeJustChanged = 1;


  } 
  else if (!Down || !Down2 || !Down3 || !Down4 && allDown == true)
  {
    allDown = false; 
  }

  if (notePlaying == 0)
  {
    if (Down)
    {
      notePlaying = 1;
    } 
    else if (Down2)
    {
      notePlaying = 2;
    } 
    else if (Down3)
    {
      notePlaying = 3;
    } 
    else if (Down4)
    {
      notePlaying = 4;
    } 
  }

  else
  {
    if (!Down && notePlaying == 1 || !Down2 && notePlaying == 2 || !Down3 && notePlaying == 3 || !Down4 && notePlaying == 4)
    {
      notePlaying = 0;
    } 
  }

  if (mode == 0 && modeJustChanged == 0)
  {
    switch (notePlaying)
    {
    case 0:
      noTone(buzzer);
      break;
    case 1:
      tone(buzzer, notes[octave * 4]);
      break;
    case 2:
      tone(buzzer, notes[octave * 4 + 1]);
      break;
    case 3:
      tone(buzzer, notes[octave * 4 + 2]);
      break;
    case 4:
      tone(buzzer, notes[octave * 4 + 3]);
      break;
    }
  }
  else if (mode == 1 && modeJustChanged == 0)
  {
    switch (notePlaying)
    {
    case 0:
      noTone(buzzer);
      break;
    case 1:
      tone(buzzer, NOTE_E5);
      break;
    case 2:
      tone(buzzer, NOTE_C5);
      break;
    case 3:
      tone(buzzer, NOTE_G5);
      break;
    case 4:
      tone(buzzer, NOTE_G4);
      break;
    }
  }


  String strOutput = " ";
  strOutput = (reading + strOutput + reading2 + strOutput + reading3 + strOutput + reading4 + strOutput + reading5 + strOutput + octave + strOutput + notePlaying + strOutput + mode + strOutput + modeJustChanged);

  Serial.println (strOutput);

}

