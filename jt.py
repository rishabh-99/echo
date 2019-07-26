from numpy import genfromtxt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
point=[]
point1=[]
# f1=open("user1.csv","r")
# for lines in f1:
#     h=lines.find("ax,ay,az,gx,gy,gz,heartRate,timestamp")
#     if h==0:
#         continue
    
acm_data = genfromtxt("user1.csv", delimiter=',', names=["ax","ay","az","gx","gy","gz","hr","timestamp"])
x = acm_data["ax"]
y = acm_data["ay"]
z = acm_data["az"]
x1 = acm_data["gx"]
y1 = acm_data["gy"]
z1 = acm_data["gz"]
hr = acm_data["hr"]
ts = acm_data["timestamp"]
time=[]
j=0
for i in ts:
    if j!=0:
        time.append(i)
    j=j+1
print(time)
j=0
lx=[]
gx=[]
ly=[]
gy=[]
lz=[]
gz=[]
lh=[]
j=0
for i in x:
    if j!=0:
        lx.append(i)
    j=j+1
j=0
for i in y:
    if j!=0:
        ly.append(i)
    j=j+1
j=0
for i in z:
    if j!=0:
        lz.append(i)
    j=j+1
j=0
for i in x1:
    if j!=0:
        gx.append(i)
    j=j+1
j=0
for i in y1:
    if j!=0:
        gy.append(i)
    j=j+1
j=0
for i in z1:
    if j!=0:
        gz.append(i)
    j=j+1
j=0
for i in hr:
    if j!=0:
        lh .append(i)
    j=j+1
j=0
for i in lx:
    point.append(math.sqrt(pow(lx[j],2)+pow(ly[j],2)+pow(lz[j],2)))	
    j=j+1
j=0
for i in lx:
    point1.append(math.sqrt(pow(gx[j],2)+pow(gy[j],2)+pow(gz[j],2)))	
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