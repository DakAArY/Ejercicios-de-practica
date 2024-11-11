"""
Ejercicio 1: Validación de Correo Electrónico
Descripción: Verifica si una cadena tiene formato de correo electrónico básico.
"""

def validar_email(email):
    # Verifica si existe el símbolo @ en el email
    tiene_arroba = '@' in email
    
    # Busca la posición del @ y verifica si hay un punto después de esa posición
    # email.find('@') encuentra la posición del @
    # email[email.find('@'):] obtiene el substring desde @ hasta el final
    # '.' in ... verifica si existe un punto en ese substring
    tiene_punto = '.' in email[email.find('@'):]

    # Verifica que el email tenga al menos 5 caracteres
    # (mínimo necesario para algo como a@b.c)
    longitud_valida = len(email) >= 5
    
    # Verifica que el email no comience ni termine con @ o .
    # startswith() y endswith() comprueban el inicio y final
    # (('@', '.')) es una tupla con los caracteres a verificar
    extremos_validos = not email.startswith(('@', '.')) and not email.endswith(('@', '.'))

    # Retorna True solo si todas las condiciones son verdaderas
    return tiene_arroba and tiene_punto and longitud_valida and extremos_validos

def main():
    # Solicita al usuario que ingrese un email
    email = input("Ingrese un correo electronico: ")

    # Llama a la función validar_email y muestra el resultado
    if validar_email(email):
        print("El correo es valido")
    else:
        print("El correo no es valido")

# Verifica si el script se está ejecutando directamente
# (no siendo importado como módulo)
if __name__ == "__main__":
    main()



