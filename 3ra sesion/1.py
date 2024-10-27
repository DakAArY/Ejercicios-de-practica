"""
Elevar un número a una potencia:
Escribe una función recursiva que tome dos argumentos: un número base y un exponente,
y devuelva el resultado de elevar el número base a la potencia del exponente.
"""

def potencia(base, exponente):
    # Caso base: cualquier número elevado a la potencia 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: multiplicar la base por el resultado de elevar la base a la potencia (exponente - 1)
    return base * potencia(base, exponente - 1) # el exponente se decrementa en cada llamada recursiva por que se va multiplicando por la base

def main():
    # Solicitar al usuario que ingrese la base y el exponente
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    # Calcular la potencia
    resultado = potencia(base, exponente)
    # Mostrar el resultado
    print(f"{base} elevado a la potencia {exponente} es: {resultado}")

if __name__ == "__main__":
    main()