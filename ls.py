#!/usr/bin/env python3

import argparse
import sys


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='Get a file listing in a more scriptable way')
    parser.add_argument('--url', dest='url', type=str, help='a url that might be interesting')
    parser.add_argument('files', help='some files, of which there may not be any', 
        nargs='*', default=None)
    parser.add_argument('-b', '--bmybaby',
                    help='be my...be my baby',
                    action="store_true")
    return parser.parse_args()


def ls():
    import os
    import sys
    print("== args.url ==")
    for subdir, dirs, files in os.walk("."):
        for f in dirs + files:
            ino = os.lstat(os.path.join(subdir, f)).st_ino
            sys.stdout.write("%d %s %s\n" % (ino, subdir, f))


def main(argv=None):
    """ A program that uses argparse """
    ls()
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


