estudiantes = int(input("Cuántos alumnos hay en su grupo?: ")) #Se solicita al usuario que ingrese el número total de estudiantes en el grupo

edades = 0 #Se inicializa la variable edades en 0

for i in range(estudiantes): #Se inicia un bucle for que iterará desde 0 hasta estudiantes - 1
    edad = int(input("Inserte la edad de cada alumno: ")) #En cada iteración del bucle, se solicita al usuario que ingrese la edad de un estudiante
    edades += edad #Se suma la edad ingresada al total acumulado en la variable edades

edadPromedio = edades / estudiantes #Después de completar el bucle, se calcula el promedio de las edades dividiendo la suma total de las edades (edades) por el número total de estudiantes

print(f"El promedio de edad entre todo su grupo de alumnos es de: {edadPromedio}") #Se imprime el promedio de las edades, mostrando el resultado al usuario