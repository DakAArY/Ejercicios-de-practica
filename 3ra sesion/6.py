"""
Generar todas las combinaciones de una lista:
Escribe una función recursiva que tome una lista y devuelva una lista de listas
con todas las combinaciones posibles de los elementos de la lista.
"""

def combinaciones(lista):
    # Caso base: si la lista está vacía, devolver una lista que contiene una lista vacía
    if not lista:
        return [[]]
    # Caso recursivo: generar combinaciones sin el primer elemento
    #esto hace que se vaya eliminando el primer elemento de la lista 
    comb_sin_primero = combinaciones(lista[1:])
    # Generar combinaciones con el primer elemento
    comb_con_primero = [[lista[0]] + comb for comb in comb_sin_primero] #la lista esta en indice 0 por que se esta tomando el primer elemento
    # Devolver la combinación de ambas
    return comb_sin_primero + comb_con_primero

def main():
    # Solicitar al usuario que ingrese una lista de números
    #map se usa para aplicar una funcion a cada elemento de una lista
    #En este caso map se usa para convertir los elementos de la lista en enteros
    lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(',')))
    # Generar todas las combinaciones de la lista
    resultado = combinaciones(lista)
    # Mostrar el resultado
    print(f"Todas las combinaciones de la lista son: {resultado}")

if __name__ == "__main__":
    main()