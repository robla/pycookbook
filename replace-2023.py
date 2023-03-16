#!/usr/bin/env python3
'''
replace-2023.py - an updated argparse example to use as a starter script for
software that will use argparse to get the input file and possibly the output
file.
'''

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

def main(argv=None):
    """ A program that uses argparse """

    parser = argparse.ArgumentParser(
        description='A program that uses argparse')
    parser.add_argument('infile', help='input file')
    parser.add_argument('outfile', help='output file', nargs='?', default=None)
    parser.add_argument('--oldstring', '-o', help='original string', default='')
    parser.add_argument('--newstring', '-n', help='new string to use', default='')
    parser.add_argument('-f', '--force', help='no prompting; just doing',
        default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    pr1_str = f'Replacing {args.oldstring} with {args.newstring}...'
    pr2_str = f'Input: {args.infile}'
    pr3_str = f'Output: {args.outfile}'
    prFINAL_str = 'Does all that work for you? '

    if args.force:
        should_run = True
    else:
        prompt_string = pr1_str + "\n" + pr2_str + "\n" + pr3_str + "\n" + prFINAL_str
        should_run = confirm_step(prompt_string)

    if not should_run:
        sys.exit('KABOOOM!!!!!!')

    # Read in the file
    filedata = []
    with open(args.infile, 'r') as infile_line :
        filedata.append(infile_line.read())

    # Replace the target string
    outlinearray = []
    for thisstr in filedata:
        newstr = thisstr.replace(args.oldstring, args.newstring)
        outlinearray.append(newstr)

    # Write the file out again
    if args.outfile is None:
        for line in outlinearray:
           sys.stdout.write(line)
    else:
        with open(args.outfile, 'w') as outfile_line:
            for line in outlinearray:
                outfile_line.write(line)

if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)


