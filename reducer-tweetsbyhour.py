
import sys
from collections import Counter

datain = list()
for linein in sys.stdin:
    datain.append(linein)


hourcounts = Counter(datain)
hours = list(set(hourcounts))
hours.sort()

print "Tweets by Hour:"

for hour in hours:
    print hour + "\t\t" + str(hourcounts[hour])

##takes in list of hour counts
#note, hour counts come in with date-hour data
#sorts list of hours (called hours)
#prints date-hour, tabs, count for that date-hour


