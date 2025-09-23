class animal:
    def __init__(self, nombre = "", especie = ""):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self, sonido):
        return f"{self.nombre} dice {sonido}"
    
    def __str__(self):
        return f"Animal(nombre={self.nombre}, especie={self.especie})"
    
    def mostrar_nombre(self):
        return self.nombre
    
class perro(animal):
    def __init__(self, nombre = "", especie = "Perro"):
        super().__init__(nombre, especie)
    
animal1 = animal("Rex", "Perro")
animal2 = animal("Michi", "Gato")

print(animal1.hacer_sonido("Guau"))
print(animal2.hacer_sonido("Miau"))
print (animal1.nombre)    

print (animal2.especie)
print (animal1.hacer_sonido("Woof"))
print (animal2.__str__())