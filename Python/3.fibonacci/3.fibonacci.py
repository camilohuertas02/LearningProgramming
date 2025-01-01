#--------------------------------
# Autor: Camilo Huertas
# dec/2024
#---------------------------------
# Este script calcula el n-esimo numero de fibonacci de manera recursiva e iterativa
#---------------------------------


print("Ingresa el n-esimo de fibonacci que desea calcular")

entrada = int(input())



# Forma 1: con funcion recursiva:

def fibonacci_recursivo(n):
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:  # Llamada recursiva
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Pedir el número n al usuario
n = int(input("Ingresa el número n para calcular el n-ésimo Fibonacci: "))

# Imprimir los números de la sucesión hasta el enésimo
print("Sucesión de Fibonacci:")
for i in range(n + 1):
    print(fibonacci_recursivo(i), end=" ")


        

# Forma 2: con funcion iterativa:

def iterativa(entrada):
    a = 1
    b = 0
    print("\nLa sucesion en funcion iterativa es:")
    for i in range(1,entrada+1):
        c = a + b
        print(c)
        b = a
        a = c

iterativa(entrada)

