import sys
import os
import nltk
import sklearn
import sklearn.cluster
import numpy as np

from C2char import getListdir


def getText(filename):
    f = open(filename, 'r', encoding='UTF-8')
    return f.read()


def getVector():
    texts = []
    d = './News_C/'
    os.chdir(d)
    fa = getListdir(os)
    for i in range(0, len(fa)):
        texts.append(" ".join(nltk.word_tokenize(getText(fa[i]))))

    countVector = sklearn.feature_extraction.text.CountVectorizer()
    transformer = sklearn.feature_extraction.text.TfidfTransformer()

    tfidf_matrix = transformer.fit_transform(countVector.fit_transform(texts))

    ch_max = 0
    km = sklearn.cluster.KMeans(n_clusters=20)
    y_pred = km.fit_predict(tfidf_matrix)

    print("每个类的代表文档为：\n（按序号排，第一个参数为文档与类中心的余弦距离，第二个参数为文档名字）")
    print(getDistance(tfidf_matrix.toarray(), y_pred, km.cluster_centers_))

    return y_pred


def get_max(vec):
    l = []
    a1 = a2 = a3 = 0, 1, 2
    for i in range(20):
        l.append((len(list(np.where(vec == i)[0])), i))
    l.sort(key=lambda x: x[0], reverse=True)
    print("最大的三个类为：\n第一个参数为类中文档数，第二个参数为类编号，以1开始")
    return l[:3]


def getDistance(vec, label, c):
    dis = []

    for i in range(0, len(c)):
        dis_max = 0
        for j in range(0, len(label)):
            if label[j] == i:
                idis = sklearn.metrics.pairwise.cosine_similarity(
                    vec[j].reshape(1, -1), c[i].reshape(1, -1))
                if idis > dis_max:
                    dis_max = idis
                    dis_max_i = j
        dis.append((dis_max, dis_max_i))
    return dis


def main():

    print(get_max(getVector()))


if __name__ == '__main__':
    main()
