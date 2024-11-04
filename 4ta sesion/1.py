"""
Ejercicio 1: Contar vocales en una cadena
Descripción: Esta función cuenta el número de vocales en una cadena dada.
"""

def contar_vocales(cadena):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    # Inicializar el contador
    contador = 0
    # Recorrer cada carácter en la cadena
    for char in cadena:
        # Si el carácter es una vocal, incrementar el contador
        if char in vocales:
            contador += 1
    return contador

def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena: ")
    # Contar las vocales en la cadena
    resultado = contar_vocales(cadena)
    # Mostrar el resultado
    print(f"El número de vocales en la cadena es: {resultado}")

if __name__ == "__main__":
    main()