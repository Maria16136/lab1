import argparse
import sys
from .calculator import calc
from .converter import convert


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    calc_parser = subparsers.add_parser('calc')
    calc_parser.add_argument('math_expression')


    convert_parser = subparsers.add_parser('convert')
    convert_parser.add_argument('value')
    convert_parser.add_argument('--from', dest='unit_from', required=True)
    convert_parser.add_argument('--to', dest='unit_to', required=True)

    arguments = sys.argv[1:]

    if arguments[0] == 'calc' and arguments[1].startswith('-'):
        arguments.insert(1, '--')

    args = parser.parse_args(arguments)

    try:
        if args.command == 'calc':
            result = calc(args.math_expression)
        elif args.command == 'convert':
            result = convert(args.value, args.unit_from, args.unit_to)
        print(result)
    except Exception as error:
        print(error)
        sys.exit(2)


if __name__ == '__main__':
    main()