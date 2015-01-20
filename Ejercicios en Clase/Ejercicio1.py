import numpy as np



data=np.loadtxt("edadesvsalturas.txt")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print factorial(3)
"""


def square(x):
    print x**2

def convert(x,y):
    if y==0:
        return x*1.16
    elif y==1:
        return x*2.54
    elif y==2:
        return x*1000
    else:
        print "Debe escribir un numero entre 1 y 3"

x=input("Escriba la cantidad que desea convertir ")
y=input("Escriba el tipo de conversion que va a realizar (1 para millas a km, 2 para pulgadas a cm o 3 de litros a cm^3) ")
    

print convert(x,y-1)




print type(data), np.shape(data)
x=data[:,0]
y=data[:,1]

f=open("edadesaltos.txt","w")
for i in range(len(x)):
    if y[i]>1.7:
        f.write("%f \n" %(x[i]))
f.close

index=np.where(y>1.70)
print x[index], index


f=open("multiplicacion.txt","w")
for i in range(len(x)):
    f.write("%f %f \n" %(x[i], y[i]))
f.close
"""
