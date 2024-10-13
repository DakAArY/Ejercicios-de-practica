#Desarrolla que implemente un algoritmo de Euclides para encontrar
#el máximo común divisor de dos números enteros positivos.

def main():
    def mcd(a, b):
        if b == 0:
            return a
        
        return mcd(b, a % b)
    
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese  el segundo numero: "))
    
    if num1 <= 0 or num2 <= 0:
        print("por favor ingrese un numero valido")
    else:
        result = mcd(num1, num2)
        print(f"El MCD de {num1} y {num2} es: {result}")

if  __name__ == "__main__":
    main()