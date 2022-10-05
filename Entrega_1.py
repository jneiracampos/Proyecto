"""
Esta funcion determina si una secuencia es subsecuencia de otra
@param string1: secuencia 1
@param string2: secuencia 2
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

"""
Esta funcion cuenta la cantidad de veces que se repite una subsecuencia en una secuencia
@param string1: secuencia 1
@param string2: secuencia 2
@return: cantidad de veces que se repite la subsecuencia
"""
def countSubSequence(string1, string2):
    m = len(string1)
    n = len(string2)
    if isSubSequence(string1, string2, m, n):
        return 1 + countSubSequence(string1, string2[m:])
    else:
        return 0

if __name__ == '__main__':
    string1 = input("Ingrese la subsecuencia: ")
    string2 = input("Ingrese la secuencia: ")
    print(countSubSequence(string1, string2))
