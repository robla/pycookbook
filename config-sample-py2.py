#!/usr/bin/python2

import configparser
import os
import sys


def load_config_file():
    configfile = os.path.expanduser("~/.local/share/pycookbook-config-sample/sampleconfig")

    config = configparser.RawConfigParser()
    with open(configfile, "r") as f:
        config.readfp(f)
    return config


def get_apitoken(config):
    api_token = config.get("authentication", "api_token")

    return api_token


def main(argv=None):
    config = load_config_file()
    print get_apitoken(config)


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)

