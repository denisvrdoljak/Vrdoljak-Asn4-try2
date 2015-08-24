from mapper import *
import sys

datain = list()
for linein in sys.stdin:
    datain.append(linein)

for lineout in wordpairmapper(datain):
    print lineout

#wordpairmapper function takes in a generator or list
#and returns a list of results, one result-instance per line
