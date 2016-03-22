# Error with the decisiontreeclassifier

import nltk
from nltk.corpus import brown
from nltk.classify import decisiontree

def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
    return features


def main():
    suffix_fdist = nltk.FreqDist()
    for word in brown.words():
        word = word.lower()
        suffix_fdist[word[-1:]] += 1
        suffix_fdist[word[-2:]] += 1
        suffix_fdist[word[-3:]] += 1
    global common_suffixes
    common_suffixes = suffix_fdist.keys()[:100]
    print common_suffixes

    tagged_words = brown.tagged_words(categories='news')
    featuresets = [(pos_features(n), g) for (n, g) in tagged_words]

    size = int(len(featuresets) * 0.001)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = decisiontree.DecisionTreeClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)

    classifier.classify(pos_features('cats'))

    print classifier.pseudocode(depth=4)

if __name__ == "__main__":
    main()
