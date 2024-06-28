import os
os.system('cls' if os.name == 'nt' else 'clear')

# importacion
from clasesEspeciales import Libro

libro1 = Libro("Stephen King", "It", 1032)
print(str(libro1))
print(len(libro1))