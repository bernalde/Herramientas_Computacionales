import numpy as np


def tribonacci(n,serie):
    m=n+3
    if m<=3:
        return serie
    else:
        new=serie[-1]+serie[-2]+serie[-3]
        serie.append(new)
        tribonacci(n-1,serie)
        return serie

print "Este codigo le permite ver la cantidad que desee de numeros de la serie de tribonacci"
num=input("Cuantos numeros de Tribonacci desea ver (aparte de los unos)? ")
if num<1:
    print "La cantidad de numeros debe ser positiva y mayor a 1"
else:
    serie=[]
    for i in range(3):
        serie.append(1)
    serie=tribonacci(num,serie)
    print serie

