#!/usr/bin/env python3
"""
A program that uses argparse.

Change the docstring above.  Srsly
"""

import argparse
import sys


def printallargs(args):
    """
    Print all of the arguments
    """

    print("== args.url ==")
    print(args.url)

    print("== args.files ==")
    print(args.files)

    print("== args.bmybaby ==")
    print(args.bmybaby)


def main(argv=None):
    # using splitlines to just get the first line
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])

    parser.add_argument('--url', dest='url', type=str,
                        help='a url that might be interesting')
    parser.add_argument('files', help='some files, of which there may not be any',
                        nargs='*', default=None)
    parser.add_argument('-b', '--bmybaby',
                        help='be my...be my baby',
                        action="store_true")
    args = parser.parse_args()

    printallargs(args)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
