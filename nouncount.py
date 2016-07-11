from nltk.tag.stanford import StanfordPOSTagger

from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
from collections import Counter
import nltk
"""import os

from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/home/eunsoo/stanford-parser-full-2015-04-20/stanford-postagger.jar'
os.environ['STANFORD_MODELS'] = '/home/eunsoo/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar'

parser = stanford.StanfordParser(model_path="/home/eunsoo/stanford-postagger-full-2015-04-20/models/english-bidirectional-distsim.tagger")
                                           # "/location/of/the/englishPCFG.ser.gz")
#print parser.raw_batch_parse(("Hello, My name is Melroy.", "What is your name?"))
#print os.environ.get('CLASSPATH')
#st = StanfordPOSTagger('english-bidirectional-distsim.tagger')

#st.tag('What is the airspeed of an unladen swallow ?'.split())
"""
wordlist=[]
synonyms = []
text=[]
global ssum
global wordlist
f=open("nountest.txt",'r')
while(1):
    tt=f.readline()
    if tt:
        a = tt.find('|')
        k = tt.find('|', a + 2)

        #print tt[a + 2:k]
        text = nltk.word_tokenize(tt[a + 2:k])
        b = []
        for a in nltk.pos_tag(text):
            if a[1] == 'NN':
                b.append(a[0].lower())
        ssum = 0

        for s in b:
            synonyms = []
            ssum = 0
            for syn in wordnet.synsets(s):
                for l in syn.lemmas():
                    if (l.name):
                        synonyms.append(l.name())
            for a in set(synonyms):
                ssum = ssum + 1
                #wordlist.append(s)
            #print s, "-", ssum
            wordlist.append((ssum,s))

        f.readline()
    else:
        break
newlist=[]
s=0
newlist=list(set(wordlist))
print len(newlist)
print type(newlist)
newlist.sort(reverse=True)
for y in newlist:
    s=s+y[0]
    print y
print s/1044
#print set(wordlist)
#print len(set(wordlist))"""

