import re

name = 'Lizz'
print(name[0:2])
['A','B','C','A','B','C']
lista=['A','B','C','A','B','C']
set1 = set(lista)
print(set1)
x, y, z = 6, 2, 5
print(x,y,z)
def par_inpar(numero):
    restar = 2

    for n in range(0,numero):
        numero = numero - restar
        if numero == 0:
            return numero
    return numero

def multiplos(num1, num2):
    resultado = num1%num2
    if resultado == 0:
        print("es multiplo")
    else:
        print("no es multiplo")


porOinpar = par_inpar(9)
if porOinpar == 0:
    print("es par")
else:
    print("es impar")

def menor_mayor(numeros):
    menor = numeros[0]
    mayor = numeros[0]

    for n in range(0, len(numeros)):
        if menor > numeros[n]:
            menor = numeros[n]
        elif mayor < numeros[n]:
            mayor = numeros[n]
    return (menor,mayor)

def suma_cuadrado(num):
    resultado = 0
    for n in range(0,num):
        resultado = n**2 + resultado
    return resultado

def impares_cuadrados(numero):
    resultado = 0
    #print(numero)
    for n in range(0,numero):
        if n%2 != 0:
            #print(n)
            resultado = resultado + n**2
    print(resultado)

def range_funct():
    for n in range(50, 90, 10):
        print(n)
    for n in range(8, -9, -2):
        print(n)
def lista_cuadradA(limite):
    lista1 = []
    for n in range(0, limite):
        lista1.append(2**n)
        print(lista1)

"""multiplos(0,4)
list1 = [14,2,4,52,12,3,14,2,4,52,12,3,52,12,3]
lista2 = [2324,43,434554,56,3,46,312,5,2,45,63,56,342,566,323,1]
result = menor_mayor(lista2)
print(result)

sumasqrt = suma_cuadrado(10)
print(sumasqrt)
impares_cuadrados(100)
#range_funct()
lista_cuadradA(10)"""

def answer(name):
    largo = 0
    nombre_abreviado = ""
    nombres = name.split(' ')
    largo = len(nombres)
    print(nombres, largo)
   # print(nombres[0][0])
    nombre_abreviado = nombres[0]
    nombre_abreviado[0]
    print("asda ___",nombre_abreviado[0].upper())
    for n in range(0, largo):
        #nombre_abreviado = nombres[0]
        print("nnn", n)
        if n > 0 and n < largo - 1:
            #print("aca")
            nombre_abreviado = nombre_abreviado + " " +nombres[n][0].upper()
            #print(nombre_abreviado)
            #print(nombres[n])
        if n == largo - 1:
            nombre_abreviado = nombre_abreviado + " "+ nombres[n]
    return nombre_abreviado
import re
def answer2(phone_number):
    count = 0
    invalido = "invalido"
    #print(phone_number)
    #print(re.sub("-"," ",phone_number))
    nuevo_phone_number = ""
    phone_number = re.sub("-|\.","",phone_number)
    print(phone_number)
    #print(re.sub("\(|\)","",phone_number))
    phone_number = re.sub("\(|\)","",phone_number)
    #phone_number = phone_number.split(" ")
    nuevo_phone_number = phone_number
    if len(nuevo_phone_number) < 10:
        return invalido
    for n in range(0, len(nuevo_phone_number)):
        if n < 3 and n < 6:
            primero = nuevo_phone_number[:3]
            segundo = nuevo_phone_number[3:6]
            print(primero + " " + segundo)
        ultimo = nuevo_phone_number[6:]
    print(" " + ultimo)
    #for n in range(0, len(nuevo_phone_number)):
    nuevo_phone_number = primero + " " + segundo + " " + ultimo
    print(nuevo_phone_number)
    #print(phone_number)
    return nuevo_phone_number



"""name = "felipe Choque henriquez"

respuesta = answer(name)
print(respuesta)"""

numero = "65.0555.1234"
nuevo_numero = answer2(numero)
print(nuevo_numero)