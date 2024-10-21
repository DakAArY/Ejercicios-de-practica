"""
Reversión de una lista:
    Escribe una función recursiva que tome una lista y devuelva una nueva lista
    con los elementos en orden inverso.
"""

def main():
    def revertir_lista(lista):
        # Caso base: si la lista está vacía, devolver una lista vacía
        if not lista:
            return []
        # Caso recursivo: tomar el último elemento y concatenarlo con la reversión del resto de la lista
        return [lista[-1]] + revertir_lista(lista[:-1])
    
    # Solicitar al usuario que ingrese una lista de números
    numeros = input("Ingrese una lista de números separados por comas: ").split(',')
    # Convertir los elementos de la lista a enteros
    numeros = [int(num) for num in numeros]
    # Revertir la lista
    lista_revertida = revertir_lista(numeros)
    # Mostrar el resultado
    print(f"La lista revertida es: {lista_revertida}")

if __name__ == "__main__":
    main()