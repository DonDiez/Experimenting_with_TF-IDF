import string
import math
from os import listdir
from os.path import isfile, join
import operator
mypath = "files"


def log10(nr):
    return math.log(nr,10)

def IDF(word):
    antallDoc = 0
    for dictonary in listOfDict:
        if dictonary.__contains__(word):
            antallDoc+=1

    return (log10( len(files) / (antallDoc+1) + 1 ))

def count(file):
    with open("files/"+file) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    dict = {}
    nr = 0
    for line in content:
        for word in line.split():
            wordClean = ''.join(ch for ch in word if ch not in (string.punctuation+"1234567890-+_\n\t")).lower()
            if (len(wordClean)>=1):
                nr += 1
                if wordClean in dict:
                    dict[wordClean] += 1
                else:
                    dict[wordClean] = 1
    dict["xXxXx"]=nr
    return dict

def tdidf(q,docs):
    weights = []
    for x in range(len(docs)):
        row = []
        for word in q.split():
            if (docs[x].__contains__(word)):
                row.append((log10(1+docs[x][word])) * (IDF(word)))
            else:
                
                row.append(0)
        weights.append(row)
    print("q = "+q)
    res=[]
    for rows in weights:
        summas = 1
        for nr in rows:
            summas=summas*nr
        res.append(summas)
    return weights, res

def init():
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    listOfDict=[]
    print(files)
    for l in range(len(files)):
        listOfDict.append(count(files[l]))
    return listOfDict,files


q = input(str("Query? : "))
listOfDict,files = init()
w,res = tdidf(q,listOfDict)
max_index, max_value = max(enumerate(res), key=operator.itemgetter(1))

if sum(res)!=0:
    print("Document \""+files[max_index]+"\" is the most relevant with \t Q=\""+q+"\"")
else:
    print("No match")
       