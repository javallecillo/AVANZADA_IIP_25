# clase de operaciones aritmeticas
class operacionesAritmeticas:

    def __init__(self, a, b):
        self.a=a
        self.b=b

    # suma
    def suma(self):
        print(self.a + self.b)

    # resta
    def resta(self):
        print(self.a - self.b)
    
    # producto
    def producto(self):
        print(self.a * self.b)

    # division
    def division(self):
        print(self.a /  self.b)

    def potencia(self, a, b):
        print(a ** b)

op = operacionesAritmeticas(int(input("a: ")), int(input("b: ")))
op.suma()
op.potencia(2, 3)