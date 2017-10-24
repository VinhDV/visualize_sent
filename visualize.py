import sys
import codecs
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

from sklearn.manifold import TSNE
from joblib import Parallel, delayed


w2v = defaultdict()
def add_w2v(line):
    global w2v
    a = line.replace('\n', '').split(' ')
    voc = a[0]
    vec = a[1:51]
    if len(vec) == 50:
        vec = np.loadtxt(vec)
        print voc
        w2v[voc] = vec


def load_embeddings(file_name):
    global w2v
    with codecs.open(file_name, 'r', 'utf-8') as f_in:
        lines = f_in.readlines()
        print 'start joblib'
        Parallel(n_jobs=20, backend="threading")(delayed(add_w2v)(line) for line in lines)
        print 'read done'
        print 'vocabulary size:', len(w2v.keys())

embeddings_file = 'w2v_vectors.txt'
load_embeddings(embeddings_file)

count = 0
vocabulary = []
wv = []
common_word = codecs.open('common_word.txt', 'r', 'utf-8').readlines()
for line in common_word:
    if count%1 == 0:
        word = line.strip('\n').replace(' ', '_')
        if word in w2v.keys():
            vocabulary.append(word)
            wv.append(w2v[word])
        else:
            count -= 1
    count += 1


import pickle
pickle.dump(wv,open('wv2.pkl','w'), protocol=0)
a = codecs.open('voc2.txt', 'w', encoding='utf-8' )
for word in vocabulary:
    a.write(word + '\n')
a.close()


# print 'tsne'
# tsne = TSNE(n_components=2, random_state=0, verbose=True)
# np.set_printoptions(suppress=True)
#
# Y = tsne.fit_transform(wv)
#
# plt.scatter(Y[:, 0], Y[:, 1])
# for label, x, y in zip(vocabulary, Y[:, 0], Y[:, 1]):
#     plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
# plt.show()