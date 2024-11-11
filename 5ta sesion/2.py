"""
Ejercicio 2: Estadísticas de Tupla
Descripción: Calcula estadísticas básicas de una tupla de números.
"""

def calcular_estadisticas(numeros):
    # Calcula el promedio sumando todos los números y dividiendo entre la cantidad
    # sum() suma todos los elementos y len() obtiene la cantidad
    promedio = sum(numeros)/len(numeros)

    # Encuentra el elemento que más se repite (moda)
    # set() obtiene valores únicos
    # max() encuentra el máximo usando como criterio la cantidad de repeticiones
    # key=numeros.count indica que use el conteo de repeticiones como criterio
    mas_comun = max(set(numeros), key=numeros.count)

    # Cuenta cuántos números pares hay en la tupla
    # Usa una comprensión de lista que cuenta 1 por cada número par encontrado
    # n % 2 == 0 verifica si el número es par (divisible entre 2)
    pares = sum(1 for n in numeros if n % 2 == 0)
    
    # Retorna una tupla con los tres valores calculados
    return promedio, mas_comun, pares

def main():
    # Obtiene entrada del usuario y la convierte en tupla de enteros
    # split() separa la entrada por espacios
    # map(int, ...) convierte cada elemento a entero
    # tuple() convierte la lista resultante en tupla
    numeros = tuple(map(int, input("Ingrese numeros separados por espacio: ").split()))

    # Llama a la función y desempaqueta los resultados
    promedio, comun, pares = calcular_estadisticas(numeros)

    # Imprime los resultados formateados
    # :.2f formatea el promedio a 2 decimales
    print(f"Promedio: {promedio:.2f}")
    print(f"Valor mas comun: {comun}")
    print(f"Cantidad de pares: {pares}")

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()


