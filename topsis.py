from __future__ import division

import csv

import numpy as np

import pandas as pd

import dataInput as dip


def calEuclidDis(vector):
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

        ''' ideal solution '''
        self.idealSolution = []

        if(mode == "kname"):
            self.kname = data
        elif(mode == "all"):
            self.kname = data[0]
            data.pop(0)
            self.push_back(data)
        else:
            self.kname = []
            ''' init org data '''
            self.push_back(data)

    ''' add another array object to evaulate'''
    def __push_back_list(self, data):
        if(isinstance(data, list)):
            self.topNaMat.append(np.array(data,dtype=np.float64))


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
    
    ''' return size of matrix '''
    def sizeM(self):
        self.numObj = len(self.topNaMat)
        self.numCrt = len(self.topNaMat[0])

    ''' return key name '''
    def knameAt(self,idx):
        if not isinstance(idx, int):
            raise TypeError()
        if len(self.kname) <= 0 :
            for i in range(0, self.numCrt):
                self.kname.append("Crit "+str(i))
        if len(self.kname) <= idx:
            raise Exception("Out of Range")
        else:
            return self.kname[idx]

    ''' formulate matrix '''
    def genFotMat(self):   
        self.fotMat = self.topNaMat
        self.sizeM()
        for obj in range(0, self.numCrt):
            base = calEuclidDis([self.topNaMat[x][obj] for x in range(0,self.numObj)])
            print(self.knameAt(obj)+" base: "+str(base))
            for v in range(0,self.numObj):
                self.fotMat[v][obj] /= base
                print(self.fotMat[v][obj],end=' ')
            print()
        return self.fotMat

    ''' generate weight formulate matrix'''
    def genWgtMat(self):
        self.wgtMat = self.fotMat

        if len(self.weight) != self.numCrt:
            self.weight = np.ones(shape=self.numCrt,dtype=np.float64)
        
        for obj in self.wgtMat:
            idx = 0
            for crit in obj:
                crit *= self.weight[idx]
                idx += 1
        
        return self.wgtMat

    def solIdealSolution(self):
        self.idealSolution = []
        for x in range(0,self.numCrt):
            nBig = self.wgtMat[0][x]
            for i in range(0,self.numObj):
                nBig = max(self.wgtMat[i][x],nBig)
            self.idealSolution.append(nBig)

    def readObjName(self,data):
        self.objName = data

    def rank(self):
        self.orgRanking = []
        obj = {}
        for i in range(0,self.numObj):
            obj = {}
            obj["name"] = self.objName[i]
            obj["v"] = sum(self.wgtMat[i])
            #print(obj)
            self.orgRanking.append(obj)

        #print(self.orgRanking) 
        self.ranking = sort(self.orgRanking)

        i=0
        print("Idx  Name          score")
        for x in self.ranking:
            i+=1
            print("%-3d  %-10.10s    "%(i,x["name"])+str(x["v"]))
        return self.ranking

    def run(self):
        print(self.genEvaMat())
        print("genEvaMat Comp")
        print(self.genFotMat())
        print("genFotMat Comp")
        print(self.genWgtMat())
        print("genWgtMat Comp")
        print("---------------")
        self.rank()

def sort(data,reverse=False):
    r = data
    for i in range(0,len(r)-1):
        for j in range(i,len(r)):
            if r[i]["v"] > r[j]["v"]:
                r[i], r[j] = r[j], r[i]
    if reverse:
        r = r.reverse()        
    return r

def store(data,filename="./data/temp.csv",type="default",header=None):
    
    if type=="matrix":
        with open(filename,'w') as f:
            if header is not None:
                for x in header:
                    x +='      '
                    print("%.5s"%x,end='   ')
                    f.write("%.5s   "%x)
                f.write('\n')
                print()
                    
            for obj in data:
                for x in obj:
                   print("%5.3f"%x,end='    ')
                   f.write("%5.3f   "%x)
                print()
                f.write('\n')

def show(data, type, header=None):
    if(type=="array" or type=="list"):
        for x in data:
            print("%.5f"%x,end='   ')
        print()

def max(x, y):
    if x>y:
        return x
    else:
        return y

def main(): # test use
    filename = "./data/dataset.csv"
    with open(filename) as f:
        Reader = csv.reader(f)
        dataset = list(Reader)
        print(dataset)
        dataset = [ ["Year","Angle","Length","Speed","Height","Duration","Material","Type","Inversion","Drop"],
                    [1,90,1000,110,200,60 ,1,1,2 ,100],
                    [1,60,900 ,50 ,800,150,2,2,10,700],
                    [2,30,1500,120,100,40 ,2,3,3 ,50 ],
                    [3,45,1200,90 ,150,100,1,4,5 ,120]]
        tMatrix = TopsisMatrix(data=dataset,mode="all")
        tMatrix.readObjName(["a","b","c","d"])
        return tMatrix

def DEEPmain():
    dataset = dip.getRidOfName()
    tMatrix = TopsisMatrix(data=dataset[0],mode="all")
    tMatrix.readObjName(dataset[1])
    tMatrix.run()
    return tMatrix
    

if __name__ == "__main__":
    # tMatrix = main()
    # tMatrix.run()
    tMatrix = DEEPmain()

