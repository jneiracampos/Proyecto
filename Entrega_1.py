"""
Esta funcion determina si una secuencia es subsecuencia de otra
@param string1: secuencia 1
@param string2: secuencia 2
@param m: longitud de la secuencia 1 - y 
@param n: longitud de la secuencia 2 - x
@return: True si es subsecuencia, False si no lo es
"""
def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False

    # If last characters of two
    # strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)

    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)



def rightString2(string1, string2, primera, segunda):
    if segunda == -1:
        mayorPosicionLetra = string2.rfind(primera)
        string2.replace(string2[mayorPosicionLetra-1],'A')
    elif segunda != -1:
        mayorPosicionLetra = string2.rfind(primera)
        if mayorPosicionLetra != -1:
            string2.replace(string2[mayorPosicionLetra-1],'A')
        else:
            string2.replace('A', primera)
            mayorPosicionLetra = string2.rfind(segunda)
            string2.replace(string2[mayorPosicionLetra-1],'B')
    return string2



"""
Esta funcion cuenta la cantidad de veces que se repite una subsecuencia en una secuencia
@param string1: subsecuencia
@param string2: secuencia
@return: cantidad de veces que se repite la subsecuencia
"""
def countSubSequence(string1, string2):
    m = len(string1)
    n = len(string2)
    if m  == 1:
        primera = string1
        segunda = -1
    elif m == 2:
        primera = string1[0]
        segunda = string1[1]
    if isSubSequence(string1, string2, m, n):
        string2=rightString2(string1, string2, primera, segunda)
        return 1 + countSubSequence(string1, string2)
    else:
        return 0

if __name__ == '__main__':
    string1 = input("Ingrese la subsecuencia: ")
    string2 = input("Ingrese la secuencia: ")
    print(countSubSequence(string1, string2))
