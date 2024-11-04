"""
Ejercicio 3: Eliminar caracteres duplicados
Descripción: Esta función elimina los caracteres duplicados en una cadena.
"""

def eliminar_duplicados(cadena):
    # Usar un conjunto para rastrear caracteres únicos
    caracteres_vistos = set()
    resultado = []
    # Recorrer cada carácter en la cadena
    for char in cadena:
        # Si el carácter no ha sido visto antes, agregarlo al resultado
        if char not in caracteres_vistos:
            caracteres_vistos.add(char)
            resultado.append(char)
    return ''.join(resultado)

def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena: ")
    # Eliminar los caracteres duplicados en la cadena
    resultado = eliminar_duplicados(cadena)
    # Mostrar el resultado
    print(f"La cadena sin caracteres duplicados es: {resultado}")

if __name__ == "__main__":
    main()