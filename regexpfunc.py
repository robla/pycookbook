#!/usr/bin/env python3
'''
regexpfunc.py - Simple example of a regular expression test in a function
'''

import argparse
import json
import re
import sys

def b1060time(timestr):
    '''
    This function is mainly a simple example of regular expression matching
    of a single input parameter.  In this case, it checks if the first
    parameter matches this regexp:

       r'\d{8}-\w{3}$'

    ...which corresponds to b1060time defined here:
    https://myndmess.org/wiki/b1060time
    '''

    regexp = r'\d{8}-\w{3}$'
    if(re.match(regexp, timestr)):
        return f"{timestr} matches {regexp}"
    else:
        return f"{timestr} does NOT match {regexp}"


def main(argv=None):
    # using splitlines to just get the first line
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1]) 
    parser.add_argument('timestr', help='time string')

    args = parser.parse_args()

    print("b1060time: " + b1060time(args.timestr))

    sys.exit()


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)


