class FiguraGeometrica:
    def __init__(self, ancho="", altura=""):
        self.ancho = ancho
        self.altura = altura
        
    def area(self):
        pass
    
class Triangulo(FiguraGeometrica):
    def area(self):
        super().area()
        return (self.ancho * self.altura) / 2

class Rectangulo(FiguraGeometrica):
    def area(self):
        super().area()
        return self.ancho * self.altura
    
figura1 = Triangulo(5, 10)
figura2 = Rectangulo(4, 6)

print("El área de la figura es:", figura1.area())
print("El área de la figura es:", figura2.area())