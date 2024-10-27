"""
Suma de listas:

Escribe una función recursiva que tome dos listas de números y devuelva una nueva lista
donde cada elemento es la suma de los elementos correspondientes de las dos listas.
Si las listas tienen diferentes longitudes, los elementos faltantes se consideran como 0.
"""

def suma_listas(lista1, lista2):
    # Caso base: si ambas listas están vacías, devolver una lista vacía
    if not lista1 and not lista2:
        return []
    # Si una de las listas está vacía, considerar sus elementos como 0
    if not lista1:
        lista1 = [0]
    if not lista2:
        lista2 = [0]
    # Caso recursivo: sumar los primeros elementos de ambas listas y llamar recursivamente con el resto de las listas
    return [lista1[0] + lista2[0]] + suma_listas(lista1[1:], lista2[1:])

def main():
    # Solicitar al usuario que ingrese dos listas de números
    lista1 = list(map(int, input("Ingrese la primera lista de números separados por comas: ").split(',')))
    lista2 = list(map(int, input("Ingrese la segunda lista de números separados por comas: ").split(',')))
    # Calcular la suma de las listas
    resultado = suma_listas(lista1, lista2)
    # Mostrar el resultado
    print(f"La suma de las listas es: {resultado}")

if __name__ == "__main__":
    main()