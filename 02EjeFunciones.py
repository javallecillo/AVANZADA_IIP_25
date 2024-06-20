import os
os.system('cls' if os.name == 'nt' else 'clear')

def devolver_distintos(a, b, c):
    suma = a+b+c

    if suma >= 15:
        resultado = max(a, b, c)
    elif suma <= 10:
        resultado = min(a, b, c)
    else:
        resultado = a+b+c - max(a, b, c) - min(a, b, c)

    return resultado

print(devolver_distintos(4, 3, 10))

#Ordenar de menor a mayor
def ordenar_valores(a, b, c):
    return sorted([a, b, c])