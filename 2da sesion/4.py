"""
Eliminar elementos duplicados de una lista:
Escribe una función recursiva que tome una lista y devuelva una nueva lista sin 
elementos duplicados.
"""

def main():
    def eliminar_duplicados(lista):
        # Caso base: si la lista está vacía, devolver una lista vacía
        if not lista:
            return []
        # Caso recursivo: si el primer elemento no está en el resto de la lista, incluirlo
        if lista[0] not in lista[1:]:
            return [lista[0]] + eliminar_duplicados(lista[1:])
        # Si el primer elemento está en el resto de la lista, omitirlo
        return eliminar_duplicados(lista[1:])
    
    # Solicitar al usuario que ingrese una lista de números
    numeros = input("Ingrese una lista de números separados por comas: ").split(',')
    # Convertir los elementos de la lista a enteros
    numeros = [int(num) for num in numeros]
    # Eliminar duplicados de la lista
    lista_sin_duplicados = eliminar_duplicados(numeros)
    # Mostrar el resultado
    print(f"La lista sin duplicados es: {lista_sin_duplicados}")

if __name__ == "__main__":
    main()  