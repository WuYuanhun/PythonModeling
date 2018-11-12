import numpy as np 
import matplotlib.pyplot as plt 
import extNumpy as enp 

x = [1,2,3,4,5]
y = [2.5, 3.51, 6.45, 7.52, 6.47]

z1 = np.polyfit(x, y, 3)
p1 = np.poly1d(z1)

print(z1)
print(p1)

# X = np.linspace(0,6,1000)
# Y = enp.generateY(X,z1)
X,Y = enp.generateXY(x,z1)

plt.plot(X,Y)
plt.scatter(x,y,marker='+',color='r',label='1')
plt.show() 

