from Consensus import *


def pairing(dataset1, dataset2):
    pass


def edgeassign(clusterpairs):
    pass


def network(datasets,H,K,gset):
    clusterset=[]
    for i in range(len(datasets)):
        clusterset.append(clustering(datasets[i], H, K, gset))
    clusterpairs=[]
    for i in range(len(clusterset)-1):
        for j in range(i+1,len(clusterset)):
            clusterpairs.append(pairing(clusterset[i],clusterset[j]))
    for i in range(len(clusterpairs)):
        edgeassign(clusterpairs)
    return clusterpairs
