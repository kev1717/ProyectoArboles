class Nodo:
    def __init__(self, nombre, distancia=0):
        self.nombre = nombre
        self.distancia = distancia
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __repr__(self):
        return f"{self.nombre} (Distancia: {self.distancia})"

class rutaTransporte:
    def __init__(self):
        self.raiz= Nodo("Posicion inicial", distancia=0)
        