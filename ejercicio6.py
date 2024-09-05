numeroPersonas = int(input("Cuantas personas hay en el salon?: ")) #Se solicita al usuario que ingrese el número total de personas en el salón
#Estas variables contarán la cantidad de mujeres y hombres respectivamente
mujeres = 0
hombres = 0

for i in range(numeroPersonas): #Se inicia un bucle for que se ejecutará numeroPersonas veces
    personas = input("Escriba si cada participante es hombre o mujer: ") #se solicita al usuario que ingrese el género de la persona

    if personas == "mujer": #Si la entrada es "mujer", se incrementa el contador mujeres en 1
        mujeres += 1
    elif personas == "hombre": #Si la entrada es "hombre", se incrementa el contador hombres en 1
        hombres += 1

print(f"Hay {hombres} hombres en el salon.") #La cantidad de hombres en el salón
print(f"Hay {mujeres} mujeres en el salon.") #La cantidad de mujeres en el salón
print(f"Hay un total de {numeroPersonas} personas.") #El número total de personas en el salón