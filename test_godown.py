import time
import sys
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime

from pacific.imu import IMUSensorFusion
from pacific.pressure import Pressure
from pacific.servos import Syringe


@dataclass
class Runner:
    path: Path = Path()

    def print(self, msg: str):
        now = datetime.now()  # current date and time
        with self.path.open() as fd:
            fd.write(f"{now.strftime('%H:%M:%S')}: {msg}")
            fd.write("\n")

    def __post_init__(self):
        self.print("Boot")
        self.pitch_roll = IMUSensorFusion()
        self.pressure = Pressure()
        self.syringe = Syringe()
        self.print("Waiting 10 seconds")
        time.sleep(10)

    def run(self):
        self.print("Going down")
        self.syringe.close()  # close linear act, open syringe

        while True:
            p, r = self.pitch_roll.read()
            press, temp = self.pressure.read()

            self.print(f"Pitch: {p} | Roll: {r}")
            self.print(f"Press: {press} | Temp: {temp}")

            time.sleep(0.5)


if __name__ == '__main__':
    try:
        r = Runner()
        r.run()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
