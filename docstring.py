#!/usr/bin/python3
"""This is a test

This line is extended text in the main header.
* Loaf of bread
* Container of milk
* Stick of butter
"""

def main(argv=None):
    """ First line after the main function """
    print("======================")
    print("First line of __doc__:")
    print("---------------------")
    print(__doc__.splitlines()[0])
    print("======================")
    print("__doc__ full enchilada")
    print("---------------------")
    print(__doc__)
    print("======================")
    print("main() docstring")
    print("---------------------")
    print(main.__doc__)

main()
