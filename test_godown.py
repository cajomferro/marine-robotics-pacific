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
    init_wait_time_sec: int = 20
    path: Path = Path("out.csv")

    def print(self, msg: str):
        now = datetime.now()  # current date and time
        output = f"{now.strftime('%H:%M:%S')}, {msg}\n"
        with self.path.open("a+") as fd:
            fd.write(output)
        print(output)

    def __post_init__(self):
        self.print("Boot")
        self.pitch_roll = IMUSensorFusion()
        self.pressure = Pressure()
        self.syringe = Syringe()
        self.syringe.open()  # open linear act, close syringe
        self.print(f"Waiting {self.init_wait_time_sec} seconds")
        time.sleep(self.init_wait_time_sec)

    def run(self):
        self.print("Going down")
        self.syringe.close()  # close linear act, open syringe

        counter = 0

        while counter <= 100:
            p, r = self.pitch_roll.read()
            press, temp = self.pressure.read()

            # self.print(f"Pitch: {p} | Roll: {r} | Press: {press} | Temp: {temp}")
            self.print(f"{p}, {r}, {press}, {temp}")
            time.sleep(0.5)

            counter += 1

        self.syringe.open()  # open linear act, open syringe
        time.sleep(10)


if __name__ == '__main__':
    try:
        r = Runner()
        r.run()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
