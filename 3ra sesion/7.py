"""
Encontrar subsecuencias que sumen a un valor objetivo:
Escribe una función recursiva que tome una lista de números y un valor objetivo,
y devuelva una lista de listas con todas las subsecuencias de la lista original
que sumen al valor objetivo.

"""

def subsecuencias_que_suman(lista, objetivo):
    # Caso base: si la lista está vacía, devolver una lista vacía si el objetivo es 0, de lo contrario devolver una lista vacía
    if not lista:
        return [[]] if objetivo == 0 else []
    # Caso recursivo: encontrar subsecuencias sin el primer elemento
    sin_primero = subsecuencias_que_suman(lista[1:], objetivo)
    # Encontrar subsecuencias con el primer elemento
    con_primero = [[lista[0]] + subseq for subseq in subsecuencias_que_suman(lista[1:], objetivo - lista[0])] #se llama a la funcion recursiva con el objetivo menos el primer elemento
    # Devolver la combinación de ambas
    return sin_primero + con_primero

def main():
    # Solicitar al usuario que ingrese una lista de números y un valor objetivo
    lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(',')))
    objetivo = int(input("Ingrese el valor objetivo: "))
    # Encontrar subsecuencias que sumen al valor objetivo
    resultado = subsecuencias_que_suman(lista, objetivo)
    # Mostrar el resultado
    print(f"Las subsecuencias que suman a {objetivo} son: {resultado}")

if __name__ == "__main__":
    main()