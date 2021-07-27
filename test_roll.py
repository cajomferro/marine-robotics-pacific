import argparse
from pacific import servos


def parse_command():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", type=int, help="servo port.", default=1)
    parser.add_argument(
        "-m", "--min", help="min value", action="store_true")
    parser.add_argument(
        "-M", "--max", help="max value", action="store_true")
    parser.add_argument(
        "-c", "--center", help="center", action="store_true")
    parser.add_argument(
        "-s", "--set", type=int, help="specific value")
    return parser.parse_args()


def main():
    args = parse_command()

    # print(args.port)
    # print(args.open)
    # print(args.close)

    servo = servos.Roll(port=args.port)

    if args.min is True:
        servo.set(-90)

    elif args.max is True:
        servo.set(90)

    elif args.center is True:
        servo.set()

    elif args.set is not None:
        servo.set(args.set)


if __name__ == "__main__":
    main()
