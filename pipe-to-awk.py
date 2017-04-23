#!/usr/bin/env python
# this is an attempt to replicate this:
# $ wmctrl -l | awk '{ print $4 " is on desktop " $2 }'

import subprocess
out_bytes = subprocess.check_output(['wmctrl','-l'])
lines = out_bytes.split('\n')
for line in lines:
    try:
        lineout = line.split()[3]
        lineout += " is on desktop "
        lineout += line.split()[1]
        print(lineout)
    except:
        pass
