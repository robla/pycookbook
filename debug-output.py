#!/usr/bin/env python3

# Sometimes, I just want to print out a datastructure, and don't mind
# hack/kludging it in.  Hence this bit of cut-n-pastery

thingtoprint = {'a': 1, 'b': 2}
thingtoprint = {'a': 1, 'b': 2, 'c': set(['d', 'e'])}
try:
    import json
    print(json.dumps(thingtoprint, sort_keys=True, indent=4, separators=(',', ': ')))
except TypeError:
    print("thingtoprint is not JSON serializable")
    import pprint
    pprint.pprint(thingtoprint)


def example_function():
    pass

# Debugging tool for times when one needs to print all of the global functions
def list_all_gfuncs():
    global_namespace = globals()
    global_functions = [name for name, obj in global_namespace.items() if callable(obj)]
    retval = ''
    for i, func in enumerate(global_functions):
        retval += f"  {i}->{func}\n"
    return(retval) 


