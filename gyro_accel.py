from machine import I2C, Pin
import time

MPU9250_ADDRESS = 0x68

PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

def mpu9250_init():
    i2c.writeto_mem(MPU9250_ADDRESS, PWR_MGMT_1, b'\x00')

def read_raw_data(addr):
    high = i2c.readfrom_mem(MPU9250_ADDRESS, addr, 1)[0]
    low = i2c.readfrom_mem(MPU9250_ADDRESS, addr + 1, 1)[0]
    value = (high << 8) | low

    if value > 32768:
        value = value - 65536
    return value

def read_accel_data():
    accel_x = read_raw_data(ACCEL_XOUT_H)
    accel_y = read_raw_data(ACCEL_XOUT_H + 2)
    accel_z = read_raw_data(ACCEL_XOUT_H + 4)

    accel_x = accel_x / 16384.0
    accel_y = accel_y / 16384.0
    accel_z = accel_z / 16384.0

    return accel_x, accel_y, accel_z

def read_gyro_data():
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_XOUT_H + 2)
    gyro_z = read_raw_data(GYRO_XOUT_H + 4)

    gyro_x = gyro_x / 131.0
    gyro_y = gyro_y / 131.0
    gyro_z = gyro_z / 131.0

    return gyro_x, gyro_y, gyro_z
