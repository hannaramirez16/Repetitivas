calificacionMenos50 = 0 #calificacionMenos50 para estudiantes con calificaciones menores a 50
calificacion50 = 0 #calificacion50 para estudiantes con calificaciones entre 50 (inclusive) y 70 (exclusive)
calificacion70 = 0 #calificacion70 para estudiantes con calificaciones entre 70 (inclusive) y 80 (exclusive)
calificacion80 = 0 #calificacion80 para estudiantes con calificaciones mayores o iguales a 80

i = 0 #Esta variable se usará como contador en el bucle while

while i < 23: #Se inicia un bucle while que se ejecutará 23 veces, ya que el valor de i comienza en 0 y se incrementa en cada iteración hasta que alcanza 23
    i += 1 #e solicita al usuario que ingrese la calificación de un estudiante. Esta entrada se convierte a entero utilizando int() y se almacena en la variable calificacion
    
    calificacion = int(input("Inserte la calificación del estudiante: ")) #Esta entrada se convierte a entero utilizando int() y se almacena en la variable calificacion

    if calificacion < 50: #Si calificacion es menor a 50, se incrementa el contador calificacionMenos50
        calificacionMenos50 += 1
    elif calificacion >= 50 and calificacion < 70: #Si calificacion está en el rango [50, 70), se incrementa el contador calificacion50
        calificacion50 += 1
    elif calificacion >= 70 and calificacion < 80: #Si calificacion está en el rango [70, 80), se incrementa el contador calificacion70
        calificacion70 += 1
    else:
        calificacion80 += 1

#Se imprimen los resultados, la cantidad de estudiantes con calificaciones menores a 50, 70, 80,o mayores
print(f"{calificacionMenos50} Estudiantes obtuvieron una calificación menor a 50.")
print(f"{calificacion50} Estudiantes obtuvieron una calificación entre 50 y 70.")
print(f"{calificacion70} Estudiantes obtuvieron una calificación entre 70 y 80.")
print(f"{calificacion80} Estudiantes obtuvieron una calificación mayor a 80.")