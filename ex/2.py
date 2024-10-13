#Desarrolla que implemente un algoritmo de Euclides para encontrar
#el máximo común divisor de dos números enteros positivos.

def main():
    #Se define una funcion recursiva que calcula el MCD de dos numeros
    def mcd(a, b):
        #Caso base: si b es igual a 0, se retorna a
        if b == 0:
            return a
        
        #Se retorna el MCD de b y el residuo de a entre b
        return mcd(b, a % b)
    
    #Se pide al usuario que ingrese dos numeros positivos
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese  el segundo numero: "))
    
    #Se validan los numeros ingresados
    if num1 <= 0 or num2 <= 0:
        print("por favor ingrese un numero valido")
    else:
        #Se calcula el MCD de los numeros ingresados
        result = mcd(num1, num2)
        print(f"El MCD de {num1} y {num2} es: {result}")

if  __name__ == "__main__":
    main()