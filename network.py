from Consensus import *


def findparmcalculate(data1,data2):

    pass


def pairing(nnfractionmatrix,meancorelationmatrix,clustermatrix, clustermap, datalist):
    for i in range(len(datalist)-1):
        for j in range(i+1,len(datalist)):
            m,n,nnf,mpc=findparmcalculate(datalist[i],datalist[j])
            clustermatrix[m][n]=1
            clustermatrix[n][m]=1
            nnfractionmatrix[m][n]=nnf
            nnfractionmatrix[n][m]=nnf
            meancorelationmatrix[m][n]=mpc
            meancorelationmatrix[n][m]=mpc
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
            datalist[i].clusters[j].index=f
            f=f+1
    clustermatrix=np.zeros([f,f])
    nnfractionmatrix=np.zeros([f,f])
    meancorelationmatrix=np.zeros([f,f])
    pairing(nnfractionmatrix,meancorelationmatrix,clustermatrix,clustermap,datalist)
    edging()

    return clusterpairs
