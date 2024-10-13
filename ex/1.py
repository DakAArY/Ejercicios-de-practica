#1. Implementa una función recursiva que calcule la suma de los dígitos de un número entero. Luego, crea una función iterativa que repita este proceso hasta que el resultado sea un solo dígito (también conocido como raíz digital). Por ejemplo, para 678: 6+7+8=21, 2+1=3.

def main():
    def suma_digitos(n):
        if n < 10:
            return n
        
        return n % 10 + suma_digitos(n // 10)
    
    n = int(input("Ingresa un numero positivo: "))
    
    if n <= 0:
        print("El numero no es valido, por favor ingresa un numero positivo.")
    else:
        result = suma_digitos(n)
        print(f"La suma de los digitos de {n} es {result}")

if __name__ == "__main__":
    main()