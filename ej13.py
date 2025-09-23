class estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}")
        
estudiante1 = estudiante("Ana", 20, "DAM")
estudiante2 = estudiante("Antonio", 20 , "DAW")
estudiante3 = estudiante("Israel" , 19 , "ASIR")

estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()
estudiante3.mostrar_informacion()