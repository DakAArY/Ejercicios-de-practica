"""
Ejercicio 3: Formateo de Nombres
Descripción: Formatea nombres según reglas específicas.
"""

def formatear_nombre(nombre):
    # Convierte el nombre completo a minúsculas y lo divide en partes
    # lower() convierte todo a minúsculas
    # split() separa el texto en una lista usando espacios como delimitador
    partes = nombre.lower().split()

    # Une las partes del nombre después de capitalizarlas
    # parte.capitalize() convierte la primera letra de cada parte a mayúscula
    # ' '.join() une las partes usando espacio como separador
    formateado = ' '.join(parte.capitalize() for parte in partes)

    # Elimina espacios extras al inicio y final del nombre
    # strip() remueve espacios en blanco de ambos extremos
    return formateado.strip()

def main():
    # Solicita al usuario que ingrese un nombre
    nombre = input("Ingrese un nombre: ")
    # Muestra el resultado formateado usando f-string
    print(f"Nombre formateado: {formatear_nombre(nombre)}")

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
