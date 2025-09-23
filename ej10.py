lista = [2,6,2,8,3]

promedio = sum(lista) / len(lista)
print("El promedio de la lista es:", promedio)

suma = 0
for numero in lista:
	suma += numero
promedio_for = suma / len(lista)
print(f"El promedio calculado con for es: {promedio_for}")