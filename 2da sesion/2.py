"""
2. Búsqueda de un elemento en una lista:
Escribe una función recursiva que tome una lista y un elemento, y devuelva True
si el elemento está en la lista y False en caso contrario.
"""

def main():
    def buscar_elemento(lista, elemento):
        # Caso base: si la lista está vacía, devolver False
        if not lista:
            return False
        # Si el primer elemento de la lista es el elemento buscado, devolver True
        if lista[0] == elemento:
            return True
        # Caso recursivo: buscar en el resto de la lista
        return buscar_elemento(lista[1:], elemento)
    
    # Solicitar al usuario que ingrese una lista de números
    numeros = input("Ingrese una lista de números separados por comas: ").split(',')
    # Convertir los elementos de la lista a enteros
    numeros = [int(num) for num in numeros]
    # Solicitar al usuario que ingrese el elemento a buscar
    elemento = int(input("Ingrese el elemento a buscar: "))
    # Buscar el elemento en la lista
    encontrado = buscar_elemento(numeros, elemento)
    # Mostrar el resultado
    if encontrado:
        print(f"El elemento {elemento} está en la lista.")
    else:
        print(f"El elemento {elemento} no está en la lista.")

if __name__ == "__main__":
    main()