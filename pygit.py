#!/usr/bin/env python3

import argparse
import git
import os
import re
import sys


def parse_arguments():
    """ see http://docs.python.org/library/argparse """
    parser = argparse.ArgumentParser(
        description='pygit example')
    parser.add_argument('--nocommit', help='no commits to git repos',
        action="store_true")

    return parser.parse_args()


def main(argv=None):
    """ Sample of working with pygit """

    args = parse_arguments()
    commitflag = (not args.nocommit)

    repo = git.Repo('.')
    print("All untracked:")
    print(repo.untracked_files)
    regexp = re.compile(r'(txt|py)$')
    new_txt_or_py = [x for x in repo.untracked_files if regexp.search(x)]
    print("Ends in py or txt:")
    print(new_txt_or_py)
    print("Modified:")
    modded = [x.a_path for x in repo.index.diff(None).iter_change_type('M')]
    print(modded)
    

if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)

