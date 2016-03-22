# Extract named entities like Organisations, Locations from text.

import nltk, re, pprint

def ie_preprocess(document):
    sents = nltk.sent_tokenize(document)
    sents = [nltk.word_tokenize(sent) for sent in sents]
    sents = [nltk.pos_tag(sent) for sent in sents]
    return sents

def main():
    sent = nltk.corpus.treebank.tagged_sents()[22]
    print "sent (nltk):", sent
    #print nltk.ne_chunk(sent, binary=True)
    #print nltk.ne_chunk(sent)

    sent = ie_preprocess("""Injured personnel consisting of six Schlum employees were immediately transported
                        to nearby hospitals and most of them (were)
                        discharged after having received treatment""")
    print sent
    print nltk.ne_chunk(sent[0])

if __name__ == "__main__":
    main()
