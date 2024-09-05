minimo = 20 #se inicializa en 20, que es un valor mayor al rango típico de notas (suponiendo que las notas están en un rango de 0 a 10)
maximo = 0 #se inicializa en 0, que es un valor menor al rango típico de notas
notas = 0 #se inicializa en 0 y se utilizará para acumular la suma total de todas las notas ingresadas

for i in range(20): #Se ejecuta 20 veces, solicitando al usuario que ingrese una nota en cada iteración
    nota = float(input("Ingresa las notas: ")) #suma la nota actual al total acumulado
    notas += nota #
    if nota < minimo: #Si la nota ingresada es menor que el valor actual de minimo, se actualiza minimo con la nueva nota 
        min = nota
    elif nota > maximo: #Si la nota ingresada es mayor que el valor actual de maximo, se actualiza maximo con la nueva nota
        max = nota

notasPromedio = notas / 20 #Se calcula el promedio de las notas dividiendo la suma total de las notas (notas) entre 20

print(f"El promedio de todas las notas es: {notasPromedio}") #Se imprime el promedio de las notas
print(f"La nota mìnima fue de {minimo}, y la maxima fue {maximo}.") #Se imprime la nota mínima y máxima encontradas durante el proceso