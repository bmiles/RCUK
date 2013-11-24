#
# Use the corpus from project_topics_corpus.py to build topics.
#
# Based on http://radimrehurek.com/gensim/tut2.html
#
import logging
from os import environ
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# load data from project_topics_corpus.py
dictionary = corpora.Dictionary.load('project_topics_corpus.dict')
corpus = corpora.MmCorpus('project_topics_corpus.mm')
print corpus

# initialize the model
tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

# initialize an LSI transformation
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=200)

with open('project_topics_corpus_topics.txt', 'wb') as f:
  f.write(str(lsi.show_topics(num_topics=200, num_words=10, formatted=False)))
  f.write('\n')

# create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
corpus_lsi = lsi[corpus_tfidf]
with open('project_topics_corpus_docs.txt', 'wb') as f:
  for doc in corpus_lsi:
    f.write(str(doc))
    f.write('\n')
