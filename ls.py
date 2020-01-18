#!/usr/bin/env python3
"""
Get file listing of pwd in a scriptable way (instead of parsing
output of ls)
"""
import argparse
import sys


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
    """ Parse arguments and call ls() """

    parser = argparse.ArgumentParser()
    parser.add_argument('files', help='some files, of which there may not be any',
                        nargs='*', default=['.'])
    args = parser.parse_args()

    ls(args.files)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
