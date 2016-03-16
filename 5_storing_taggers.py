import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents)*0.9)
print "size:", size
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
#t3 = nltk.TrigramTagger(train_sents, backoff=t2)
#print "precision:", t3.evaluate(test_sents)

#save tagger
#from cPickle import dump
#output = open('t2.pkl','wb')
#dump(t2,output,-1)
#output.close()

cfd = nltk.ConditionalFreqDist(
    ((x[1], y[1], z[0]), z[1])
    for sent in brown_tagged_sents
    for x, y, z in nltk.trigrams(sent))

ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
print "ambiguous percent:", sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N()

test_tags = [tag for sent in brown.sents(categories='editorial')
             for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
cm = nltk.ConfusionMatrix(gold_tags, test_tags)

f = open('confusion_matrix.txt','w')
f.write(cm.pretty_format())
f.close()