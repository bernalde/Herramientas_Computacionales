import sys
import math
import random

R= float(sys.argv[1])

x=[]
y=[]
z=[]
rf=[]
pasos=0
n=[]

def angulosAleatorios():
 y= random.random()  
 x=2*(3.1415)
 return x*y                           

r=0
xi=0
yi=0
zi=0
while(r<R):

 th=angulosAleatorios()
 ph=angulosAleatorios()
 x1=(math.sin(th))*(math.sin(ph))
 y1=(math.sin(th))*(math.cos(ph))
 z1=(math.cos(th))

 xi+=x1
 yi+=y1
 zi+=z1

 r=math.sqrt((xi*xi)+(yi*yi)+(zi*zi))

 pasos+=1
 x.append(xi)
 y.append(yi)
 z.append(zi)
 rf.append(r)
 n.append(pasos)
 
f=open("Marcha-Aleatoria.dat","w")
for i in range(len(x)):
    f.write(str(x[i])+" "+str(y[i])+" "+str(z[i])+" "+str(rf[i])+" "+str(n[i])+"\n")
f.close

 

    
