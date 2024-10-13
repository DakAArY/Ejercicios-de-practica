#Escribir un algoritmo que genere los primeros n numeros
#de la secuencia de fibonacci

def main():
    #Se define una funcion recursiva que calcula el n-esimo numero de fibonacci
    def fibonacci(n):
        #Caso base: si n es menor o igual a 1, se retorna n
        if n <= 1:
            return n
        
        #Se retorna la suma de los dos numeros anteriores
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    #Se define una funcion que genera los primeros n numeros de la secuencia de fibonacci
    def secuencia(n):
        #Se retorna una lista con los n primeros numeros de fibonacci
        return [fibonacci(i) for i in range(n)]
    
    #Se pide al usuario que ingrese un numero positivo
    n = int(input("Ingrese los numeros a generar de la secuencia de fibonacci: "))
    
    #Se valida que el numero sea positivo
    if n <= 0:
        print("Ingrese un numero positivo")
    else:
        #Se generan los primeros n numeros de la secuencia de fibonacci
        fib_seq = secuencia(n)
        print(f"los primeros {n} numeros son: {fib_seq}")

if __name__  == "__main__":
    main()