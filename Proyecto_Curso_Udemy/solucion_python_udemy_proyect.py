#proyecto del sistema de banco
from abc import ABCMeta, abstractmethod
from random import randint

#clase abstracta
#creamos esta clase para evitar que estos metodos se utilizen
class Cuenta(metaclass = ABCMeta):
    @abstractmethod
    def crearCuenta(self):
        return 0

    @abstractmethod
    def autentificacion(self):
        return 0

    @abstractmethod
    def retiro(self):
        return 0

    @abstractmethod
    def deposito(self):
        return 0

    @abstractmethod
    def mostrarBalance(self):
        return 0
class CuentaAhorro(Cuenta):
    def __init__(self):
        #dicionario de las cuentas de ahorros del banco
        # Los valores para el diccionario son [la llave][0] = nombre y [llave ][1] seran el balance de la cuenta
        self.cuentasAhorros = {}
    def crearCuenta(self, nombre, depositoInicial):
        self.numeroCuenta = randint(10000, 99999)
        self.cuentasAhorros[self.numeroCuenta] = [nombre, depositoInicial]
        print("Creacion de cuenta hecha correctamente, su numero de cuenta es: ", self.numeroCuenta)
    def autentificacion(self, nombre, numeroCuenta):
        if numeroCuenta in self.cuentasAhorros.keys():
            if self.cuentasAhorros[numeroCuenta][0] == nombre:
                print("Validacion satisfactoria")
                #este sera el numero de cuenta para el restante proceso de la isntancia de la cuenta de ahorro
                self.numeroCuenta = numeroCuenta
                return True
            else:
                print("Autentificacion fallida")
                return False
        else:
            return False

    def retiro(self, montoRetiro):
        if montoRetiro > self.cuentasAhorros[self.numeroCuenta][1]:
            print("balance insufieciente")
        else:
            self.cuentasAhorros[self.numeroCuenta][1] -= montoRetiro
            self.mostrarBalance()

    def deposito(self, montoDeposito):
        self.cuentasAhorros[self.numeroCuenta][1] += montoDeposito
        self.mostrarBalance()
    def mostrarBalance(self):
        print("Balance disponible: ",self.cuentasAhorros[self.numeroCuenta][1])


cuentaDeAhorro = CuentaAhorro()

while True:
    print("Presione 1 para crear una cuenta")
    print("presione 2 para acceder a una cuenta existente")
    print("presione 3 para salir")
    eleccionUsuario = int(input())
    if eleccionUsuario is 1:
        print("ingresa tu nombre")
        nombre = input()
        print("Ingrese su deposito inicial")
        depostio = int(input())
        cuentaDeAhorro.crearCuenta(nombre, depostio)
    if eleccionUsuario is 2:
        print("ingrese su nombre")
        nombre = input()
        print("Ingrese su numero de cuenta")
        numeroDeCuenta = int(input())
        estadoDeAutentificacion = cuentaDeAhorro.autentificacion(nombre, numeroDeCuenta)
        if estadoDeAutentificacion is True:
            while True:
                print("Presione 1 para retirar")
                print("presione 2 para depositar")
                print("presione 3 para ver su balance")
                print("presione 4 para volver al menu anterior")
                eleccionUsuario2 = int(input())
                if eleccionUsuario2 is 1:
                    print("Ingrese la cantidad que quiere retirar")
                    montoRetiro = int(input())
                    cuentaDeAhorro.retiro(montoRetiro)
                if eleccionUsuario2 is 2:
                    print("Ingrese la cantidad que quiere depositar")
                    cantidadDeposito = int(input())
                    cuentaDeAhorro.deposito(cantidadDeposito)
                if eleccionUsuario2 is 3:
                    cuentaDeAhorro.mostrarBalance()
                if eleccionUsuario2 is 4:
                    break
    elif eleccionUsuario is 3:
        quit()
