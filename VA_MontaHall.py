import numpy as np
from random import shuffle

#Retorna un orden aleatorio de la lista
def sort_doors():
    lista = ["goat","goat", "car"]
    
    np.random.shuffle(lista)
    
    return lista

b=sort_doors()
#Retorna un numero aleatorio entre 0,1,2
def choose_door():
    num=[0,1,2]

    a= np.random.choice(num)
    
    return a

c=choose_door()
#Funcion que retorna en que posicion se encuentra una cabra

def reveal_door(lista,choice):
    
    for i in range(len(lista)):
        
        if ( i!=choice)and(lista[i]=="goat"):
            
            lista[i]="GOAT_MONTY"
            
            return lista

#Funcion que finaliza el juego y relaciona si el jugador desea cambiar o no de puerta 
def finish_game(lista,choice,change):
    
    if (change == False):
        
        return lista[choice]

    else :
        #Se tiene el condicional en el caso de que el jugador quiera cambiarse de puerta
        for i in range(len(lista)):
            
            if( i!=choice)and(lista[i]!="GOAT_MONTY"):
                
                return lista[i]

            
        
print b,c
print reveal_door(b,c)
print finish_game(b,c,True)

#Simulacion para diferentes escenarios del juego
lis_true=[]
for i in range (99):

    #Numero de puerta
    a=sort_doors()
    #puerta que elige 
    c=choose_door()
    #Se revela la puerta
    d=reveal_door(a,c)
    
    b=finish_game(d,c,True)
    lis_true.append(b)

lis_false=[]
for i in range (99):
    
    #Numero de puerta
    a=sort_doors()
    #puerta que elige 
    c=choose_door()
    #Se revela la puerta
    d=reveal_door(a,c)
    
    b=finish_game(d,c,False)
    lis_false.append(b)
    
print "lista de True",lis_true
print "lista de false",lis_false


#Se busca saber cual es la probabilidad de ganar un carro cambiando de puerta o no 
win_true=0.0
win_false=0.0

for i in range (len(lis_true)):
    #Probabilidad de ganar cambiando de puerta
    if (lis_true[i]=="car"):
        win_true+=1.0

for i in range (len(lis_false)):
    #Probabilidad de ganar sin cambiar de puerta
    if (lis_false[i]=="car"):
        win_false+=1.0
                
    
prob1= win_true/len(lis_true)
prob2=win_false/len(lis_false)

print "La probabilidad de ganar cambiando de puerta es :", prob1,"La probabilidad de ganar sin cambiar de puerta es:",prob2
