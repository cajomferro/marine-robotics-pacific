import time


class Servos:

    def __init__(self, port: int, min: int, max: int):
        import pi_servo_hat
        self.min: int = min
        self.max: int = max
        self.port: int = port
        self.servo = pi_servo_hat.PiServoHat()
        self.servo.restart()

    def close(self):
        self.servo.move_servo_position(self.port, self.min)
        # time.sleep(1)

    def open(self):
        self.servo.move_servo_position(self.port, self.max)
        # time.sleep(1)

    def set(self, val: int = 0):
        if val < self.min or val > self.max:
            print(f"Warning! Value {val} is outside range (min={self.min}, max={self.max})")
            return
        else:
            self.servo.move_servo_position(self.port, val)


class Syringe(Servos):
    def __init__(self, port: int = 0, min: int = 0, max: int = 90):
        super().__init__(port, min, max)


class Pitch(Servos):
    def __init__(self, port: int = 2, min: int = 55, max: int = 95):
        super().__init__(port, min, max)


class Roll(Servos):
    def __init__(self, port: int = 1, min: int = -90, max: int = 90):
        super().__init__(port, min, max)
        self.factor: float = 1.88  # 340=abs(60)+280 | 340 / 180 ~1.88
        self.offset: int = -60  # real min

    def close(self):
        pass

    def open(self):
        pass

    def set(self, val: int = 0):
        print(val)
        if val < self.min or val > self.max:
            print(f"Warning! Value {val} is outside range (min={self.min}, max={self.max})")
            return
        else:
            if val >= 0:
                val += 90
            else:
                val = 90 + val

            print(val)
            degrees = self.offset + (val * self.factor)
            print(degrees)
            self.servo.move_servo_position(self.port, degrees, 180)
