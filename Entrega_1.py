
import math
import sys
# Funcio para contar la cantiad de veces que se repite la subsecuencia en la secuencia
def count(X, Y, m, n):
 
    # caso base 1: si solo un carcater falta
    if m == 1 and n == 1:
        return 1 if (X[0] == Y[0]) else 0
 
    # caso base 2: Si ya se recorrio toda la secuencia X
    if m == 0:
        return 0
 
    # Caso base 3: Si ya se recorrió toda la subsecucnia Y, se encontró la subsecuencia
    if n == 0:
        return 1
 
    #Si la longitud de la subsecuencia es mayor a la secuencia, no se puede encontrar
    if n > m:
        return 0
 
    # Si el ultimo caracter de la secuencia es igual al ultimo de la subsecuencia, se puede encontrar
    return (count(X, Y, m - 1, n - 1) if X[m - 1] == Y[n - 1] else 0)\
        + count(X, Y, m - 1, n)
 




#Funcion grande
def find_secuence(x,y,m):
    m=int(m)
    x_list = list(x.strip(" "))
    y_list = list(y.strip(" "))
    primeramitad = x_list[:math.ceil(len(x_list)//2)]
    segundamitad = x_list[math.floor(len(x_list)//2):]
    y_first = y_list[0]
    y_second = y_list[1]
    lista_correcta = changing (primeramitad, segundamitad, y_first, y_second,m)
    string_correcto = "".join(lista_correcta)
    cantidad_subsecuencias = count(string_correcto,y,len(string_correcto),len(y))
    return cantidad_subsecuencias

        


#Funcion recursuva, cambia la letra
def changing (primeramitad, segundamitad, y_first, y_second,m):
    rep_first = primeramitad.count(y_first)
    rep_second = segundamitad.count(y_second)
    if m <= 0:
        return primeramitad+segundamitad
    elif rep_first == len ( primeramitad ) and rep_second == len ( segundamitad ):
        return primeramitad+segundamitad 
    #Si el numero de x es igual al numero de t y no está perfecto (xxatta)
    if rep_first == rep_second and rep_first <  len(primeramitad):
        #se busca en ambas mitades
        i = to_change(primeramitad, y_first,y_second,1)
        j = to_change(segundamitad, y_second,y_first,2)
        #se cambia la letra
        segundamitad[j] = y_second 
        m = m-1
        if m <= 0:
            return primeramitad+segundamitad
        else:
            primeramitad[i] = y_first
            m = m-1
        #se llama a la funcion recursiva
        changing(primeramitad, segundamitad, y_first, y_second,m)
    #Si el numero de x es igual al numero de t y no está perfecto solo en la segunda mitad (xxxattt)
    elif rep_first == rep_second and rep_second < len(segundamitad):
    #se busca solo en la segunda mitad
        j = to_change(segundamitad, y_second,y_first,2)
        #se cambia la letra
        segundamitad[j] = y_second
        m = m-1
        #se llama a la funcion recursiva
        changing(primeramitad, segundamitad, y_first, y_second,m)
    #Si el numero de x es menor al numero de t
    elif rep_first < rep_second:
    #Solo se busca en la primera 
        i = to_change(primeramitad, y_first,y_second,1)
        #se cambia la letra
        primeramitad[i] = y_first
        m = m-1
        #se llama a la funcion recursiva
        changing(primeramitad, segundamitad, y_first, y_second,m)
    #Si el numero de t es menor al numero de x
    elif rep_first > rep_second:
    #solo se busca en la segunda mitad
        j = to_change(segundamitad, y_second,y_first,2)
        #se cambia la letra
        segundamitad[j] = y_second
        m = m-1
        #se llama a la funcion recursiva
        changing(primeramitad, segundamitad, y_first, y_second,m)

    return primeramitad+segundamitad


    
    

#funcion que busca el indice de la letra a cambiar
def to_change (lista, letra_principal, letra_otra, cadena):
    rep_principal = lista.count(letra_principal)
    rep_otra = lista.count(letra_otra)
    #Si no todas son x o t
    if cadena == 1:
        if rep_principal + rep_otra != len(lista):
            #Busco una letra que no sea ni x ni t
            for i in lista:
                #excepto si es la primera
                if lista.index(i)==0 and i == letra_otra:
                    return lista.index(i)
                if i != letra_principal and i != letra_otra:
                    return lista.index(i)
        #Si todas son x o t
        else:
        #Busco la primera letra que no sea x
            for i in lista:
                if i != letra_principal:
                    return lista.index(i)
    if cadena == 2:
        i = len(lista)-1
        if rep_principal + rep_otra != len(lista):
            #Busco una letra que no sea ni x ni t
            while i >= 0:
                #excepto si es la útima
                if i == len(lista)-1 and i == letra_otra:
                    return i
                if lista[i] != letra_principal and lista[i] != letra_otra:
                    return i
                i = i-1
        #Si todas son x o t
        else:
        #Busco la primera letra que no sea x
            while i >= 0:
                if lista[i] != letra_principal:
                    return i
                i = i-1


if __name__ == '__main__':
    numero_casos = int(sys.stdin.readline())
    for i in range(numero_casos):
        x, y, m = sys.stdin.readline().split()
        m = int(m)
        cantidad_subsecuencias = find_secuence(x,y,m)
        print(cantidad_subsecuencias)
    