
import sys
from collections import Counter

datain = list()
for linein in sys.stdin:
    datain.append(linein)

tagcounts = Counter(datain))
print "Top 5 tweet tags:"
for toptag in tagcounts.most_common(len(tagcounts)):
    t,c = toptag
    print str(t), "\t", str(c) + " times"
