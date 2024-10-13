#1. Implementa una función recursiva que calcule la suma de los dígitos de un número entero. Luego, crea una función iterativa que repita este proceso hasta que el resultado sea un solo dígito (también conocido como raíz digital). Por ejemplo, para 678: 6+7+8=21, 2+1=3.

def main():
    #Se define una funcion recursiva que calcula la suma de los digitos de un numero
    def suma_digitos(n):
        #Caso base: si el numero es menor a 10, se retorna el numero
        if n < 10:
            return n
        
        #Se retorna el ultimo digito del numero mas la suma de los digitos restantes
        return n % 10 + suma_digitos(n // 10)
    
    #Se pide al usuario que ingrese un numero positivo
    n = int(input("Ingresa un numero positivo: "))
    
    #Se valida que el numero sea positivo
    if n <= 0:
        print("El numero no es valido, por favor ingresa un numero positivo.")
    else:
        #Se calcula la suma de los digitos del numero ingresado
        result = suma_digitos(n)
        print(f"La suma de los digitos de {n} es {result}")

#Se llama a la funcion principal
if __name__ == "__main__":
    main()