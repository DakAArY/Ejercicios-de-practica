#Escribir un algoritmo que genere los primeros n numeros
#de la secuencia de fibonacci

def main():
    def fibonacci(n):
        if n <= 1:
            return n
        
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    def secuencia(n):
        return [fibonacci(i) for i in range(n)]
    
    n = int(input("Ingrese los numeros a generar de la secuencia de fibonacci: "))
    
    if n <= 0:
        print("Ingrese un numero positivo")
    else:
        fib_seq = secuencia(n)
        print(f"los primeros {n} numeros son: {fib_seq}")

if __name__  == "__main__":
    main()