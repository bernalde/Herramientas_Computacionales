#David Bernal 200921359 Taller 4 Herramientas Computacionales

number=input('Por favor ingrese su numero magico: ')


print "Los multiplos de "+str(number)+" entre 1 y 1000 son:"

mult=0;
i=1;
suma=0;
resp=[];
while (mult+number)<1000:
    mult=number*i;
    i=i+1;
    resp.append(str(mult));
    suma=suma+mult;

print ' '.join((resp))
print "Su suma es: "+str(suma)


