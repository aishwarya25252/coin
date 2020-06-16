from Consensus import *


def pairing(clustermatrix, clustermap):
    
    pass


def network(datasets,H,K,gset):
    datalist=[]
    clustermap={}
    f=0
    for i in range(len(datasets)):
        datalist.append(clustering(datasets[i], H, K, gset))
    for i in range(len(datalist)):
        for j in range(len(datalist[i].clusters)):
            clustermap[f]=datalist[i].clusters[j]
            f=f+1
    clustermatrix=np.zeros([f,f])
    pairing(clustermatrix,clustermap)


    return clusterpairs
