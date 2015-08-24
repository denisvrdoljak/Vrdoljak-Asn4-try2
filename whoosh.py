import os
import whoosh
import codecs
from whoosh.fields import Schema
from whoosh.index import create_in
from mappers import inputdatastream
from whoosh.fields import ID, KEYWORD, TEXT

FILEPATH = "/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/ WC2015-2testing.csv"


#schema setup
my_schema = Schema(id = ID(unique=True, stored=True), 
                    path = ID(stored=True), 
                    tagsearch = ID(stored=True),
                    tags = TEXT(stored=True), 
                    date = TEXT(stored=True),
                    hour = TEXT(stored=True),
                    tweet = TEXT(stored=True))


#enter data
writer = index.writer()
os.mkdir("twitterwwc-index")
index = create_in("wwc-index1", my_schema)

for i,line in enumerate(inputdatastream(FILEPATH)):
    print ".",
    writer.add_document( path = FILEPATH.encode("utf-8"),
                    tagsearch = line.split(",")[4].encode("utf-8"),
                    tags = [word for word in line.split(",")[0] if '#' in word], 
                    date = line.split(",")[2].encode("utf-8"),
                    hour = line.split(",")[3].encode("utf-8"),
                    tweet = line.split(",")[0].encode("utf-8"))



#supported queries
keywords = "soccer"

#showed up under #usa search, and has #jap in tweet
usa-also-tags-jap = And([Term(u'tagsearch',u'#usa'), Term(u'tags',u'#jap')])
counter = CountingCollector()
searcher.search_with_collector(usa-also-tags-jap, counter)
print(counter.count)


#tags both #can and #fra (ie, france vs. canada..if they played)
canada-vs-france = And([Term(u'tags',u'#can'), Term(u'tags',u'#fra')])
counter = CountingCollector()
searcher.search_with_collector(canada-vs-france, counter)
print(counter.count)
#I thought it was wierd Can had the most results, and Fra had next to none (in English)

#Assignment example, retweeted (aka, starts with "RT:" in tweet.text), and has keywords too
retweets-ExampleQuery = And([Term(u'tweet',u'RT:'), Term(u'tweet',keywords.encode("utg-8"))])
ccounter = CountingCollector()
searcher.search_with_collector(retweets-ExampleQuery, counter)
print(counter.count)

#keywords and "usa", not necessarily "#usa"
usa-vs-keywords = And([Term(u'tweet',u'usa'), Term(u'text',keywords.encode("utf-8"))])
ccounter = CountingCollector()
searcher.search_with_collector(usa-vs-keywords, counter)
print(counter.count)

#has "usa" and "champion" in tweet
usa-champion = And([Term(u'tweet',u'usa'), Term(u'text',u'champion')])
ccounter = CountingCollector()
searcher.search_with_collector(usa-champion, counter)
print(counter.count)

