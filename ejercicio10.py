valor = 1 #Se inicializa la variable valor en 1

for i in range(1, 21): #Se inicia un bucle for que itera sobre los números del 1 al 20
    valor *= i #En cada iteración del bucle, se multiplica el valor actual de valor por i y se almacena el resultado de nuevo en valor

print(f"El resultado de la multiplicación de 1 a 20 es: {valor}") #el bucle ha terminado, se imprime el resultado final almacenado en valor, que es el producto de todos los números desde 1 hasta 20