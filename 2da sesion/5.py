"""
Dividir una lista en dos partes:
Escribe una función recursiva que tome una lista y un índice, y devuelva dos 
listas: una con los elementos antes del índice y otra con los elementos desde 
el índice en adelante.
"""

def main():
    def dividir_lista(lista, indice):
        if indice == 0:
            return [], lista
        
        primera_parte, segunda_parte = dividir_lista(lista[1:], indice - 1)
        return [lista[0]] + primera_parte, segunda_parte
    
    numeros = input("Ingrese una lista de numeros separados por comas: ").split(",")
    numeros = [int(num) for num in numeros]
    
    indice = int(input("Ingrese el indice en el que se dividira la lista: "))
    
    primera_parte, segunda_parte = dividir_lista(numeros, indice)
    
    print(f"La primera parte de la lista es: {primera_parte}")
    print(f"La segunda parte de la lista es: {segunda_parte}")

if __name__ == "__main__":
    main()