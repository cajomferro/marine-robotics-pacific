#!/usr/bin/python
from pacific import ms5837
from dataclasses import dataclass


@dataclass
class Pressure:
    sensor = None
    BAR_CONST: float = 0.0689475729

    def read(self):
        """
        Read tempeature (ºC) and pressure (bar)
        """

        # We have to read values from sensor to update pressure and temperature
        if not self.sensor.read():
            raise Exception("Pressure sensor read failed!")

        pressure_bar = self.sensor.pressure(ms5837.UNITS_psi) * self.BAR_CONST
        temp_celsius = self.sensor.temperature(ms5837.UNITS_Centigrade)

        return pressure_bar, temp_celsius

    def __post_init__(self):
        self.sensor = ms5837.MS5837_30BA()  # Default I2C bus is 1 (Raspberry Pi 3)

        # We must initialize the sensor before reading it
        if not self.sensor.init():
            raise Exception("Pressure sensor could not be initialized")
