import random
class Usuario:
    def __init__(self, nombre,edad, pais, email, cuenta):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.email = email
        self.cuenta = cuenta
class Cuenta(Usuario):
    def __init__(self):
        pass

    def depositar(self):
        pass
    def retirar(self):
        pass
    def generarClave(self):
        clave = random.randint(1,100000)
        return clave
    def validadCuenta(self):
        pass

class Balance(Cuenta):
    pass

print("Bienvenido al banco Python")
print("¿Desea crear una nueva cuenta en el banco?, presione 1")
print("Si ya tiene una cuenta presionar 2 para acceder a esta")
print(random.randint(1,100000))
eleccionUsuario = int(input())
cuenta = Cuenta()
if eleccionUsuario == 1:

    print("ingrese el nombre")
    nombre = input()
    print("ingrese la edad")
    edad = input()
    print("ingrese su pais")
    pais = input()
    print("Ingrese su email")
    email = input()
    clave = cuenta.generarClave()
    print("Su numero de cuenta es: ", clave)
    usuario = Usuario(nombre, edad, pais, email, clave)
    #print(usuario.nombre, usuario.cuenta)
elif eleccionUsuario == 2:
    pass
