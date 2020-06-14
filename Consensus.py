import random
import numpy as np
import pandas as pd
from Kmeans import *


def cluster (data , k) :
    index=data.index
    columns=data.columns
    matrix=data.to_numpy()
    centroids=np.random.randn(k,len(index))
    assignedCluster, centroids =kmeans(matrix.T, centroids)
    l=len(columns)
    m=np.zeros(l,l)
    for i in range(l):
        for j in range(l):
            if assignedCluster[i]==assignedCluster[j]:
                m[i][j]=1
    d=pd.DataFrame(m,columns=columns,index=columns)
    return d


def resample(data, gset):
    g = set(gset)
    ag = set(data.index)
    ni = list(g.intersection(ag))
    c = list(data.columns)
    random.shuffle(c)
    d = data.loc[ni, c]
    return d


def consensous(M):
    pass

def partition(data, bK, mK):
    pass

def bestK(cM, K):
    #(PAC), defined as the fraction of sample pairs with consensus
    # index values falling in the intermediate sub-interval (x1, x2) ∈ [0, 1] (Methods).
    # A low value of PAC indicates a flat middle segment,
    # allowing inference of the optimal K by the lowest PAC.
    pass


def clustering(data, H, K, gset):
    cM = []
    for k in K:
        M = []
        for h in range(H):
            d = resample(data, gset)
            m = cluster(d, k)
            M.append(m)
        cM.append(consensous(M))
    bK, mK = bestK(cM, K)
    p = partition(data, bK, mK)
    return p
