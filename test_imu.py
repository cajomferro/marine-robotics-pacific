# import time
import sys
from pacific.imu import IMUSensorFusion


def run():
    pitch_roll = IMUSensorFusion()
    while True:
        p, r = pitch_roll.read()
        print("pitch: ", p)
        print("roll: ", r)


if __name__ == '__main__':
    try:
        run()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
