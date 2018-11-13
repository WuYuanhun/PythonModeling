import csv

fileName = "./data/RollerCoasterData.csv"
funcList = []
bookS = []

def getRidOfName():
    book = {}
    fileName = "./data/RollerCoasterData.csv"
    objName = []
    with open(fileName) as f:
        reader = csv.reader(f)
        keywords = list(reader)

        kname = keywords.pop(0)
        kname.pop(0)
        for x in kname:
            x = x.replace('Number of','').replace(' ','')
        
        bookS.append([])
        bookS.append([] for i in keywords)
        for x in keywords:
            #x[0] = x[0].replace(' ','_')
            if x[0] in book.keys():
                book[x[0]] += 1
                x[0] += ("_" + str(book[x[0]]-1))
            else:
                book[x[0]] = 0
            
            for i in range(1,len(x)):
                if(x[i]==""):
                    x[i] = 0.0
                else:
                    x[i] = float(x[i])
                # else:
                #     if x[i] in bookS[i].keys():
                #         x[i] = bookS[i][x[i]] + 1
                #         bookS[i]    
            objName.append(x.pop(0))

        objName.pop(0)  
        keywords.insert(0,kname)  

        return (keywords,objName)

if __name__ == '__main__':
    # with open(fileName) as f:
    #     reader = csv.reader(f)
    #     keywords = list(reader)[0]
    #     keywords.pop(0)
    #     print(keywords)
    print(getRidOfName()[0])