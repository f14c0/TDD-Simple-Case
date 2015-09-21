__author__ = 'JULIAN'


def solve(cadena):
    if not cadena:
        return 0
    elif len(cadena) == 1:
        return cadena
    elif len(cadena) > 1:
        cadena = cadena.replace(":",",")
        cadena = cadena.replace("&",",")
        numbers = cadena.split(',')
        numbers = numbers[:2]
        result=0
        for number in numbers:
            result += int(number)
        return result
