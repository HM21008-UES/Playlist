class nodo:
    def __init__(self, dato):
        self.dato = dato # registro del dato
        self.siguiente = None # enlace al siguiente nodo

class nodoarbol:
    def __init__(self, nombre):
        self.nombre = nombre # asignacion del nombre del genero
        self.hijos = []