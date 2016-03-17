import nltk


def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i+1][0].isupper(),
            'prevword': tokens[i-1].lower(),
            'punct':tokens[i],
            'prev-word-is-one-char': len(tokens[i-1]) == 1}


def main():
    sents = nltk.corpus.treebank_raw.sents()
    tokens = []
    boundaries = set()
    offset = 0
    for sent in sents:
        tokens.extend(sent)
        offset += len(sent)
        boundaries.add(offset-1)
    featuresets = []
    for i in range(1, len(tokens) - 1):
        if tokens[i] in '.?!':
            featuresets.append((punct_features(tokens, i), (i in boundaries)))

    size = int(len(featuresets)*0.1)
    print size
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)


if __name__ == "__main__":
    main()
