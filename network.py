from Consensus import *

def comparesetmaker(data1,data2):
    compareset=list(set(data1.index)&set(data2.index))
    return compareset


def pearsoncorelation(compareset, centroidmatrix, cluster):
    labels=cluster.labels
    data=cluster.parent.data
    modifydata=data.loc[compareset,labels]
    matrix = modifydata.to_numpy()
    assign = {}
    avg = {}
    for j in range(centroidmatrix.shape[0]):
        assign[j] = 0
        avg[j] = 0
    for i in range(matrix.shape[1]):
        corrcoef=np.corrcoef(matrix.T[i],centroidmatrix[0])[1][0]
        p=0
        for j in range(centroidmatrix.shape[0]):
            temp=np.corrcoef(matrix.T[i],centroidmatrix[j])[1][0]
            if temp>corrcoef :
                p=j
                corrcoef=temp

        assign[p]= assign[p]+1
        avg[p]=avg[p]+corrcoef
    n=0
    v=assign[0]
    for j in range(centroidmatrix.shape[0]):
        if assign[j]>v :
            n=j
    if assign[n]==0:
        return n,0.0
    nmean=avg[n]/assign[n]
    return n,nmean


def pairing(meancorelationmatrix,clustermatrix, clustermap, datalist):
    for i in range(len(datalist)-1):
        for j in range(i+1,len(datalist)):
            compareset = comparesetmaker(datalist[i].data, datalist[j].data)
            centroidmatrix=np.zeros([len(datalist[i].clusters),len(compareset)])
            for a in range(len(datalist[i].clusters)):
                centroidmatrix[a]=datalist[i].clusters[a].centroid(compareset)
            for a in range(len(datalist[j].clusters)):
                temp,avg=pearsoncorelation(compareset,centroidmatrix,datalist[j].clusters[a])
                n=datalist[i].clusters[temp].index
                m=datalist[j].clusters[a].index
                clustermatrix[n][m]=1
                meancorelationmatrix[n][m]=avg
    return


def network(datasets,H,K,gset):
    datalist=[]
    clustermap={}
    f=0
    for i in range(len(datasets)):
        datalist.append(clustering(datasets[i].T, H, K, gset))
    for i in range(len(datalist)):
        for j in range(len(datalist[i].clusters)):
            clustermap[f]=datalist[i].clusters[j]
            datalist[i].clusters[j].index=f
            f=f+1
    clustermatrix=np.zeros([f,f])
    meancorelationmatrix=np.zeros([f,f])
    pairing(meancorelationmatrix,clustermatrix,clustermap,datalist)

    return clustermatrix , meancorelationmatrix , clustermap
