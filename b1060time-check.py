#!/usr/bin/env python3
'''Check if timestr is b1060time

This script is mainly a simple example of regular expression matching
of a single input parameter.  In this case, it checks if the first
parameter matches this regexp:

r'\d{8}-\w{3}$'

...which corresponds to b1060time defined here:
https://myndmess.org/wiki/b1060time
'''

import argparse
import sys
import re


def main(argv=None):
    """Check if timestr is b1060time"""

    parser = argparse.ArgumentParser(
        description='check if timestr is b1060time')
    parser.add_argument('timestr', help='time string')
    args = parser.parse_args()

    regexp = r'\d{8}-\w{3}$'
    if(re.match(regexp, args.timestr)):
        print(f"{args.timestr} matches {regexp}")
    else:
        print(f"{args.timestr} does NOT match {regexp}")


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
