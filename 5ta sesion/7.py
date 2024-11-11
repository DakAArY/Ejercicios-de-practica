"""
Ejercicio 7: Contador de Palabras
Descripción: Cuenta la frecuencia de cada palabra en un texto.
"""

def contar_palabras(texto):
    # Convierte el texto a minúsculas y lo divide en palabras
    # lower() convierte todo a minúsculas
    # split() separa el texto en palabras usando espacios
    palabras = texto.lower().split()
    
    # Diccionario para almacenar las frecuencias
    frecuencias = {}

    # Recorre cada palabra y cuenta su frecuencia
    for palabra in palabras:
        # get() obtiene el valor actual o 0 si no existe la palabra
        # Suma 1 a la frecuencia existente
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    # Retorna el diccionario con las frecuencias
    return frecuencias

def main():
    # Solicita el texto al usuario
    texto = input("Ingrese un texto: ")
    
    # Obtiene el diccionario de frecuencias
    frecuencias = contar_palabras(texto)

    # Muestra los resultados ordenados alfabéticamente
    # sorted() ordena las palabras
    # items() obtiene pares (palabra, frecuencia)
    for palabra, freq in sorted(frecuencias.items()):
        print(f"'{palabra}': {freq} veces")

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
