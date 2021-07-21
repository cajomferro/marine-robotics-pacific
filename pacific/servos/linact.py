import argparse
import time

class LinAct:

    def __init__(self, port:int=0):
        import pi_servo_hat
        self.port = port
        self.servo = pi_servo_hat.PiServoHat()
        self.servo.restart()

    def close(self):
        self.servo.move_servo_position(0, 0)
        time.sleep(1)

    def open(self):
        self.servo.move_servo_position(0, 90)
        time.sleep(1)

def parse_command():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", type=int, help="servo port.", default=0)
    return parser.parse_args()

def main():
    args = parse_command()


if __name__ == "__main__":
    main()
