class Persona:
    # Atributo de clase
    especie = "humano"

# Método de instancia
def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

def saludar(self):
    print(f'Hola, mi nombre es {self.nombre}')

def cumplir_anios(self, estado_humor):
    print(f'Cumplir {self.edad + 1} años me pone {estado_humor}')

juan = Persona("Juan", 37)
juan.saludar()
juan.cumplir_anios("feliz")

print(juan.nombre)