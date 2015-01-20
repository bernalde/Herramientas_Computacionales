#David Bernal 200921359 Taller 11 Herramientas Computacionales


import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import *

gotas=100000 #Numero de gotas totales
size=10 #Tamanho total de la placa

#Parte a.

def myfunkya():
    x=np.zeros(gotas)
    y=np.zeros(gotas)
    for i in range(gotas):
        x[i]=np.random.random()*size
        y[i]=np.random.random()*size
    return x,y


x,y=myfunkya()


#Parte b.

def myfunkyb(a,P):

    N=np.zeros(P)
    for i in range(P):
        x0=np.random.random()*size
        y0=np.random.random()*size
        
        if y0+a>size:
            ymax=y0+a-size
            Y=1
        else:
            ymax=y0+a
            Y=0
        if x0+a>size:
            xmax=x0+a-size
            X=1
        else:
            xmax=x0+a
            X=0

        if (X==0)&(Y==0):
            for j in range(len(x)):
                if (x0<x[j]<xmax)&(y0<y[j]<ymax):
                    N[i]+=1
        if (X==1)&(Y==0):
            for j in range(len(x)):
                if ((x0<x[j]<size)|(0<x[j]<xmax))&(y0<y[j]<ymax):
                    N[i]+=1
        if (X==0)&(Y==1):
            for j in range(len(x)):
                if (x0<x[j]<xmax)&((y0<y[j]<size)|(0<y[j]<ymax)):
                    N[i]+=1
        if (X==1)&(Y==1):
            for j in range(len(x)):
                if ((x0<x[j]<size)|(0<x[j]<xmax))&((y0<y[j]<size)|(0<y[j]<ymax)):
                    N[i]+=1

    return N


a=input("Ingrese un valor de lado 'a' de area cuadrada menor a 10: ")
while a >=10:
    a=input("Ingrese un valor de lado 'a' de area cuadrada menor a 10: ")
P=input("Ingrese el valor de mediciones de gotas en el area de a*a: ")
N=myfunkyb(a,P)

mu=a*a*(gotas/(size*size))
k=np.arange(min(N),max(N))
poisson=poisson.pmf(k,mu)

plt.hist(N,bins=len(k)/10,normed=True,label='Distribucion obtenida')
plt.plot(k,poisson,label='Ajuste de Poisson')
plt.title('Histograma para gotas en areas a*a')
plt.legend()
plt.xlabel('Numero de gotas en area a*a')
plt.ylabel('Frecuencia normalizada')
plt.grid()
plt.show()

print "Puede notarse como se distribuyen Poisson las mediciones"
