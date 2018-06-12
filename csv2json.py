#!/usr/bin/python3
"""
Parse CSV file, making it json-ish
"""

import argparse
import csv
import json
import sys


def main(argv=None):
    # using splitlines to just get the first line
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument('infile', help='csv file to convert')

    args = parser.parse_args()

    list_of_rows = []
    with open(args.infile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_of_rows.append(row)

    # output file handle, which we'll just hardcode to stdout for now
    outfh = sys.stdout

    json.dump(list_of_rows, outfh, indent=4)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
