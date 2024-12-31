#---------------------------
# Autor: Camilo Huertas
# dec/2024
#---------------------------
# Este script es una calculadora basica, el usuario ingresa 2 numeros y el codigo los suma, resta, multiplica y divide, luego los imprime.
#---------------------------


print("Hola, ingresa el primer numero")

a = float(input())

print("Ingresa el segundo numero")

b = float(input())

suma = a + b
print ("la suma es ", suma)

resta = a - b
print ("La resta es", resta)

multi = a * b
print ("La multiplicacion es ", multi)

if b != 0:
    divi = a / b
    print("La division es", divi)
else:
    print("b es 0, una división indefinida")
