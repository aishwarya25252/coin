import random
import numpy as np
import pandas as pd
from Kmeans import *


def cluster(data, k, mapindex, tempindex):
    index = data.index
    columns = data.columns
    matrix = data.to_numpy()
    centroids = np.random.randn(k, len(index))
    assignedCluster, centroids = kmeans(matrix.T, centroids)
    l=data.columns
    m = np.zeros(l,l)
    for i in range(l):
        for j in range(l):
            if assignedCluster[i] == assignedCluster[j]:
                m[mapindex[tempindex[i]]][mapindex[tempindex[j]]] = 1
    return m


def resample(data):
    q = list(data.columns)
    random.shuffle(q)
    d = data.loc[data.index, q]
    tempindex = dict(zip(list(range(len(q))), q))
    return d, tempindex


def consensous(M):
    consenmatrix = np.zeros(M[0].shape)
    for m in M:
        consenmatrix = np.add(consenmatrix, m)
    consenmatrix = np.divide(consenmatrix, len(M))
    return consenmatrix


def partition(data, bK, mK):
    pass


def PAC(m):
    pacscore = 0
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if (m[i][j] < 0.9) and (m[i][j] > 0.1):
                pacscore = pacscore + 1
    return pacscore


def bestK(cM, K):
    # (PAC), defined as the fraction of sample pairs with consensus
    # index values falling in the intermediate sub-interval (x1, x2) ∈ [0, 1] (Methods).
    # A low value of PAC indicates a flat middle segment,
    # allowing inference of the optimal K by the lowest PAC.
    smallPACscore = PAC(cM[0])
    optimK = K[0]
    optimM = cM[0]
    for i in range(1, len(K)):
        PACscore = PAC(cM[i])
        if PACscore < smallPACscore:
            smallPACscore = PACscore
            optimK = K[i]
            optimM = cM[i]
    return optimK, optimM


def process(data, gset):
    pass


def clustering(data, H, K, gset):
    cM = []
    newdata, mapindex = process(data, gset)
    for k in K:
        M = []
        for h in range(H):
            d, tempindex = resample(newdata)
            m = cluster(d, k, mapindex, tempindex)
            M.append(m)
        cM.append(consensous(M))
    bK, mK = bestK(cM, K)
    p = partition(data, bK, mK)
    return p
