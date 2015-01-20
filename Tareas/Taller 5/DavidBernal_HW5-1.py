import numpy as np
from random import randrange

def strtonum(string):
    if string=="Piedra":
        return 1
    elif string=="Papel":
        return 2
    elif string=="Tijera":
        return 3
    elif string=="Spock":
        return 4
    else:
        return "Lagartija"

def numtostr(number):
    if number==1:
        return "Piedra"
    elif number==2:
        return "Papel"
    elif number==3:
        return "Tijera"
    elif number==4:
        return "Spock"
    else:
        return "Lagartija"

def winner(usernum,pcnum):
    if usernum==1:
        if pcnum==1:
            print "Hay empate"
        elif pcnum==2:
            print "El computador gana"
        elif pcnum==3:
            print "El usuario gana"
        elif pcnum==4:
            print "El computador gana"
        else:
            print "El usuario gana"
    elif usernum==2:
        if pcnum==1:
            print "El usuario gana"
        elif pcnum==2:
            print "Hay empate"
        elif pcnum==3:
            print "El computador gana"
        elif pcnum==4:
            print "El usuario gana"
        else:
            print "El computador gana"
    elif usernum==3:
        if pcnum==1:
            print "El computador gana"
        elif pcnum==2:
            print "El usuario gana"
        elif pcnum==3:
            print "Hay empate"
        elif pcnum==4:
            print "El computador gana"
        else:
            print "El usuario gana"
    elif usernum==4:
        if pcnum==1:
            print "El usuario gana"
        elif pcnum==2:
            print "El computador gana"
        elif pcnum==3:
            print "El usuario gana"
        elif pcnum==4:
            print "Hay empate"
        else:
            print "El computador gana"
    else:
        if pcnum==1:
            print "El computador gana"
        elif pcnum==2:
            print "El usuario gana"
        elif pcnum==3:
            print "El computador gana"
        elif pcnum==4:
            print "El usuario gana"
        else:
            print "Hay empate"

print "Este codigo es un juego de usted contra la computadora de piedra, papel, tijera, Spock o lagartija"
user=raw_input("Piedra, Papel, Tijera, Spock o Lagartija? ")
if((user=="Piedra") | (user=="Papel") | (user=="Tijera") | (user=="Spock") | (user=="Lagartija")):
    print "Usuario: "+user
    usernum=strtonum(user)
    pcnum=randrange(1,6)
    pc=numtostr(pcnum)
    print "Computador: "+pc
    winner(usernum,pcnum)
else:
    print "Ustede debe ingresar Piedra, Papel, Tijera, Spock o Lagartija con tal de iniciar el juego"


