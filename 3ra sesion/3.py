"""
Encontrar el segundo mínimo en una lista:
Escribe una función recursiva que tome una lista de números y devuelva el
segundo número mínimo en la lista.
"""

def segundo_minimo(lista):
    # Caso base: si la lista tiene menos de 2 elementos, no se puede encontrar el segundo mínimo
    if len(lista) < 2:
        return None
    # Encontrar el mínimo de la lista
    minimo = min(lista)
    # Eliminar todas las ocurrencias del mínimo
    lista_sin_minimo = [x for x in lista if x != minimo]
    # Caso recursivo: encontrar el mínimo de la lista sin el mínimo original
    return min(lista_sin_minimo)

def main():
    # Solicitar al usuario que ingrese una lista de números
    lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(',')))
    # Encontrar el segundo mínimo
    resultado = segundo_minimo(lista)
    # Mostrar el resultado
    if resultado is not None:
        print(f"El segundo mínimo de la lista es: {resultado}")
    else:
        print("La lista no tiene suficientes elementos para encontrar el segundo mínimo.")

if __name__ == "__main__":
    main()