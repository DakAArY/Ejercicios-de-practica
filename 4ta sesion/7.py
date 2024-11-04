"""
Ejercicio 7: Generar todas las permutaciones de una cadena
Descripción: Esta función recursiva genera todas las permutaciones posibles de una cadena.
"""

def permutaciones(cadena):
    # Caso base: si la cadena tiene un solo carácter
    if len(cadena) == 1:
        return [cadena]
    # Lista para almacenar las permutaciones
    perms = []
    # Recorrer cada carácter en la cadena
    for i, char in enumerate(cadena):
        # Obtener las permutaciones del resto de la cadena
        for perm in permutaciones(cadena[:i] + cadena[i+1:]):
            # Agregar el carácter actual al inicio de cada permutación
            perms.append(char + perm)
    return perms

def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena: ")
    # Generar todas las permutaciones de la cadena
    resultado = permutaciones(cadena)
    # Mostrar el resultado
    print(f"Las permutaciones de la cadena son: {resultado}")

if __name__ == "__main__":
    main()