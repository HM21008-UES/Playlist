import json
from nodos import nodo

class listaplaylist:
    def __init__(self):
        self.cabeza = None # definicion del inicio de la lista
    def agregar(self, dato):
        n = nodo(dato)
        if not self.cabeza: # insercion en lista vacia
            self.cabeza = n
            return
        actual = self.cabeza
        while actual.siguiente: # recorrido hasta el ultimo nodo
            actual = actual.siguiente
        actual.siguiente = n
    def mostrar_rec(self, nodo_actual):
        if not nodo_actual: return # caso base para la recursividad
        print(nodo_actual.dato) # impresion del dato
        self.mostrar_rec(nodo_actual.siguiente) # llamada recursiva
    def guardar_json(self):
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato.to_dict()) # acumulacion de datos
            actual = actual.siguiente
        try:
            with open("Mi_Playlist.json", "w") as archivo:
                json.dump(datos, archivo, indent=4) # escritura en archivo externo
        except Exception as e:
            print(f"Error en la persistencia: {e}")




