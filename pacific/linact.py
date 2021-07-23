import time


class LinAct:

    def __init__(self, port: int = 0):
        import pi_servo_hat
        self.port: int = port
        self.servo = pi_servo_hat.PiServoHat()
        self.servo.restart()

    def close(self, min: int = 0):
        self.servo.move_servo_position(self.port, min)
        # time.sleep(1)

    def open(self, max: int = 90):
        self.servo.move_servo_position(self.port, max)
        # time.sleep(1)
