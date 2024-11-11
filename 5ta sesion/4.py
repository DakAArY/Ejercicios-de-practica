"""
Ejercicio 4: Combinación de Tuplas 
Descripción: Combina dos tuplas alternando sus elementos.
"""

def combinar_tuplas(tupla1, tupla2):
    # Obtiene la longitud de la tupla más larga
    # max() retorna el mayor valor entre las longitudes
    # len() obtiene la cantidad de elementos de cada tupla
    max_len = max(len(tupla1), len(tupla2))
    
    # Lista para ir almacenando los elementos combinados
    resultado = []

    # Itera hasta la longitud de la tupla más larga
    for i in range(max_len):
        # Si aún hay elementos en tupla1, agrega el elemento actual
        if i < len(tupla1):
            resultado.append(tupla1[i])
        # Si aún hay elementos en tupla2, agrega el elemento actual
        if i < len(tupla2):
            resultado.append(tupla2[i])

    # Convierte la lista resultante en tupla y la retorna
    return tuple(resultado)

def main():
    # Obtiene entrada del usuario para la primera tupla
    # split() divide la entrada en elementos separados por espacio
    # tuple() convierte la lista resultante en tupla
    t1 = tuple(input("Ingrese los valores de la primera tupla: ").split())
    
    # Obtiene entrada del usuario para la segunda tupla
    t2 = tuple(input("Ingrese los valores de la segunda tupla: ").split())

    # Muestra el resultado de combinar las tuplas
    print(f"Tupla combinada: {combinar_tuplas(t1, t2)}")

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
