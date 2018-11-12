import numpy as np

def generateY(oArray, ploy1d):
    y = []
    for i in oArray:
        yi = 0 
        for k in ploy1d:
            yi *= i
            yi += k
        y.append(yi)
    return y

def generateXY(oArray, ploy1d):

    maxX = max(oArray)
    minX = min(oArray)
    dif = (maxX - minX)/len(oArray)

    X = np.linspace(minX-2*dif, maxX+2*dif, (len(oArray)+4)*1000)
    return X, generateY(X,ploy1d)

# def polyfit_exp(x, y, deg):
