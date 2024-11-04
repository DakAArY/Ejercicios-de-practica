"""
Ejercicio 4: Contar palabras en una cadena
Descripción: Esta función cuenta el número de palabras en una cadena dada.
"""

def contar_palabras(cadena):
    # Dividir la cadena en palabras usando espacios como separadores
    palabras = cadena.split()
    # Contar el número de palabras
    return len(palabras)

def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena: ")
    # Contar las palabras en la cadena
    resultado = contar_palabras(cadena)
    # Mostrar el resultado
    print(f"El número de palabras en la cadena es: {resultado}")

if __name__ == "__main__":
    main()