class Personaje:
    def __init__(self, nombre, herramienta):
        self.nombre = nombre
        self.arma = herramienta

class Mago(Personaje):
    pass

hechicero = Mago("Merlín", "caldero")
print(hechicero.nombre)
print(hechicero.arma)