#include <Wire.h>
#include <MPU9250.h>
MPU9250 mpu;

void setup() {
  Serial.begin(115200);

  Wire.begin();
  if (!mpu.setup(0x68)) {
    Serial.println("MPU9250 connection failed!");
    while (1);
  }

}

void loop() {
  if (mpu.update()) {
    Serial.print("Accel X: "); Serial.print(mpu.getAccX());
    Serial.print("  Y: "); Serial.print(mpu.getAccY());
    Serial.print("  Z: "); Serial.print(mpu.getAccZ());
    Serial.println(" m/s^2");

    Serial.print("Gyro X: "); Serial.print(mpu.getGyroX());
    Serial.print("  Y: "); Serial.print(mpu.getGyroY());
    Serial.print("  Z: "); Serial.print(mpu.getGyroZ());
    Serial.println(" rad/s");
  }
 delay(1000);
}