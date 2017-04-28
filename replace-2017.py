#!/usr/bin/env python3

import argparse
import sys


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='A program that uses argparse')
    parser.add_argument('infile', help='input file')
    parser.add_argument('outfile', help='output file', default='-')
    parser.add_argument('--oldstring', '-o', help='original file')
    parser.add_argument('--newstring', '-n', help='new string to use')
    return parser.parse_args()


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


def main(argv=None):
    """ A program that uses argparse """

    args = parse_arguments()

    prompt = "Replace {} with {} in {} and output to {}?".format(
        args.oldstring,
        args.newstring,
        args.infile,
        args.outfile)
    confirm_step(prompt)

    # cribbing from http://stackoverflow.com/a/22876912/314034     
    # Read in the file
    with open(args.infile, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(args.oldstring, args.newstring)

    # Write the file out again
    with open(args.outfile, 'w') as file:
        file.write(filedata)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)


