"""
Ejercicio 2: Invertir una cadena
Descripción: Esta función recursiva invierte una cadena dada.
"""

def invertir_cadena(cadena):
    # Caso base: si la cadena está vacía o tiene un solo carácter
    if len(cadena) <= 1:
        return cadena
    # Caso recursivo: invertir el resto de la cadena y agregar el primer carácter al final
    return invertir_cadena(cadena[1:]) + cadena[0]

def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena: ")
    # Invertir la cadena
    resultado = invertir_cadena(cadena)
    # Mostrar el resultado
    print(f"La cadena invertida es: {resultado}")

if __name__ == "__main__":
    main()