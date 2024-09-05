positivos = 0 #variable para determinar numeros positivos empezando desde 0
negativos = 0 #variable para determinar numeros negativos empezando desde 0
neutros = 0 #variable para determinar numeros neutros empezando desde 0

for i in range (20): #Bucle con un limite de 20 veces en las cuales el usuario colocara los numeros correspondientes tanto positivos, negativos y neutros
    numero = int(input("Ingresa un numero: ")) #se solicita al usuario que ingrese un número, el número ingresado se convierte de cadena a entero con int

    if numero < 0: #Los numeros ingresados se contaran desde 0 en adelante
        negativos += 1 #Si el número ingresado es menor que 0, se incrementa el contador negativos
    elif numero > 1: #Los numeros negativos seran menores a 1+
        positivos += 1 #Si el número ingresado es mayor que 1, se incrementa el contador positivos
    elif numero == 0 or 1: #Los numeros negativos seran mayores a 1+
        neutros += 1 #Si el número es 0 o 1, se incrementa el contador neutros

print(f"Numeros positivos : {positivos}") #se imprimen la cantidad de numeros positivos que se ingresaron
print(f"Numeros negativos: {negativos}") #se imprimen la cantidad de numeros negativos que se ingresaron
print(f"Numeros neutros: {neutros}") #se imprimen la cantidad de numeros neutros que se ingresaron