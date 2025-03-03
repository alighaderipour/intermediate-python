import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="simple calculator")
    parser.add_argument("--x", default = 1.0 , type = float, help="first argument")
    parser.add_argument("--o", default = 'sub' , type = str, help="operation: mul, add, sub,div")
    parser.add_argument("--y", default = 1.0 , type = float, help="sec argument")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y

if __name__ == "__main__":
    main()