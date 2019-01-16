# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence, TaggedDocument
from gensim.models import Doc2Vec
import pandas as pd
# numpy
import numpy

# shuffle
from random import shuffle

# logging
import logging
import os.path
import sys
import cloudpickle as pickle

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))


data = pd.read_csv('train_350000_10_doc2vec.csv', sep = '\t')
print("******************")
print(len(data))
sentences= []
for elem in data.iterrows():
    tup = elem[1]
    ids = tup['Tag'].split(" ")
    a = str(tup['combined']).split(' ')
    t = [x.replace('}', '').replace('(', '').replace('.', ' ').replace(')', '').replace('{', '').replace(';', '').replace('-', '').replace('_', ' ') for x in a if(x != '')]
    sentences.append(LabeledSentence(t, ids))
    if(len(sentences)%500 == 0):
    	print(len(sentences))

model = Doc2Vec(sentences, min_count=1, window=100, size=50, workers=7, iter = 20)
print(sentences[1:4])
print('vocab done*********************')
model.train(sentences, epochs=model.iter, total_examples=model.corpus_count)
model.save('./new_imdb_withoutID_medium.d2v')

	# MODEL PARAMETERS


