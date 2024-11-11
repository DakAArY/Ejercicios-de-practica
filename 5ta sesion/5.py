"""
Ejercicio 5: Búsqueda de Patrones
Descripción: Encuentra todas las ocurrencias de un patrón en una cadena.
"""

def buscar_patron(texto, patron):
    # Lista para almacenar las posiciones donde se encuentra el patrón
    posiciones = []
    # Variable para rastrear la posición actual de búsqueda
    posicion = 0

    # Bucle que continúa mientras se encuentren coincidencias
    while True:
        # find() busca el patrón a partir de la posición actual
        # Retorna -1 si no encuentra el patrón
        pos = texto.find(patron, posicion)

        # Si no se encuentra el patrón, termina el bucle
        if pos == -1:
            break
        # Agrega la posición encontrada a la lista
        posiciones.append(pos)
        # Actualiza la posición de búsqueda para la siguiente iteración
        # Se suma 1 para evitar encontrar el mismo patrón repetidamente
        posicion = pos + 1

    # Retorna la lista con todas las posiciones encontradas
    return posiciones

def main():
    # Solicita al usuario el texto donde buscar
    texto = input("Ingrese un texto: ")
    # Solicita el patrón a buscar
    patron = input("Ingrese un patron a buscar: ")
    # Llama a la función de búsqueda
    posiciones = buscar_patron(texto, patron)
    # Muestra los resultados: posiciones y cantidad de ocurrencias
    print(f"El patron aparece en las posiciones: {posiciones}")
    print(f"Cantidad de ocurrencias: {len(posiciones)}")

if __name__ == "__main__":
    main()
