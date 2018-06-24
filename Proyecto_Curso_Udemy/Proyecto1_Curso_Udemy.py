import random
class Usuario:
    def __init__(self, nombre,edad, pais, email, cuenta):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.email = email
        self.cuenta = cuenta
        self.saldo = 0
        #self.listaUsuarios = listaUsuarios

class Cuenta(Usuario):
    def __init__(self, listaUsuarios):
        self.listaUsuarios = listaUsuarios

    def depositar(self, numeroCuentaUser, cuentaUser):
        for n in range(0, len(listaUsuarios)):
            if cuentaUser == listaUsuarios[n].nombre and numeroCuentaUser == listaUsuarios[n].cuenta:
                print("Ingrese la cantidad que quiere depositar")
                deposito = int(input())
                self.saldo = self.saldo + deposito
                print("Su saldo total es:", self.saldo)
    def retirar(self, numeroCuentaUser, cuentaUser):
        for n in range(0, len(listaUsuarios)):
            if cuentaUser == listaUsuarios[n].nombre and numeroCuentaUser == listaUsuarios[n].cuenta:
                print("Ingrese la cantidad que quiere retirar")
                deposito = int(input())
                self.saldo = self.saldo + deposito
                print("Su saldo total es:", self.saldo)
    def generarClave(self):
        clave = random.randint(1,100000)
        return clave
    def validadCuenta(self, nombre, cuenta):
        print("aca", nombre, cuenta)
        valida = False
        for n in range(0, len(listaUsuarios)):
            print("imp",n, listaUsuarios[n].nombre, listaUsuarios[n].cuenta)
            if nombre == listaUsuarios[n].nombre and cuenta == listaUsuarios[n].cuenta:
                print("su cuenta es valida")
                valida = True
        return valida

            #if nombre in listaUsuarios[n].nombre and cuenta in listaUsuarios[n].cuenta:
                #print("Su cuenta es valida")
                #return Trueelse:
                #print("Su cuenta no existe")
               #return False


class Balance(Cuenta):
    pass

listaUsuarios = []

print("Bienvenido al banco Python")
#print("¿Desea crear una nueva cuenta en el banco?, presione 1")
#print("Si ya tiene una cuenta presionar 2 para acceder a esta")
#print(random.randint(1,100000))
#eleccionUsuario = int(input())
cuenta = Cuenta(listaUsuarios)
for n in range(0,3):
    print("¿Desea crear una nueva cuenta en el banco?, presione 1")
    print("Si ya tiene una cuenta presionar 2 para acceder a esta")
    eleccionUsuario = int(input())
    if eleccionUsuario == 1:

        print("ingrese el nombre")
        nombre = input()
        print("ingrese la edad")
        edad = input()
        print("ingrese su pais")
        pais = input()
        print("Ingrese su email")
        email = input()
        numCuenta = cuenta.generarClave()
        print("Su numero de cuenta es: ", numCuenta)
        usuario = Usuario(nombre, edad, pais, email, numCuenta)
        listaUsuarios.append(usuario)
        #print(usuario.nombre, usuario.cuenta)
        #print(listaUsuarios[0].cuenta)
    elif eleccionUsuario == 2:
        print("ingrese su nombre")
        nombre = input()
        print("Ingrese su numero de cuenta")
        numeroCuenta = int(input())
        validacion = cuenta.validadCuenta(nombre, numeroCuenta)
        if validacion == True:
            print("Que desea hacer")
            print("Si quiere depositar presione 1")
            print("Si quiere retirar Presione 2")
            eleccion = int(input())
            if eleccion == 1:
                cuenta.depositar(nombre, numeroCuenta)
            elif eleccion == 2:
                cuenta.retirar(nombre, numeroCuenta)

    #pass
