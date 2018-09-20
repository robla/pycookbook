#!/usr/bin/python3

import configparser
import os
import sys


def main(argv=None):
    configfile = os.path.expanduser("~/.local/share/pycookbook-config-sample/sampleconfig")

    config = configparser.RawConfigParser()
    with open(configfile, "r") as f:
        config.readfp(f)

    api_token = config.get("authentication", "api_token")

    print(api_token)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)

