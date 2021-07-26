#!/usr/bin/env python
# -----------------------------------------------------------------------------
# ex1_qwiic_ICM20948.py
#
# Simple Example for the Qwiic ICM20948 Device
# ------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, March 2020
#
# This python library supports the SparkFun Electroncis qwiic
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatable) single
# board computers.
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
# ==================================================================================
# Copyright (c) 2019 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==================================================================================
# Example 1
#

from __future__ import print_function
import qwiic_icm20948
from icm20948 import ICM20948
import time
import sys
from dataclasses import dataclass
import math


@dataclass
class Settings:
    gyro_sens: float = 65.5
    accel_sens: float = 8.192
    pitch = 0
    roll = 0
    alpha = 0.7


def calibrate(aX, aY, aZ, gX, gY, gZ, mX, mY, mZ, setts: Settings):
    accel = (aX / setts.accel_sens, aY / setts.accel_sens, aZ / setts.accel_sens)
    gyro = (gX-0.5, gY-0.8, gZ)
    print(gX, gY)
    magn = (mX, mY, mZ)

    # Integrating gyroscope data
    dt = 0.32

    setts.pitch += (gyro[0] / setts.gyro_sens) * dt
    setts.roll -= (gyro[1] / setts.gyro_sens) * dt

    # Only use accelerometer when it's steady (magnitude is near 1g)
    forceMagnitude = math.sqrt(accel[0] ** 2 + accel[1] ** 2 + accel[2] ** 2)

    if forceMagnitude > 0.9 and forceMagnitude < 1.1:
        setts.pitch = setts.pitch * setts.alpha + math.atan2(accel[1],
                                                      math.sqrt(accel[0] ** 2 + accel[2] ** 2)) * (180 / math.pi) * (1 - setts.alpha)
        setts.roll = setts.roll * setts.alpha + math.atan2(-accel[0], accel[2]) * (180 / math.pi) * (1 - setts.alpha)

    p = (setts.pitch * 180 / math.pi)
    r = (setts.roll * 180 / math.pi)
    return round(p), round(r), setts


def example():
    i2c_addr = 0x69
    imu = ICM20948(i2c_addr)
    setts = Settings()

    while True:
        x, y, z = imu.read_magnetometer_data()

        ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
    #     print("""
    # Accel: {:05.2f} {:05.2f} {:05.2f}
    # Gyro:  {:05.2f} {:05.2f} {:05.2f}
    # Mag:   {:05.2f} {:05.2f} {:05.2f}""".format(
    #         ax, ay, az, gx, gy, gz, x, y, z
    #     ))

        p, r, setts = calibrate(ax, ay, az,
                                gx, gy, gz,
                                x, y, z,
                                setts)
        print("roll: ", r)
        print("pitch: ", p)




# def runExample():
#     print("\nSparkFun 9DoF ICM-20948 Sensor  Example 1\n")
#     IMU = qwiic_icm20948.QwiicIcm20948()
#
#     if IMU.connected == False:
#         print("The Qwiic ICM20948 device isn't connected to the system. Please check your connection", \
#               file=sys.stderr)
#         return
#
#     IMU.begin()
#
#     while True:
#         if IMU.dataReady():
#             IMU.getAgmt()  # read all axis and temp from sensor, note this also updates all instance variables
#             print( \
#                 'Ax: {: 06d}'.format(IMU.axRaw) \
#                 , '\t', 'Ay: {: 06d}'.format(IMU.ayRaw) \
#                 , '\t', 'Az: {: 06d}'.format(IMU.azRaw) \
#                 , '\t', 'Gx: {: 06d}'.format(IMU.gxRaw) \
#                 , '\t', 'Gy: {: 06d}'.format(IMU.gyRaw) \
#                 , '\t', 'Gz: {: 06d}'.format(IMU.gzRaw) \
#                 , '\t', 'Mx: {: 06d}'.format(IMU.mxRaw) \
#                 , '\t', 'My: {: 06d}'.format(IMU.myRaw) \
#                 , '\t', 'Mz: {: 06d}'.format(IMU.mzRaw) \
#                 )
#             setts = Settings()
#             setts.last_time = time.time()
#             p, r, setts = calibrate(IMU.axRaw, IMU.ayRaw, IMU.azRaw,
#                                     IMU.gxRaw, IMU.gyRaw, IMU.gzRaw,
#                                     IMU.mxRaw, IMU.myRaw, IMU.mzRaw,
#                                     setts)
#             print(p)
#             print(r)
#             time.sleep(0.03)
#         else:
#             print("Waiting for data")
#             time.sleep(0.5)


if __name__ == '__main__':
    try:
        # runExample()
        example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
