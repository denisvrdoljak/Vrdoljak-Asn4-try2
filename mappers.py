import re
from collections import Counter

HEADERLINE = "tweet-text" + "," + "tweet-url" + "," + "Year-Month-Day" + "," + "Hour" + "," + "Hashtag-Searched"
FILE_PATH = "/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/WC2015-run1.csv"
#for simulator MR

#simulates MR input data stream
def inputdatastream(filepath):
    with open(filepath) as csvfile:
        for line in csvfile:
            yield line


#mapper, generates list of tags (incl repeats) given a list or generator as input
def tagmapper(datain):

    taglist = list()
    try:
        for line in datain:
            if HEADERLINE in line:
                pass
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            taglist.append(re.sub('[,\t\n ]+', '', tweettag))
        return taglist
    except:
        return False



#mapper, generates list of urls (incl repeats) given a list or generator as input
def urlmapper(datain):
    urllist = list()
    try:
        for line in datain:
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            urllist.append(tweeturl)
        return urllist
    except:
        return False


#mapper, generates list of tweet lengths (incl repeats) given a list or generator as input
def tweetlengthmapper(datain):
    lengthlist = list()
    try:
        for line in datain:
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            lengthlist.append(len(tweettext))
        return lengthlist
    except:
        return False


def hourmapper(datain):
    import re
    hourlist = list()

    try:
        for line in datain:
            if HEADERLINE in line:
                continue
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            timestamp = str(tweetdate+"@"+tweethour+"00hours")
            hourlist.append(timestamp)
        return hourlist
    except:
        return False

def wordmapper(datain):
    import re
    wordlist = list()
    try:
        for line in datain:
            if HEADERLINE in line:
                continue
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            for word in tweettext.split():
                wordlist.append(word)
        return wordlist
    except:
        return False








def listwordpairs(textline):
    pairlist = list()
    for word in textline.split():
        for word2 in textline.split():
            if len(word)<2 or len(word2)<2:
                continue
            pairlist.append(str(word + " with " + word2))
    return pairlist


def wordpairmapper(datain):
    wordpairs = list()
    try:
        for line in datain:
            if HEADERLINE in line:
                continue
            tweettext,tweeturl,tweetdate,tweethour,tweettag = line.split(",")
            for pair in listwordpairs(tweettext):
                wordpairs.append(pair)
        return wordpairs
    except:
        return False
        
#generates a PMI value, given a result set, and two values
def PMI(resultsset,x,y):
    import math
    top = resultsset[str(x+" with "+y).lower()]*len(resultsset)
    bottom = resultsset[str(x+" with "+x).lower()]*resultsset[str(y+" with "+y).lower()]
    return (math.log(top/bottom))








