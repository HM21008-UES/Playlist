from nodos import nodo
class pila:
    def __init__(self):
        self.cima = None # inicializacion de la cima
    def push(self, dato):
        n = nodo(dato)
        n.siguiente = self.cima # enlace con la cima previa
        self.cima = n # actualizacion de la cima
    def pop(self):
        if not self.cima: return None # verificacion de vacio
        dato = self.cima.dato
        self.cima = self.cima.siguiente # reajuste del puntero
        return dato