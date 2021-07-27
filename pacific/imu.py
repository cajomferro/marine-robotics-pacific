from icm20948 import ICM20948  # https://github.com/pimoroni/icm20948-python
from dataclasses import dataclass
import math


@dataclass
class IMUSensorFusion:
    gyro_sens: float = 65.5
    gx_offset: float = -0.5
    gy_offset: float = -0.8
    accel_sens: float = 8.192
    pitch: float = 0
    roll: float = 0
    alpha: float = 0.7
    dt: float = 0.32
    imu = ICM20948(0x69)

    def read(self):
        """
        Read and calibrate
        Based on: https://andrewmourcos.github.io/blog/2020/11/21/complementary-filter.html
        """
        aX, aY, aZ, gX, gY, gZ = self.imu.read_accelerometer_gyro_data()

        accel = (aX / self.accel_sens, aY / self.accel_sens, aZ / self.accel_sens)
        gyro = (gX + self.gx_offset, gY + self.gy_offset, gZ)

        self.pitch += (gyro[0] / self.gyro_sens) * self.dt
        self.roll -= (gyro[1] / self.gyro_sens) * self.dt

        # Only use accelerometer when it's steady (magnitude is near 1g)
        forceMagnitude = math.sqrt(accel[0] ** 2 + accel[1] ** 2 + accel[2] ** 2)

        if 0.9 < forceMagnitude < 1.1:
            self.pitch = self.pitch * self.alpha + math.atan2(accel[1],
                                                              math.sqrt(accel[0] ** 2 + accel[2] ** 2)) * (
                                 180 / math.pi) * (1 - self.alpha)
            self.roll = self.roll * self.alpha + math.atan2(-accel[0], accel[2]) * (180 / math.pi) * (
                    1 - self.alpha)

        p = (self.pitch * 180 / math.pi)
        r = (self.roll * 180 / math.pi)

        return round(p), round(r)
