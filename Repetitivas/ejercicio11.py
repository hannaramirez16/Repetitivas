#Se inicializan las variables que se utilizarán para almacenar los datos recopilados
cantidadHombres = 0
cantidadMujeres = 0
totalAltura = 0
cantidadAlturaMayor170 = 0
cantidadAlturaMenorOIgual150 = 0
cantidadAlumnos = 0

edad = int(input("Ingrese la edad del alumno (0 para finalizar): ")) #La entrada se convierte a entero con int()
if edad == 0: #la edad ingresada es 0, el proceso de entrada de datos debe finalizar
    
    sexo = input("Ingrese el sexo del alumno (M para masculino, F para femenino): ").upper() #se solicita el sexo del alumno (M para masculino y F para femenino) y se convierte a mayúsculas usando upper()
    altura = float(input("Ingrese la altura del alumno en metros: ")) #se solicita la altura del alumno en metros y se convierte a float() para permitir decimales

#Se incrementa el contador correspondiente según el sexo ingresado, si el sexo es M, se incrementa cantidadHombres Si el sexo es F, se incrementa cantidadMujeres
    if sexo == "M":
        cantidadHombres += 1
    elif sexo == "F":
        cantidadMujeres += 1
    #Se suma la altura del alumno al total acumulado en totalAltura y se incrementa el contador cantidadAlumnos
    totalAltura += altura
    cantidadAlumnos += 1
#Se incrementan los contadores correspondientes según la altura ingresada
    if altura > 1.70:
        cantidadAlturaMayor170 += 1

    if altura <= 1.50:
        cantidadAlturaMenorOIgual150 += 1
#Se calcula el promedio de altura si se ha procesado al menos un alumno (cantidadAlumnos > 0
if cantidadAlumnos > 0:
    alturaPromedio = totalAltura / cantidadAlumnos
else:
    alturaPromedio = 0

#Se imprimen los resultados: Cantidad de hombres, mujeres, altura promedio (formateada a dos decimales), etc
print(f"Cantidad de hombres: {cantidadHombres}")
print(f"Cantidad de mujeres: {cantidadMujeres}")
print(f"Altura promedio: {alturaPromedio:.2f} metros")
print(f"Cantidad de alumnos con altura mayor a 1.70 m: {cantidadAlturaMayor170}")
print(f"Cantidad de alumnos con altura menor o igual a 1.50 m: {cantidadAlturaMenorOIgual150}")