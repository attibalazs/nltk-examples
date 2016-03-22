# coding=utf-8
import nltk
from nltk.corpus import rte

"""Example 6-7. Recognizing Text Entailment feature extractor: The RTEFeatureExtractor class
    builds a bag of words for both the text and the hypothesis after throwing away some stopwords, then
    calculates overlap and difference."""

def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))

def main():
  # Doesn`t work, crashes with the following error: Resource u'corpora/rte' not found.
  rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[33]
  extractor = nltk.RTEFeatureExtractor(rtepair)
  print extractor.text_words
  print extractor.hyp.words
  print extractor.overlap('word')
  print extractor.overlap('ne')
  print extractor.hyp_extra('ne')

if __name__ == "__main__":
    main()
