#!/usr/bin/env python3

import argparse
import sys


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='A program that uses argparse')
    parser.add_argument('--url', dest='url', type=str, help='a url that might be interesting')
    parser.add_argument('files', help='some files, of which there may not be any', 
        nargs='*', default=None)
    parser.add_argument('-b', '--bmybaby',
                    help='be my...be my baby',
                    action="store_true")
    return parser.parse_args()


def main(argv=None):
    """ A program that uses argparse """

    args = parse_arguments()
    print("== args.url ==")
    print(args.url)

    print("== args.files ==")
    print(args.files)

    print("== args.bmybaby ==")
    print(args.bmybaby)

if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)


