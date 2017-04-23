#!/usr/bin/env python3
import sys
import subprocess



def main(argv=None):
    """ set up the desktop """

    out_bytes = subprocess.check_output(['wmctrl','-lx'])
    lines = out_bytes.decode("utf8").split('\n')
    for line in lines:
        print(line)
        field = line.split(maxsplit=4)
        try:
            lineout = ""
            lineout += ":0: "
            lineout += field[0]
            lineout += "\n:1: "
            lineout += field[1]
            lineout += "\n:2: "
            lineout += field[2]
            lineout += "\n:3: "
            lineout += field[3]
            lineout += "\n:4: "
            lineout += field[4]
            print(lineout)
        except:
            print(">>> ah crap <<<")
            pass



if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)


