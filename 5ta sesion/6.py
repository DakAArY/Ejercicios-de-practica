"""
Ejercicio 6: Rotación de Tuplas
Descripción: Rota los elementos de una tupla n posiciones.
"""

def rotar_tupla(tupla, n):
    # Normaliza n para que esté dentro del rango de la tupla
    # usando el operador módulo (%) para evitar rotaciones innecesarias
    # Ejemplo: si n=7 y len(tupla)=5, n será 2
    n = n % len(tupla)

    # Divide la tupla en dos partes y las recombina
    # tupla[n:] toma los elementos desde n hasta el final
    # tupla[:n] toma los elementos desde el inicio hasta n-1
    # El operador + concatena las dos partes
    return tupla[n:] + tupla[:n]

def main():
    # Obtiene los elementos de la tupla del usuario
    # split() divide la entrada por espacios
    # tuple() convierte la lista resultante en una tupla
    elementos = tuple(input("Ingrese elementos separados por espacio: ").split())
    
    # Obtiene el número de posiciones a rotar
    # int() convierte la entrada en un número entero
    n = int(input("Posiciones a rotar: "))
    
    # Muestra el resultado usando f-string
    print(f"Tupla rotada: {rotar_tupla(elementos, n)}")

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
