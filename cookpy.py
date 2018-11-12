import numpy as np 
import csv

def calEuclidDis(vector):
   # if(not isinstance(vector, list)):
    #    raise TypeError("function calEuclidDis needs a parameter of list or numpy array")
    
    # vector = np.array(vector)[0]
    # print("vector")
    # print(vector)
    sum = 0
    for x in vector:
        sum += (x**2)
    
    return np.sqrt(sum)


class TopsisMatrix(object):

    def __init__(self,data, numObj=0, numCrt=0, mode="default"):
        
        ''' number of object needed to be evaluate '''
        self.numObj = numObj 
        
        ''' number of Criteria needed to be evaluate'''
        self.numCrt = numCrt

        ''' Topsis: Evaluation Matrix '''
        self.topMat = 0
        self.topNaMat = []

        ''' Formulation Matrix '''
        self.fotMat = 0

        ''' Weight Formulation Matrix '''
        self.wgtMat = 0

        ''' weight of each criteria '''
        self.weight = []

        ''' Formulate Matrix need to be evalutate '''
        self.ndUpdate = True  

        if(mode == "kname"):
            self.kname = data
        elif(mode == "all"):
            self.kname = data[0]
            data.pop(0)
            self.push_back(data)
        else:
            ''' init org data '''
            self.push_back(data)

    ''' add another array object to evaulate'''
    def __push_back_list(self, data):
        if(isinstance(data, list)):
            self.topNaMat.append(np.array(data))


    ''' add another object(s) to evaluate'''
    def push_back(self, data):

        if(isinstance(data, list)):
            self.ndUpdate = True
            if(isinstance(data[0], list)):
                for adata in data:
                    self.__push_back_list(adata)
            else:
                self.topNaMat.append(np.array(data))

        elif(isinstance(data, np.array)):
            self.ndUpdate = True
            self.topNaMat.append(data)

        elif(isinstance(data, TopsisMatrix)):
            self.ndUpdate = True
            for adata  in data.topNaMat:
                self.topNaMat.append(adata)
        else:
            raise TypeError()
        
        self.genEvaMat()

    ''' generate Evaluation Matrix '''
    def genEvaMat(self):
        if self.ndUpdate :
            self.topMat = np.array(self.topNaMat)
            self.ndUpdate = False
        return  self.topMat
        

    ''' formulate matrix '''
    def genFotMat(self):   
        self.fotMat = self.topNaMat
        
        
        for obj in self.fotMat.__len__:
            base = calEuclidDis(obj)
            print("base: "+str(base))


        return self.fotMat
    ''' generate weight formulate matrix'''
    def genWgtMat(self):
        self.wgtMat = self.fotMat
        
        for obj in self.wgtMat:
            idx = 0
            for crit in obj:
                crit *= self.weight[idx]
                idx += 1
        
        return self.wgtMat

    def run(self):
        print(self.genEvaMat())
        print("genEvaMat Comp")
        print(self.genFotMat())
        print("genFotMat Comp")
       # print(self.genWgtMat())
       # print("genWgtMat Comp")

def main():
    filename = "./data/dataset.csv"
    with open(filename) as f:
        Reader = csv.reader(f)
        dataset = list(Reader)
        print(dataset)
        dataset = [[1,90,1000,110,200,60,1,1,2,100],
                    [1,60,900,50,800,150,2,2,10,700],
                    [2,30,1500,120,100,40,2,3,3,50],
                    [3,45,1200,90,150,100,1,4,5,120]]
        MaoMatrix = TopsisMatrix(data=dataset, mode="all")
        return MaoMatrix

if __name__ == "__main__":
    MaoMatrix = main()
    MaoMatrix.run()
        
        
