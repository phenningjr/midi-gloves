// MPU-6050 Short Example Sketch
// By Arduino User JohnChi
// August 17, 2014
// Public Domain
#include<Wire.h>
const int MPU=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
long sumAcX, sumAcY, sumAcZ, sumTmp, sumGyX, sumGyY, sumGyZ;
int counter = 0;

void setup(){
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600);
}
void loop(){
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,14,true);  // request a total of 14 registers
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)     
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

  sumAcX = sumAcX + AcX;
  sumAcY = sumAcY + AcY;
  sumAcZ = sumAcZ + AcZ;
  sumTmp = sumTmp + Tmp;
  sumGyX = sumGyX + GyX;
  sumGyY = sumGyY + GyY;
  sumGyZ = sumGyZ + GyZ;
  if (counter == 100)
  { 
    Serial.print("AcX = "); Serial.print(sumAcX/counter);
    Serial.print(" | AcY = "); Serial.print(sumAcY/counter);
    Serial.print(" | AcZ = "); Serial.print(sumAcZ/counter);
    Serial.print(" | Tmp = "); Serial.print(sumTmp/counter/340.00+36.53);  //equation for temperature in degrees C from datasheet
    Serial.print(" | GyX = "); 
    Serial.print(sumGyX/counter);
    Serial.print(" ");
    Serial.print(" | GyY = "); 
    Serial.print(sumGyY/counter);
    Serial.print(" ");
    Serial.print(" | GyZ = "); 
    Serial.println(sumGyZ/counter);
    counter = 0;
    sumAcX = 0;
    sumAcY = 0;
    sumAcZ = 0;
    sumTmp = 0;
    sumGyX = 0;
    sumGyY = 0;
    sumGyZ = 0;
  }
  else
  {
    counter = counter + 1; 
  }
  delay(3);
}

