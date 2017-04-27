#!/usr/bin/env python3

import argparse
import sys


# adapted from http://stackoverflow.com/a/3042378/314034
def confirm_step(prompt):
    # raw_input returns the empty string for "enter"
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])

    print(prompt)
    while True:
        choice = input().lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
           sys.stdout.write("Please respond with 'yes' or 'no'")


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='A program that confirms before doing something')
    parser.add_argument('-f', '--force',
                    help='force the action without confirming',
                    action="store_true")
    return parser.parse_args()


def main(argv=None):
    """ A program that uses argparse """

    args = parse_arguments()
    print("== args.force ==")
    print(args.force)

    if args.force:
        print("THEY MADE ME DO IT!!!")
    elif confirm_step('wanna keep going?'):
        print("groovy!")
    else:
        print("well, nevermind then")


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)


