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
    for n in range(0,numero):
        if numero%2 != 0:
            resultado = resultado + numero**2
    print(resultado)

multiplos(0,4)
list1 = [14,2,4,52,12,3,14,2,4,52,12,3,52,12,3]
lista2 = [2324,43,434554,56,3,46,312,5,2,45,63,56,342,566,323,1]
result = menor_mayor(lista2)
print(result)

sumasqrt = suma_cuadrado(10)
print(sumasqrt)
