import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import *

## Parte a)

def puntoa():
    x=np.zeros(100000)
    y=np.zeros(100000)
    for i in range(100000):
        x[i]=np.random.random()*10
        y[i]=np.random.random()*10
    #plt.figure(figsize=(8,8))
   # plt.scatter(x,y)
   # plt.xlim([0,10])
   # plt.ylim([0,10])
   # plt.show()

    return x,y

x,y=puntoa()



## Parte b)

def puntob(a,P):

    N=np.zeros(P)

    for i in range(P):
        x0=np.random.random()*10
        y0=np.random.random()*10
        
        if x0+a>10:
            xmax=x0+a-10
            condfrontx=1
        else:
            xmax=x0+a
            condfrontx=0

        if y0+a>10:
            ymax=y0+a-10
            condfronty=1
        else:
            ymax=y0+a
            condfronty=0

        if (condfrontx==1)&(condfronty==1):
            for j in range(len(x)):
                if ((x0<x[j]<10)|(0<x[j]<xmax))&((y0<y[j]<10)|(0<y[j]<ymax)):
                                          N[i]+=1
        if (condfrontx==1)&(condfronty==0):
            for j in range(len(x)):
                if ((x0<x[j]<10)|(0<x[j]<xmax))&(y0<y[j]<ymax):
                                          N[i]+=1

        if (condfrontx==0)&(condfronty==1):
            for j in range(len(x)):
                if (x0<x[j]<xmax)&((y0<y[j]<10)|(0<y[j]<ymax)):
                                          N[i]+=1
        if (condfrontx==0)&(condfronty==0):
            for j in range(len(x)):
                if (x0<x[j]<xmax)&(y0<y[j]<ymax):
                                          N[i]+=1
    return N
            

## Punto c)

a=input("ingrese el valor de a menor a 10")
while a >=10:
    a=input("ingrese el valor de a menor a 10")
P=input("ingrese el valor de P ")

N=puntob(a,P)

mu=a**2*1000
k=np.arange(int(mu-3*mu**0.5),int(mu+3*mu**0.5),1)
poisson=poisson.pmf(k,mu)

plt.figure(figsize=(10,10))
plt.hist(N,bins=20,normed=True)
plt.plot(k,poisson,label='ajuste por Poisson')
plt.title('Histograma para gotas caidas en la zona de dimension a')
plt.legend()
plt.xlabel('Numero de gotas en la zona definida por a')
plt.ylabel('Frecuencia normalizada')
plt.show()

print "Se tiene una distribucion de Poisson"





