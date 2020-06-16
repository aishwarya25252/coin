class dat :
    def __init__(self,data,newdata,k):
        self.data=data
        self.newdata=newdata
        self.k=k
        self.clusters={}
        for i in range(k):
            self.clusters[i]=[]
        pass