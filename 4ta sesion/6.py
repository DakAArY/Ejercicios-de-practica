"""
Ejercicio 6: Encontrar la subcadena más larga sin caracteres repetidos
Descripción: Esta función encuentra la subcadena más larga en una cadena dada que no tenga caracteres repetidos.
"""

def subcadena_mas_larga(cadena):
    # Inicializar variables para rastrear la subcadena más larga
    inicio = 0
    max_len = 0
    max_subcadena = ""
    # Usar un diccionario para rastrear la última posición de cada carácter
    ultima_posicion = {}
    for i, char in enumerate(cadena):
        # Si el carácter ya fue visto y está dentro de la subcadena actual
        if char in ultima_posicion and ultima_posicion[char] >= inicio:
            inicio = ultima_posicion[char] + 1
        # Actualizar la última posición del carácter
        ultima_posicion[char] = i
        # Actualizar la subcadena más larga si es necesario
        if i - inicio + 1 > max_len:
            max_len = i - inicio + 1
            max_subcadena = cadena[inicio:i+1]
    return max_subcadena

def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena: ")
    # Encontrar la subcadena más larga sin caracteres repetidos
    resultado = subcadena_mas_larga(cadena)
    # Mostrar el resultado
    print(f"La subcadena más larga sin caracteres repetidos es: {resultado}")

if __name__ == "__main__":
    main()