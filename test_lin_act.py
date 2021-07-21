import argparse
from pacific.servos import linact


def parse_command():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", type=int, help="servo port.", default=0)
    parser.add_argument(
        "-o", "--open", help="open", action="store_true")
    parser.add_argument(
        "-c", "--close", help="open", action="store_true")
    return parser.parse_args()


def main():
    args = parse_command()

    print(args.port)
    print(args.open)
    print(args.close)

    servo = linact.LinAct(args.port)

    if args.open is True:
        servo.open()

    if args.close is True:
        servo.close()


if __name__ == "__main__":
    main()
