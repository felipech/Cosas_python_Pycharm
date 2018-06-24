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


