#-----------------------
# Autor: camilo huertas
# dec/2024
#-----------------------
# Este script ingresa un numero entero e imprime el factorial
#-----------------------



# funcion iterativa que calcula el factorial
def factorial(n):
    i = n 
    total = 1
    # es un ciclo while cuya ecuacion es n! = n * (n-1) * (n-2) * 2 * 1  
    while i != 0:
        total = total * i
        i = i-1

    return total


print("ingrese un numero a calcular el factorial: ")

n = int(input())

print("El factorial es: ")

print(factorial(n))




