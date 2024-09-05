ninos = 0 #Variable para acumular el peso total de los niños
jovenes = 0 #Variable para acumular el peso total de los jovenes
adultos = 0 #Variable para acumular el peso total de los adultos
ancianos = 0 #Variable para acumular el peso total de los ancianos
cantidadNinos = 0 #Variable para determinar la cantidad de niños
cantidadJovenes = 0 #Variable para determinar la cantidad de jovenes
cantidadAdultos = 0 #Variable para determinar la cantidad de adulto
cantidadAncianos = 0 #Variable para determinar la cantidad de ancianos

for i in range(10): #Se inicia un bucle for que se ejecutará 10 veces
    age = int(input("Edad de la persona: ")) #Se solicita al usuario que ingrese la edad y el peso de una persona
    weight = float(input("Peso de la persona: ")) #La edad se convierte a entero y el peso a flotante para manejar números decimales

    if age >= 0 and age <= 12: #Si la edad está entre 0 y 12 años, el peso se suma a ninos y cantidadNinos se incrementa en 1
        ninos += weight
        cantidadNinos += 1
    elif age >= 13 and age <= 29: #Si la edad está entre 13 y 29 años, el peso se suma a jovenes y cantidadJovenes se incrementa en 1
        jovenes += weight
        cantidadJovenes += 1
    elif age >= 30 and age <= 59: #Si la edad está entre 30 y 59 años, el peso se suma a adultos y cantidadAdultos se incrementa en 1
        adultos += weight
        cantidadAdultos += 1
    elif age >= 60: #Si la edad es 60 años o más, el peso se suma a ancianos y cantidadAncianos se incrementa en 1
        ancianos += weight
        cantidadAncianos += 1

#Se calculan los promedios de peso para cada grupo de edad
ninosPromedio = ninos / cantidadNinos
jovenesPromedio = jovenes / cantidadJovenes
adultosPromedio = adultos / cantidadAdultos
ancianosPromedio = ancianos / cantidadAncianos

#Se imprimen los promedios de peso para cada grupo de edad
print(f"El promedio del peso entre los niños es de: {ninosPromedio}")
print(f"El promedio del peso entre los jovenes es de: {jovenesPromedio}")
print(f"El promedio del peso entre los adultos es de: {adultosPromedio}")
print(f"El promedio del peso entre los ancianos es de: {ancianosPromedio}")