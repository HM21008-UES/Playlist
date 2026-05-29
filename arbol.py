from nodos import nodoarbol

class arbol:
    def __init__(self):
        self.raiz = nodoarbol("Música") # definicion de la raiz
    def agregar(self, nombre, padre_nombre):
        padre = self.buscar(self.raiz, padre_nombre)
        if not padre: return # validacion de existencia del padre
        padre.hijos.append(nodoarbol(nombre)) # insercion de subgenero
    def buscar(self, nodo_actual, nombre):
        if not nodo_actual: return None
        if nodo_actual.nombre == nombre: return nodo_actual # retorno de nodo encontrado
        for hijo in nodo_actual.hijos:
            res = self.buscar(hijo, nombre) # busqueda recursiva
            if res: return res
        return None
    def mostrar(self, nodo_actual, nivel=0):
        if not nodo_actual: return
        print("  " * nivel + nodo_actual.nombre) # impresion jerarquica
        for hijo in nodo_actual.hijos:
            self.mostrar(hijo, nivel + 1)