#
# Build the corpus for topic selection.
#
# Based on http://radimrehurek.com/gensim/tut1.html
#
import logging
import csv
from os import environ
from pymongo import MongoClient
from gensim import corpora, models, similarities
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dbname = environ['MONGOLAB_URI'].rsplit('/', 1)[1]
db = MongoClient(environ['MONGOLAB_URI'])[dbname]
projects = db.projects.find()

documents = [(project.get('_id'), project.get('id'), project.get('abstractText')) for project in projects]
print 'got documents'

# need to save the ids for later
with open('project_topics_corpus_ids.csv', 'wb') as f:
  writer = csv.writer(f)
  writer.writerow(['_id','ProjectId'])
  for document in documents:
      writer.writerow([document[0], document[1]])

# but we just need the text for now
documents = [document[2] or '' for document in documents]
      
# remove common words and tokenize
tokenizer = RegexpTokenizer('[\w\d]+')
stoplist = set(stopwords.words('english'))
texts = [[word for word in tokenizer.tokenize(document.lower())
            if word not in stoplist] for document in documents]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word)==1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

# convert to integer representation
print 'dictionarying'
dictionary = corpora.Dictionary(texts)
dictionary.save('project_topics_corpus.dict')
#print dictionary.token2id

# count words
print 'counting'
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('project_topics_corpus.mm', corpus)

