#
# Classify organisations into either academic organisations or private
# organisations.
#
# Input:
#   train_jlm_1.csv is the output from classify_organisations.rb with an extra
#   column added that contains the manual classification into 'Academic' or
#   something else.
#  
#   organisations.csv is the full list of organisations from
#   classify_organisations.rb
# 
# Output:
#   classify_organisations.csv: OrganisationId and probability that it's NOT an
#   academic institution
#
import csv
import numpy as np
from nltk.probability import FreqDist
from nltk.classify import SklearnClassifier
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

pipeline = [('tfidf', TfidfTransformer()),
            ('chi2', SelectKBest(chi2, k=20)),
            ('nb', MultinomialNB())]
classif = SklearnClassifier(Pipeline(pipeline))

# just break on gaps -- note that this doesn't filter out punctuation
tokenizer = RegexpTokenizer('[\w\d]+')

training_set = []
with open('train_jlm.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != 'OrganisationId': # header
            words = tokenizer.tokenize(row[1])
            if row[4] == 'Academic':
                training_set.append((words, 'academic'))
            else:
                training_set.append((words, 'private'))

classif.train([(FreqDist(words), label) for (words, label) in training_set])
training_set_classification = classif.batch_classify(
    [FreqDist(words) for (words, label) in training_set])

print "training set score:", sum([training_set[i][1] == training_set_classification[i] for i in range(len(training_set))]), '/', len(training_set)

training_set_prob_classification = classif.batch_prob_classify(
    [FreqDist(words) for (words, label) in training_set])

full_set = []
with open('organisations.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != 'OrganisationId': # header
            organisation_ids = row[0]
            words = tokenizer.tokenize(row[1])
            full_set.append((organisation_ids, words))

full_set_prob_classification = classif.batch_prob_classify(
    [FreqDist(words) for (organisation_ids, words) in full_set])

with open('classify_organisations.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['OrganisationId','ProbabilityPrivate'])
    for i in range(0, len(full_set)):
        writer.writerow([full_set[i][0]] +
            [full_set_prob_classification[i].prob('private')])
