class Progresion:
    def __init__(self, start = 0):
        #inicializamos current como el primer valor de la progresion
        self._current = start

    def _advance(self):
        self._current = self._current + 1

    #definimos como avansa el iterador
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            respuesta = self._current
            self._advance()
            return respuesta
    #aca el iterador se deevuelve a si mismo
    def __iter__(self):
        return self

    def print_progresion(self, n):
        #se imprimen los valores de la progresion
        print(" ".join(str(next(self))for j in range(n)))
class ProgresionAritmetica(Progresion):
    def __init__(self, incremento = 1, start = 0):
        #incremento para emepesar siempre es 1, se puede cambiar
        #start es el primer elemento de la progresion
        #el contructor de la clase de la que heredamos
        super().__init__(start)
        self._incremento = incremento
    def _advance(self):
        self._current = self._current + 1

class ProgresionGeometrica(Progresion):
    def __init__(self, base =2, start = 1):

        super().__init__(start)
        self._base = base
    def _advance(self):
        self._current = self._current * self._base

class ProgrecionFibonacci(Progresion):
    def __init__(self, first = 0, second = 1):
        #primero es el primer termino de la serie
        #segundo es el segundo termino de la progresion

        super().__init__(first)
        self._prev = second - first
    def _advance(self):

        self._prev, self._current = self._current, self._prev + self._current