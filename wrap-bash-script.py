#!/usr/bin/env python3

import argparse
import sys
import os


def myxtrim(path):
    import subprocess
    # get the raw output from a call to myxtrim
    out_bytes = subprocess.check_output(['myxtrim', path])
    # now convert it to utf8, and return the first line of the output
    return out_bytes.decode('utf8').split('\n')[0]


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='Call to myxtrim.sh')
    parser.add_argument('srcpath', help='path to trim', nargs='?',
                        default=os.curdir)
    return parser.parse_args()


def main(argv=None):
    """ A program that uses argparse """

    args = parse_arguments()
    print(myxtrim(args.srcpath))


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
