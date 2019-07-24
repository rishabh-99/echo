from numpy import genfromtxt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
point=[]

acm_data = genfromtxt("sample_data.csv", delimiter=',', names="acc_x, acc_y, acc_z")
x = acm_data["acc_x"]
y = acm_data["acc_y"]
z = acm_data["acc_z"]
lx=[]
ly=[]
lz=[]
for i in x:
	lx.append(i)
for i in y:
	ly.append(i)
for i in z:
	lz.append(i)
j=0
for i in x:
	point.append(math.sqrt(lx[j]*lx[j]+ly[j]*ly[j]+lz[j]*ly[j]))	
	j=j+1
i=0.00
l=[]
temp=[]
while i<j:
	l.append(i)
	i=i+1.00
plt.plot(l,point)
plt.show()
		

