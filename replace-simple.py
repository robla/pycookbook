#!/usr/bin/python3
# lightly modified version of first example at
# http://pythontesting.net/python/regex-search-replace-examples/
import fileinput
import re
 
for line in fileinput.input():
    line = re.sub('foo','bar', line.rstrip())
    print(line)
