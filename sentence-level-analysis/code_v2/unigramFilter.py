import sys
from replaceExpand import *
from collections import defaultdict

if __name__ == '__main__':

    """create emoticons dictionary"""
    f=open("emoticonsWithPolarity.txt",'r')
    data=f.read().split('\n')
    emoticonsDict={}
    for i in data:
        if i:
            i=i.split()
            value=i[-1]
            key=i[:-1]
            for j in key:
                emoticonsDict[j]=value
    f.close()

    #print emoticonsDict

    """create acronym dictionary"""
    f=open("acronym_tokenised.txt",'r')
    data=f.read().split('\n')
    acronymDict={}
    for i in data:
        if i:
            i=i.split('\t')
            word=i[0].split()
            token=i[1].split()[1:]
            key=word[0].lower().strip(specialChar)
            value=[j.lower().strip(specialChar) for j in word[1:]]
            acronymDict[key]=[value,token]
    f.close()

    #print acronymDict

    """create stopWords dictionary"""
    stopWords=defaultdict(int)
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            line=line.strip(specialChar).lower()
            stopWords[line]=1
    f.close()

    uniDict={}
 
    f=open(sys.argv[1],'r')
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            if tweet:
                tweet, token, count1, count2 = preprocesingTweet1(tweet, token, emoticonsDict, acronymDict)
                for i in tweet:
                    word=i.strip(specialChar).lower()
                    if word:
                        if word in uniDict:
                            uniDict[line][eval(label)]+=1
                        else:
                            uniDict[line]=[0,0,0]
                tweet, token = preprocesingTweet2(tweet, token, stopWords)
    f.close()

    for i in uniDict.keys():
        print i,uniDict[i]

