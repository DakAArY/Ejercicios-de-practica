"""
Ejercicio 8: Filtrado de Tuplas
Descripción: Filtra elementos de una tupla según un criterio.
"""

def filtrar_tupla(tupla, minimo, maximo):
    # Utiliza una comprensión de tupla para filtrar elementos
    # x for x in tupla -> itera sobre cada elemento de la tupla
    # if minimo <= x <= maximo -> solo incluye elementos en el rango
    # tuple() convierte la expresión generadora en una tupla
    return tuple(x for x in tupla if minimo <= x <= maximo)

def main():
    # Obtiene números del usuario y los convierte en tupla
    # input() obtiene la entrada como texto
    # split() divide el texto en elementos por espacios
    # map(float, ...) convierte cada elemento a número decimal
    # tuple() convierte el resultado en una tupla
    numeros = tuple(map(float, input("Ingrese numeros separados por espacios: ").split()))

    # Obtiene los valores límite del rango
    # float() convierte la entrada en número decimal
    min_val = float(input("Ingrese el valor minimo: "))
    max_val = float(input("Ingrese el valor maximo: "))

    # Filtra la tupla y muestra el resultado
    resultado = filtrar_tupla(numeros, min_val, max_val)
    print(f"Numeros filtrados: {resultado}")

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
