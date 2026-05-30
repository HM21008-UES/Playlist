from nodos import nodo
class cola:
    def __init__(self):
        self.frente = None # inicializacion del frente
        self.final = None # inicializacion del final
    def encolar(self, dato):
        n = nodo(dato)
        if not self.final: # caso de lista vacia
            self.frente = self.final = n
            return
        self.final.siguiente = n # enlace con el nuevo elemento
        self.final = n # actualizacion del final
    def desencolar(self):
        if not self.frente: return None # verificacion de vacio
        dato = self.frente.dato
        self.frente = self.frente.siguiente # avance del frente
        if not self.frente: self.final = None # limpieza si la cola queda vacia
        return dato



