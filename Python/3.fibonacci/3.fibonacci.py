#--------------------------------
# Autor: Camilo Huertas
# dec/2024
#---------------------------------
# Este script calcula el n-esimo numero de fibonacci de manera recursiva e iterativa
#---------------------------------


print("Ingresa el n-esimo de fibonacci que desea calcular")

entrada = int(input())



# Forma 1: con funcion recursiva:

def recursiva(entrada):

    print("\nLa sucesion en funcion recursiva es:")


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

recursiva(entrada)
iterativa(entrada)

