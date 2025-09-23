class Calculadora:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    
    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b == 0:
            raise ValueError("No se puede dividir por cero")
        return self.a / self.b
    
calc1 = Calculadora(5, 3)

print(calc1.sumar())

calc2 = Calculadora(10, 4)
print(calc2.restar())

calc3 = Calculadora(7, 6)
print(calc3.multiplicar())

print(calc1.dividir())