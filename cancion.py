class cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo # almacenamiento del titulo
        self.artista = artista # almacenamiento del artista
    def to_dict(self):
        return {"Titulo": self.titulo, "Artista": self.artista} # conversion a diccionario para formato json
    def __str__(self):
        return f"{self.titulo} - {self.artista}" # definicion de la representacion textual