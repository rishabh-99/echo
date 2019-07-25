from numpy import genfromtxt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
point=[]
point1=[]
f=open("cleaned.csv","w")
f1=open("palak.csv","r")
for lines in f1:
    h=lines.find("timestamp,accX,accY,accZ,gyrX,gyrY,gyrZ,HR")
    if h==0:
        continue
    h=lines.find(",,,,,,,")
    if h!=-1:
        continue
    f.write(lines)
acm_data = genfromtxt("cleaned.csv", delimiter=',', names=["timestamp","accX", "accY", "accZ","gx","gy","gz","hr"])
x = acm_data["accX"]
y = acm_data["accY"]
z = acm_data["accZ"]
x1 = acm_data["gx"]
y1 = acm_data["gy"]
z1 = acm_data["gz"]
hr = acm_data["hr"]
lx=[]
lx1=[]
ly=[]
ly1=[]
lz=[]
lz1=[]
lh=[]
for i in x:
    lx.append(i)
for i in y:
    ly.append(i)
for i in z:
    lz.append(i)
for i in x1:
    lx1.append(i)
for i in y1:
    ly1.append(i)
for i in z1:
    lz1.append(i)
for i in hr:
    lh.append(i)
j=0
for i in x:
    point.append(math.sqrt(pow(lx[j],2)+pow(ly[j],2)+pow(lz[j],2)))	
    j=j+1
j=0
for i in x:
    point1.append(math.sqrt(pow(lx1[j],2)+pow(ly1[j],2)+pow(lz1[j],2)))	
    j=j+1
i=0.00
l=[]
temp=[]
while i<j:
    l.append(i)
    i=i+1.00
plt.plot(l,point)
plt.plot(l,point1)
plt.plot(l,lh)
plt.show()
