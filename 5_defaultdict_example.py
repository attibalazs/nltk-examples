import nltk

def main():
    alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
    vocab = nltk.FreqDist(alice)
    v1000 = list(vocab)[:1000]
    mapping = nltk.defaultdict(lambda: 'UNK')
    for v in v1000:
        mapping[v] = v
    alice2 = [mapping[v] for v in alice]
    print alice2[:100]
    print len(set(alice2))
if __name__ == "__main__":
    main()