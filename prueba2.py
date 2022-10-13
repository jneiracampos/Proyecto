"""
Esta funcion cuenta la cantidad de veces que se repite una subsecuencia en una secuencia
@param string1: subsecuencia
@param string2: secuencia
@return: cantidad de veces que se repite la subsecuencia
"""

def count(subSecuencia, secuencia):
    count = 0
    index = 0
    while index < len(secuencia):
        aux = secuencia[index + 1:]
        for m in aux:
            if secuencia[index] + m == subSecuencia:
                count += 1
        index += 1
    return count

def listToString(s):
	str1 = ""

	for ele in s:
		str1 += ele

	return str1

"""
Esta funcion cambia n veces la secuencia de tal forma que la subsecuencia se repita la mayor cantidad de veces posible
@param string1: subsecuencia
@param string2: secuencia
@param n: cantidad de veces que se puede cambiar la secuencia
@return: cantidad de veces que se repite la subsecuencia
"""
def change(string1, string2, n):
    cambios = n

    if cambios == 0:
        return count(string1, string2)

    listSequence = list(string2)
    if (listSequence[0] != string1[0]):
        listSequence[0] = string1[0]
        cambios -= 1
    if (listSequence[-1] != string1[1] and cambios >= 1):
        listSequence[-1] = string1[1]
        cambios -= 1

    posicion = -1

    while cambios > 0 and abs(posicion) <= len(listSequence):
        if listSequence[posicion] != string1[1] and listSequence[posicion] != string1[0]:
            listSequence[posicion] = string1[1]
            cambios -= 1
        posicion -= 1
    
    newSequence = listToString(listSequence)
    maxRepeticiones = count(string1, newSequence)

    return maxRepeticiones


if __name__ == '__main__':
    string1 = input("Ingrese la subsecuencia: ")
    string2 = input("Ingrese la secuencia: ")
    n = int(input("Ingrese la cantidad de veces que se puede cambiar la secuencia: "))
    print(change(string1, string2, n))
