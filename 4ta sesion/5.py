"""
Ejercicio 5: Palíndromo
Descripción: Esta función recursiva determina si una cadena es un palíndromo.
"""

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()
    # Caso base: si la cadena tiene 0 o 1 caracteres
    if len(cadena) <= 1:
        return True
    # Caso recursivo: comparar el primer y último carácter y verificar el resto
    return cadena[0] == cadena[-1] and es_palindromo(cadena[1:-1])

def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena: ")
    # Determinar si la cadena es un palíndromo
    resultado = es_palindromo(cadena)
    # Mostrar el resultado
    if resultado:
        print("La cadena es un palíndromo")
    else:
        print("La cadena no es un palíndromo")

if __name__ == "__main__":
    main()