from cancion import cancion  # clase canción
from lista import listaplaylist  # lista enlazada (playlist)
from cola import cola  # cola de reproducción
from pila import pila  # pila de historial
from arbol import arbol  # árbol de géneros
import time  # control de tiempos (animación)

def mostrar_reproductor(c):
    print("\n────────── REPRODUCTOR ──────────")
    print(f"Canción : {c.titulo}")
    print(f"Artista : {c.artista}")
    print("\n        ⏮       ▶       ⏭")
    print("──────────────────────────")
    for i in range(27):
        barra = "█" * i + "░" * (26 - i)
        print(f"\r{barra}", end="")
        time.sleep(0.20)
    print("\n──────────────────────────")
    print("Canción finalizada")

def main():
    playlist = listaplaylist()
    cola_rep = cola()
    historial = pila()
    arbol_gen = arbol()
    while True:
        print("\n--- Sistema de Gestión ---")
        print("1. Agregar canción")
        print("2. Ver lista")
        print("3. Encolar canción")
        print("4. Reproducir canción")
        print("5. Ver historial")
        print("6. Ver géneros")
        print("7. Guardar en JSON")
        print("8. Salir")

        try:
            op = input("Seleccione una opción: ")
            match op:
                case "1":
                    titulo = input("Título: ")
                    artista = input("Artista: ")
                    genero = input("Género (Rock, Pop, Rap, Otros): ")
                    nueva = cancion(titulo, artista)
                    playlist.agregar(nueva)
                    arbol_gen.agregar(genero, "Música")
                    print("Canción agregada correctamente")

                case "2":
                    if not playlist.cabeza:
                        print("No hay canciones en la playlist")
                    else:
                        print("\n--- PLAYLIST ---")
                        playlist.mostrar_rec(playlist.cabeza)

                case "3":
                    cola_rep.encolar(
                        cancion(
                            input("Título: "),
                            input("Artista: ")
                        )
                    )
                    print("Canción agregada a la cola")

                case "4":
                    c = cola_rep.desencolar()
                    if c:
                        mostrar_reproductor(c)
                        historial.push(c)
                    else:
                        print("No hay canciones en cola")

                case "5":
                    c = historial.pop()
                    if c:
                        print(f"Última canción reproducida: {c}")
                    else:
                        print("No hay historial disponible")

                case "6":
                    arbol_gen.mostrar(arbol_gen.raiz)

                case "7":
                    playlist.guardar_json()
                    print("Playlist guardada en JSON")

                case "8":
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Opción inválida")
        except Exception as e:
            print(f"Error de ejecución: {e}")

if __name__ == "__main__":
    main()