#!/usr/bin/env python3

import argparse
import sys


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='Get a file listing in a more scriptable way')
    parser.add_argument('files', help='some files, of which there may not be any',
                        nargs='*', default=['.'])
    return parser.parse_args()


def ls(files=['.']):
    """
    Get file listing of pwd in a more scriptable way using scandir from
    Python 3.5
    """
    import os
    import sys
    for f in files:
        for entry in os.scandir(f):
            print(entry.name)


def main(argv=None):
    """ A program that uses argparse """
    args = parse_arguments()
    ls(args.files)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
