"""
Dividir una lista en dos partes:
Escribe una función recursiva que tome una lista y un índice, y devuelva dos 
listas: una con los elementos antes del índice y otra con los elementos desde 
el índice en adelante.
"""

def main():
    def dividir_lista(lista, indice):
        # Caso base: si el índice es 0, devolver dos listas: una vacía y la lista original
        if indice == 0:
            return [], lista
        # Caso recursivo: tomar el primer elemento y llamar recursivamente con el resto de la lista y el índice decrementado
        primera_parte, segunda_parte = dividir_lista(lista[1:], indice - 1)
        return [lista[0]] + primera_parte, segunda_parte
    
    # Solicitar al usuario que ingrese una lista de números
    numeros = input("Ingrese una lista de números separados por comas: ").split(',')
    # Convertir los elementos de la lista a enteros
    numeros = [int(num) for num in numeros]
    # Solicitar al usuario que ingrese el índice
    indice = int(input("Ingrese el índice para dividir la lista: "))
    # Dividir la lista en dos partes
    primera_parte, segunda_parte = dividir_lista(numeros, indice)
    # Mostrar el resultado
    print(f"La primera parte de la lista es: {primera_parte}")
    print(f"La segunda parte de la lista es: {segunda_parte}")

if __name__ == "__main__":
    main()