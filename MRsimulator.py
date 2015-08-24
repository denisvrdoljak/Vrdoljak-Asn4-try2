###
### MR simulator, using inputdatastream(FILE_PATH) from mappers import
###

from mappers import *

#############
#main()
#############


print "######## stats, staring up, etc. ########"

#for tag in generatehashtags():
#    print tag, "\t\t", Counter(tagmapper(FILE_PATH))[tag]
print "######## done staring up, and stuff ########\n\n"

tagcounts = Counter(tagmapper(inputdatastream(FILE_PATH)))
print "Top 5 tweet tags:"
for toptag in tagcounts.most_common(5):
    t,c = toptag
    print str(t), "\t", str(c) + " times"
print "***** END Top 5 tweet tags *****\n\n"


print "Word URL's:"
urlcounts = Counter(urlmapper(inputdatastream(FILE_PATH)))
for urlstat in urlcounts.most_common(21):
    print urlstat
tweetlenlist = tweetlengthmapper(FILE_PATH)
tweetstats = Counter(tweetlenlist)

print "Tweet Length Mode (mode,count): ", tweetstats.most_common(1)[0]
print "Tweet Length Mean: ", sum(tweetlenlist)/len(tweetlenlist)




print "Tweets by Hour:"
print type(hourmapper(inputdatastream(FILE_PATH)))

hourcounts = Counter(hourmapper(inputdatastream(FILE_PATH)))
hours = list(set((hourcounts)))
hours.sort()
for hour in hours:
    print hour + "\t\t" + str(hourcounts[hour])
    pass

print "Word Counts (incl hashtags):"
wordcounts = Counter(wordmapper(inputdatastream(FILE_PATH)))
words = list(set((wordcounts.most_common(100))))
words.sort()
for word,c in words:
    if c < 10000:
        break
    print word + "\t\t" + str(wordcounts[word])


#wordpairmapper
#ANALYSIS 4, QUESTION3, QUESTION4
print "Word Pairs:"
wordpairs = Counter(wordpairmapper(inputdatastream(FILE_PATH)))
print "Counter done"
#pairs = list(set((wordpairs.most_common(len(wordpairs)))))
#pairs.sort()
for pair,c in wordpairs.most_common(20):
    print "words",pair,"occur",c,"times."

print"\nUSA occurs with Japan", wordpairs["USA with Japan".lower()],"times."
print"\nChampion occurs with USA", wordpairs["Champion occurs with USA".lower()],"times."

print"\nJapan occurs with USA", wordpairs["Japan with USA".lower()],"times."
print"\nUSA occurs with Champion", wordpairs["USA occurs with Champion".lower()],"times."

#OPTIONAL, ANALYSIS5


x="#WWC"
y="#WorldCup"
print "PMI of #WWC and #WorldCup =",PMI(wordpairs,x,y)
