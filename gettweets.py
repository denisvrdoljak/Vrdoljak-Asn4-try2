import time
from BeautifulSoup import BeautifulSoup
import urllib
import json
import re
import pymongo
import time,csv, datetime

import selenium
from selenium import webdriver
from bs4 import BeautifulSoup as soupy
firefox= webdriver.Firefox()
auth_MODE = "Twitter"
UTILS_FOLDER = "DenisUtils"
SEARCH_DEPTH = 25
TIME_STEP = 1
#S3_Bucket = "DataDumpBucket"

#setConfigVars(loadConfigs(auth_MODE))
import getpass

username = getpass.getuser()
utils_path = "/users/" + username + "/" + UTILS_FOLDER
sys.path.append(utils_path)
import tweepy
import Keychain
keyfob = Keychain.Keychain()
#print "keysets available:", keyfob.get_config_options()
key_dictionary = keyfob.loadConfigs(auth_MODE)
print "Successful keys load? -->", keyfob.setConfigsGlobal(key_dictionary)
for key, val in key_dictionary.items():
    exec(key + "= '" + val + "'") in globals()
########################

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
api = tweepy.API(auth)

import os
os.chdir("/Users/denisvrdoljak/Berkeley/W205/Asn4_Work")

def writecsv(tweet):
        try:
            fp = open(" WC2015-2.csv", "a")
            fp.write(tweet)
            fp.write("\n")
            fp.close()
        except:
            fp.close()
            print "Error writing to file"
        #print "\n\n",i,tweet.split(",")

def checkdone(tag,date):
    if str(tag+"-"+date) in open('/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/done.txt').read():
        close("/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/done.txt")
        return True
    else:
        close("/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/done.txt")
        return False


def writedone(tag, date):
        try:
            fp = open("/Users/denisvrdoljak/Berkeley/W205/Asn4_Work/done.txt", "a")
            fp.write(str(tag+"-"+date))
            fp.write("\n")
            fp.close()
        except:
            fp.close()
            print "Error writing to file"

def gettweets(queryURL):

    firefox.get(queryURL)
    for i in range(SEARCH_DEPTH):
        firefox.execute_script("window.scrollTo(0, 1000000)")
    
    soup = soupy(firefox.page_source)
    alltweets = soup.findAll('p',attrs={'class':'tweet-text'})
    print len(alltweets)
    allcreated = soup.findAll('span',attrs={'class':'_timestamp'})
    print len(allcreated)
    allurls = soup.findAll('span',attrs={'class':'js-display-url'})
    print len(allurls)
    j=0
    for i,tweet in enumerate(alltweets):
        if j < len(allurls) and allurls[j].text in tweet.text:
            url = allurls[j].text.lower()
            j+=1
        else:
            url = ""
        tweet =  re.sub('[,\t\n ]+', ' ', tweet.text.lower())
        created = datetime.datetime.fromtimestamp(int(allcreated[i]['data-time-ms'])/1000.0)
    
        tweet = tweet + "," + url + "," + created.strftime("%Y-%m-%d,%H") + "," + hashtag
        yield tweet.encode("utf-8")


def generateurl(hashtag,date):
    start_datetime = datetime.datetime.strptime(date,"%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(date,"%Y-%m-%d")+datetime.timedelta(days=TIME_STEP)
    start_date = datetime.date(start_datetime.year,start_datetime.month, start_datetime.day)
    end_date = datetime.date(end_datetime.year, end_datetime.month, end_datetime.day)
    queryURL = "https://twitter.com/search?q="+ urllib.quote_plus(hashtag) + "%20since%3A" + str(start_date) + "%20until%3A" + str(end_date) + "&src=typd&lang=en"
    return queryURL
def generatetags():
    hashtags_list = ["#WWC",
    '#WorldCup','#FIFA','#CANWNT','#GERWNT','#JPNWNT','#SUIWNT','#GER',
'#FRAWNT','#MEXWNT','#USWNT','#USA','#FIFAWWC','#WWC2015','#AUSWNT','#ENGWNT','#FRA',
'#ENG','#CAN','#CHN','#NZL','#NED','#USA','#CIV','#NOR','#THA','#JPN','#SUI','#CMR',
'#ECU','#SWE','#AUS','#NGA','#BRA','#KOR','#ESP','#CRC','#COL'
    ]
    date_list = []
    next_date = "2015-06-06"
    
    for i in range(30/TIME_STEP):
        #print next_date
        date_list.append(next_date)
        next_date = datetime.datetime.strptime(next_date,"%Y-%m-%d")+datetime.timedelta(days=TIME_STEP)
        next_date = str(datetime.date(next_date.year,next_date.month, next_date.day))
    for hashtag in hashtags_list:
        for date in date_list:
            yield hashtag,date

"""
#clear file/delete old contents/enter header field
open(" WC2015.csv", "w").close()
headerline = "tweet-text" + "," + "tweet-url" + "," + "Year-Month-Day" + "," + "Hour" + "," + "Hashtag-Searched"
writecsv(headerline)
"""
for hashtag,date in generatetags():
    if checkdone(hashtag,date):
        continue
    print hashtag, date
    tweeturl = generateurl(hashtag,date)
    #print hashtag
    #print date
    #print tweeturl

    for tweet in gettweets(tweeturl):
            writecsv(tweet)
    print "Done, next tag/date..."
    writedone(hashtag,date)