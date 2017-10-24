import sys
import codecs
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

from sklearn.manifold import TSNE
from joblib import Parallel, delayed


import pickle
h = open('wv2.pkl', 'rb')
wv = pickle.load(h)
a = codecs.open('voc2.txt', 'r', encoding='utf-8' ).readlines()
vocabulary = []
for word in a:
    vocabulary.append(word.strip('\n'))

# wv = wv[:100]
# vocabulary = vocabulary[:100]

print 'tsne'
tsne = TSNE(n_components=2, random_state=0, verbose=True)
np.set_printoptions(suppress=True)

Y = tsne.fit_transform(wv)

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 70
fig_size[1] = 70
plt.rcParams["figure.figsize"] = fig_size
plt.scatter(Y[:, 0], Y[:, 1])
for label, x, y in zip(vocabulary, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
plt.savefig('test4png.png', dpi=150)
