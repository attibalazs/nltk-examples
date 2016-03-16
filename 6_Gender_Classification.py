import nltk
import random

def gender_features(word):
    return {'suffix1': word[-1:], 'suffix2': word[-2:], 'suffix2': word[-3:]}

def main():
    from nltk.corpus import names
    names = ([(name, 'male') for name in names.words('male.txt')] +
        [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(names)
    train_names = names[1500:]
    devtest_names = names[500:1500]
    test_names = names[:500]

    train_set = [(gender_features(n), g) for (n,g) in train_names]
    devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]

    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print classifier.classify(gender_features('Neo'))
    print classifier.classify(gender_features('Trinity'))
    print 'attila:', classifier.classify(gender_features('Attila'))
    print classifier.classify(gender_features('Bori'))
    print 'andy:', classifier.classify(gender_features('Andy'))
    print 'dom:', classifier.classify(gender_features('Dom'))
    print 'monica:', classifier.classify(gender_features('Monica'))

    print "accuracy:", nltk.classify.accuracy(classifier, devtest_set)
    print classifier.show_most_informative_features(5)

    errors = []
    for (name, tag) in devtest_names:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))
    for (tag, guess, name) in sorted(errors): # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

if __name__ == "__main__":
    main()