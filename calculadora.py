class Calculadora:
    def __init__(self, a="0", b="0"):
        self.a = a
        self.b = b
    
    def sumar(a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
print(Calculadora.sumar(5, 3))
print(Calculadora().restar(5, 3))
print(Calculadora().multiplicar(5, 3))
print(Calculadora().dividir(5, 2))