negativo = 0 #variable llamada negativo y se inicializa en 0

for i in range (10): #bucle for se ejecutará 10 veces, pidiendo al usuario que ingrese un número en cada iteración
    numero = int(input("Ingresa un numero negativo: ")) #En cada impresion se le solicita al usuario que ingrese un número

    op = numero * -1 #Se multiplica el número ingresado por -1, lo cual convierte un número negativo a positivo
    negativo += op #Se suma el valor positivo a la variable negativo

print(f"El total de los numeros convertidos a positivo es: {negativo}") #El bucle termina, se imprime el total de los números convertidos a positivos