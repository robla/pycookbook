#!/usr/bin/env python3

import argparse
import sys
import subprocess


def call_zim_journals_list(date):
    # https://stackoverflow.com/questions/5826427/can-a-python-script-execute-a-function-inside-a-bash-script
    funcfile = '/home/robla/src/aliases/dot.aliases'
    funcname = 'zimchanges-journals-list'
    funcarg = date
    wrapped_call = '. {}; {} {}'.format(funcfile, funcname, funcarg)
    print(wrapped_call)
    out_bytes = subprocess.check_output(['bash', '-c', wrapped_call])
    # https://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
    return out_bytes.decode('utf8')


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='Wrapping a bash function')
    parser.add_argument('date', help='a date to pass to function',
                        nargs='?', default='')
    return parser.parse_args()


def main(argv=None):
    """ A program that uses argparse """

    args = parse_arguments()
    output = call_zim_journals_list(args.date)
    print(output)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
