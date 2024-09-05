numero = int(input("Ingresa el numero: ")) #Se solicita al usuario que ingrese un número, el cual se convierte de cadena a entero usando int()

for i in range (1, 11): #Se inicia un bucle for que iterará desde 1 hasta 10 (inclusive)
    resultado = numero * i #Se calcula el producto del numero ingresado por el usuario y el valor actual de i

    print (f"{numero} x {i} = {resultado}") #Se imprime una línea que muestra la multiplicación actual en formato de tabla de multiplicar
