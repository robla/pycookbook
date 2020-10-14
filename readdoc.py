#!/usr/bin/python3
"""This is a test

moo!
"""

def main(argv=None):
    """ main moo
    """
    print("split version of [0]:")
    print(__doc__.splitlines()[0])
    print("full enchilada")
    print(__doc__)
    print("boo")

main()
