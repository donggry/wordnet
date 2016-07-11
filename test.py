from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
import nltk
for example in wn.synset('apple.n.01').examples():
    print example
# Get a collection of synsets (synonym sets) for a word
"""synsets = wordnet.synsets('book')

# Print the information
for synset in synsets:
    print "-" * 10
    print "Name:", synset.name
    print "Lexical Type:", synset.lexname
    print "Lemmas:", synset.lemma_names
    print "Definition:", synset.definition
    print "examples",synset.examples
    #for example in synset.examples:
       # print "Example:", example
# Get a collection of synsets (synonym sets) for a word
synsets = wordnet.synsets('book.n.01')
#print(synsets[0].name())
#print(synsets[7].lemmas()[0].name())
# Print the information
for synset in synsets:
    print "-" * 10
    print "Name:", synset.name
    #print "Lexical Type:", synset.lexname
    #print "Lemmas:", synset.lemma_names
    #print "Definition:", synset.definition
    for example in synset.examples:
        print "Example:", example"""
synonyms = []
antonyms = []
synslist=[]
b=[]
string="i love apple"
text = nltk.word_tokenize("And now apple for something book completely different")
nltk.pos_tag(text)
for a in nltk.pos_tag(text):
    if a[1]=='NN':
        b.append(a[0])
print b
ssum=0
print "AAAAAAAAAAAAAAAAA"
for s in b:
    print s
    global ssum

    synonyms = []
    ssum = 0

    for syn in wordnet.synsets("go"):
        test=[]
        synslist.append(syn)
        test.append(syn)
        #count=0
        ##for example in syn.examples():
            #print syn,"-",syn.lemmas()[count].name(), "-", example
            #count=count+1

        for l in syn.lemmas():
            if(l.name):
                synonyms.append(l)


    print set(synonyms)
   ### for a in set(synonyms):
      ##  print s,"-",ssum
    #print synonyms[36]
"""print(set(synonyms))
for a in wn.synset('bible.n.01').examples():
    print a
for example in set(synonyms).examples():
    #print syn, "-", example
       # if l.antonyms():
           # antonyms.append(l.antonyms()[0].name())

#print(set(synonyms))
for a in set(synonyms):
    #  wordnet.synsets(a).examples
#print(set(antonyms))
    b=a+".n.01"
    for example in wn.synset(b).examples():
        print b,"-",example

w1 = wordnet.synset('reserve.n.04')
w2 = wordnet.synset('book.n.04')
print(w1.wup_similarity(w2))"""
print"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n"
from nltk.corpus import wordnet
import itertools as IT
list1=[]
list2=[]
string1="this machine is very good for health"
string2="healthy food make us grow up"
a=string1.split()
for b in a:
    list1.append(b)
a2 = string2.split()
for b in a:
    list2.append(b)

"""list1 = ["machine", "good","health"]
list2 = ["healthy", "food", "grow", "up"]
def f(word1, word2):
    wordFromList1 = wordnet.synsets(word1)[0]
    wordFromList2 = wordnet.synsets(word2)[0]
    s = wordFromList1.wup_similarity(wordFromList2)
    return(wordFromList1.name, wordFromList2.name, wordFromList1.wup_similarity(wordFromList2))

#for word1 in list1:
    #similarities=(f(word1,word2) for word2 in list2)
    print(max(similarities, key=lambda x: x[2]))
for word1, word2 in IT.product(list1, list2):
    wordFromList1 = wordnet.synsets(word1)[0]
    wordFromList2 = wordnet.synsets(word2)[0]
    s = wordFromList1.wup_similarity(wordFromList2)
    print('{w1}, {w2}: {s}'.format(w1 = wordFromList1.name,w2 = wordFromList2.name,s = wordFromList1.wup_similarity(wordFromList2)))

counts = Counter(wordlist)
print(counts)


"""