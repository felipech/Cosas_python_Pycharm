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
        self.saldo = 0

    def depositar(self, cuentaUser,numeroCuentaUser,):
        for n in range(0, len(listaUsuarios)):
            if cuentaUser == listaUsuarios[n].nombre and numeroCuentaUser == listaUsuarios[n].cuenta:
                print("Ingrese la cantidad que quiere depositar")
                deposito = int(input())
                self.saldo = self.saldo + deposito
                print("Su saldo total es:", self.saldo)
    def retirar(self, cuentaUser,numeroCuentaUser):
        for n in range(0, len(listaUsuarios)):
            if cuentaUser == listaUsuarios[n].nombre and numeroCuentaUser == listaUsuarios[n].cuenta:
                print("Ingrese la cantidad que quiere retirar")
                retiro = int(input())
                self.saldo = self.saldo - retiro
                print("Su saldo total es:", self.saldo)
    #def generarClave(self):
     #   clave = random.randint(1,100000)
      #  return clave
    def validadCuenta(self, nombre, cuenta):
        #print("aca", nombre, cuenta)
        valida = False
        for n in range(0, len(listaUsuarios)):
            print("imp",n, listaUsuarios[n].nombre, listaUsuarios[n].cuenta)
            if nombre == listaUsuarios[n].nombre and cuenta == listaUsuarios[n].cuenta:
                print("su cuenta es valida")
                valida = True
        return valida
    def balance(self, nombre, cuenta):
        print("Su balance es el siguiente")
        for n in range(0, len(listaUsuarios)):
            if nombre == listaUsuarios[n].nombre and cuenta == listaUsuarios[n].cuenta:
                print("Nombre de la cuenta: ", listaUsuarios[n].nombre)
                print("Pais: ", listaUsuarios[n].pais)
                print("Número de cuenta: ", listaUsuarios[n].cuenta)
                print("Saldo de la cuenta: ", listaUsuarios[n].saldo)
            #if nombre in listaUsuarios[n].nombre and cuenta in listaUsuarios[n].cuenta:
                #print("Su cuenta es valida")
                #return Trueelse:
                #print("Su cuenta no existe")
               #return False




listaUsuarios = []

print("Bienvenido al banco Python")
#print("¿Desea crear una nueva cuenta en el banco?, presione 1")
#print("Si ya tiene una cuenta presionar 2 para acceder a esta")
#print(random.randint(1,100000))
#eleccionUsuario = int(input())
#cuenta = Cuenta(listaUsuarios)
while True:
    print("¿Desea crear una nueva cuenta en el banco?, presione 1")
    print("Si ya tiene una cuenta presionar 2 para acceder a esta")
    print("Si desea salir presione 3")
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
        numCuenta = random.randint(1, 100000)
        print(numCuenta)
        usuario = Usuario(nombre, edad, pais, email, numCuenta)
        print(usuario.cuenta)

        listaUsuarios.append(usuario)
        cuenta = Cuenta(listaUsuarios)
        print("Su numero de cuenta es: ", numCuenta)
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
            print("Si quiere ver su balance presione 3")
            eleccion = int(input())
            if eleccion == 1:
                cuenta.depositar(nombre, numeroCuenta)
            elif eleccion == 2:
                cuenta.retirar(nombre, numeroCuenta)
    #pass
    elif eleccionUsuario == 3:
        quit()