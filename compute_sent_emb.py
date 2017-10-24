import numpy as np
import pickle
from gensim.models.keyedvectors import KeyedVectors
wv =KeyedVectors.load_word2vec_format('w2v_vectors.txt', binary=False)
sent_vecs = []
sents = open('processed_zalo.txt').readlines()
for sent in sents:
    sent = sent.strip('\n').split()
    remove = []
    for word in sent:
        if not (word in wv.wv.vocab):
            remove.append(word)
    for rm_word in remove:
        sent.remove(rm_word)
    if len(sent) == 0:
        sent = ['null']
    print(sent)
    sent_vecs.append(np.mean(wv.wv[sent], axis=0))

np.save('sent_matrix', sent_vecs)


