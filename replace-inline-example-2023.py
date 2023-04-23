#!/usr/bin/python
import re

print('replace-inline-example-2023.py')
print('==============================')
print('------------------------------')
print('-- Example 1 --')
print('- Using \\1 \\2 etc -')
mootext = 'xxfooyy'
moonew_text, moocount = re.subn(r'^(x*)(?:foo)(y*)$', r'\1bar\2', mootext)
print(f"mootext: {mootext}\nmoonew_text: {moonew_text}\nmoocount: {moocount}\n")
print('------------------------------')
print('-- Example 2 --')
print('- Using \g<1> \g<2> etc -')
mootext = 'xxfooyy'
moonew_text, moocount = re.subn(r'^(x*)(?:foo)(y*)$', r'\g<1>bar\g<2>', mootext)
print(f"mootext: {mootext}\nmoonew_text: {moonew_text}\nmoocount: {moocount}\n")

