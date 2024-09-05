cantidadCarros = int(input("Cuántos carros entraron a la ciudad?: ")) #Se solicita al usuario que ingrese el número total de carros que han entrado a la ciudad

amarilla = 0 #variable amarilla para carros con placas terminadas en 1 o 2
rosa = 0 # variable rosa para carros con placas terminadas en 3 o 4
roja = 0 #variable roja para carros con placas terminadas en 5 o 6
verde = 0 #variable verde para carros con placas terminadas en 7 o 8
azul = 0 #variable azul para carros con placas terminadas en 9 o 0

i = 0 #Este contador se usará para controlar el número de iteraciones en el bucle while

while i < cantidadCarros: #bucle while que continuará ejecutándose mientras i sea menor que cantidadCarros
    i += 1 #Dentro del bucle, i se incrementa en 1 en cada iteración para llevar un registro del número de carros procesados
    
    placa = int(input("Inserte el último numero de la placa: ")) #Se solicita al usuario que ingrese el último número de la placa del carro

    if placa in (1, 2): #Si placa es 1 o 2, se incrementa el contador de carros amarillos
        amarilla += 1
    elif placa in (3, 4): #Si placa es 3 o 4, se incrementa el contador de carros rosas
        rosa += 1
    elif placa in (5, 6): #Si placa es 5 o 6, se incrementa el contador de carros rojos
        roja += 1
    elif placa in (7, 8): #Si placa es 7 o 8, se incrementa el contador de carros verdes
        verde += 1
    elif placa in (9, 0): #Si placa es 9 o 0, se incrementa el contador de carros azules
        azul += 1

#Se imprimen los resultados, mostrando la cantidad de carros de cada color según el último número de la placa
print(f"autos amarillos: {amarilla}")
print(f"autos rosas: {rosa}")
print(f"autos rojos: {roja}")
print(f"autos verdes: {verde}")
print(f"autos azules: {azul}")