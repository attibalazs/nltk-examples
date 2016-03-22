import nltk
import re
import pprint


def main():
    IN = re.compile(r'.*\bin\b(?!\b.+ing)')
    for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
        for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern=IN):
            print nltk.sem.relextract.rtuple(rel)

if __name__ == "__main__":
    main()
