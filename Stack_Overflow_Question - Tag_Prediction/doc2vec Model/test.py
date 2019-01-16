import gensim.models as g
import codecs
from gensim import utils
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import os
import numpy as np
import numpy
import pandas as pd


model = g.Doc2Vec.load('./new_imdb_withoutID_medium.d2v')
#print(np.shape(model.docvecs[1]))
tokens = "c# Language Conversion Testing We created tool converts language called P2  language similar assembly think exists Japan  C#  There least hundred modules written P2 want verify conversion C# right How test "
tokens_noise = "c# Property default values using Properties.Settings.Default using  Net 2 normal way store settings  store custom object serialized xml  trying retrieve default value property (but without reseting properties)  use:  ValuationInput valuationInput = (ValuationInput) Settings Default Propertie] DefaultValue;   But seems return string instead ValuationInput throws exception    made quick hack  works fine:  string valuationInputStr = (string)  Settings Default Properties DefaultValue;             XmlSerializer xmlSerializer = new XmlSerializer(typeof(ValuationInput));             ValuationInput valuationInput = (ValuationInput) xmlSerializer Deserialize(new StringReader(valuationInputStr));   But really ugly - use tool define strongly typed setting  want serialize default value  would like read way read current value: ValuationInput valuationInput = Settings Default ValuationInput;"
tokens_new = "asd jefperofj ofeqvjdo qvq[ feoqpf "
tokens_new = "Trip time calculation in relational databases?"
tokens_new = "Is Implicit Arraylist assignment possible?"
tokens_new = "MySQL/Apache Error in PHP MySQL query"
tokens_new = ""
#tokens_new = "javascript css How create Netflix-style iframe"
new_vector = model.infer_vector(tokens)
new_vector2 = model.infer_vector(tokens_noise)
new_vector3 = model.infer_vector(tokens_new)

training = pd.read_csv("test_350000_10_doc2vec.csv", sep="\t")
print(training.columns)
print(len(training))

#vector_list = []
#def get_vectors(data):
#    vector_list.append(model.infer_vector(data))

train_arrays = numpy.zeros((len(training), 50))
train_arrays = []
counter= 0
for string in training.iterrows():
    tup = string[1]
    vec = model.infer_vector(tup['Title'])
    train_arrays.append(vec)
    counter+=1
    if(counter%600 == 0):
        print(counter)

#    train_arrays.append(model.infer_vector(string))
training['vectors'] = train_arrays
training.to_pickle("./newdataframe_test_onlytitle.pkl")
#print(train_arrays)

#training['combined'].apply(lambda s: get_vectors(s))
#sims = model.docvecs.most_similar([new_vector])
#sims2 = model.docvecs.most_similar([new_vector2])
#sims3 = model.docvecs.most_similar([new_vector3])
#print(sims)
#print("*******************************************")
#print(sims2)
#print("*******************************************")
#print(sims3)


#print("*******************************************")
#print("Cosine distance between a stack over flow question and the same question with some added noies")
#cosine_similarity = numpy.dot(new_vector, new_vector2)/(numpy.linalg.norm(new_vector)* numpy.linalg.norm(new_vector2))
#print(cosine_similarity)
#print("*******************************************")
#print("Cosine distance between a stack over flow question and a random set of sentences which have on relation")
#cosine_similarity2 = numpy.dot(new_vector2, new_vector3)/(numpy.linalg.norm(new_vector2)* numpy.linalg.norm(new_vector3))
#print(cosine_similarity2)

