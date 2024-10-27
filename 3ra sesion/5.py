"""
Contar elementos mayores que un valor en una lista:
Escribe una función recursiva que tome una lista y un valor, y devuelva el número
de elementos en la lista que son mayores que el valor dado.
"""

def contar_mayores(lista, valor):
    # Caso base: si la lista está vacía, devolver 0
    if not lista:
        return 0
    # Caso recursivo: si el primer elemento es mayor que el valor, contar 1 y llamar recursivamente con el resto de la lista
    if lista[0] > valor:
        return 1 + contar_mayores(lista[1:], valor)
    # Si el primer elemento no es mayor que el valor, no contar y llamar recursivamente con el resto de la lista
    return contar_mayores(lista[1:], valor)

def main():
    # Solicitar al usuario que ingrese una lista de números y un valor
    lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(',')))
    valor = int(input("Ingrese el valor: "))
    # Contar los elementos mayores que el valor en la lista
    resultado = contar_mayores(lista, valor)
    # Mostrar el resultado
    print(f"El número de elementos mayores que {valor} es: {resultado}")

if __name__ == "__main__":
    main()