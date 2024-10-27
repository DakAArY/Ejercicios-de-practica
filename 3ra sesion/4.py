"""
Eliminar elementos pares de una lista:
Escribe una función recursiva que tome una lista de números y devuelva 
una nueva lista sin los elementos pares.
"""

def eliminar_pares(lista):
    # Caso base: si la lista está vacía, devolver una lista vacía
    if not lista:
        return []
    # Caso recursivo: si el primer elemento es impar, incluirlo en la lista resultante
    if lista[0] % 2 != 0:
        return [lista[0]] + eliminar_pares(lista[1:])
    # Si el primer elemento es par, omitirlo
    return eliminar_pares(lista[1:])

def main():
    # Solicitar al usuario que ingrese una lista de números
    lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(',')))
    # Eliminar los elementos pares de la lista
    resultado = eliminar_pares(lista)
    # Mostrar el resultado
    print(f"La lista sin elementos pares es: {resultado}")

if __name__ == "__main__":
    main()