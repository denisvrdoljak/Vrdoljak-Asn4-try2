
import sys
from collections import Counter

datain = list()
for linein in sys.stdin:
    datain.append(linein)


wordcounts = Counter(datain))
words = list(set((wordcounts.most_common(100))))
words.sort()
for word,c in words:
    if c < 10000:
        break
    print word + "\t\t" + str(wordcounts[word])



##takes in list of word counts
#sorts list of wordcounts (called words)
#prints word, tabs, count for that word
#only prints words with over 10k count


