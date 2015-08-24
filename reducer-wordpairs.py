
import sys
from collections import Counter

datain = list()
for linein in sys.stdin:
    datain.append(linein)

print "Word Pairs:"

wordpairs = Counter(datain)
print "...Counting done"

pairs = list(set((wordpairs.most_common(len(wordpairs)))))
pairs.sort()
for pair,c in wordpairs.most_common(20):
    print "words",pair,"occur",c,"times."
#prints all word pairs

#prints selected word pairs
#prints x-y pair, and y-x pair for accuracy check also
print"\nUSA occurs with Japan", wordpairs["USA with Japan".lower()],"times."
print"\nChampion occurs with USA", wordpairs["Champion occurs with USA".lower()],"times."

print"\nJapan occurs with USA", wordpairs["Japan with USA".lower()],"times."
print"\nUSA occurs with Champion", wordpairs["USA occurs with Champion".lower()],"times."


##takes in list of wordpairs, counts
#sorts list of pairs (called pairs)
#prints all pairs
#prints selected pairs