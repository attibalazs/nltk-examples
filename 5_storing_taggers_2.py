from cPickle import load

input = open('t2.pkl','rb')
tagger = load(input)
input.close()

text = """the board`s action shows that free enterprise
    is up against in our ocplex maze of regulartory laws."""
tokens = text.split()
print tagger.tag(tokens)

