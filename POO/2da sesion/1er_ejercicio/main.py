"""
Script principal que integra los módulos y proporciona una interfaz por consola.
"""
from biblioteca import Biblioteca

def mostrar_menu():
    """Muestra las opciones del menú"""
    print("\n=== SISTEMA DE BIBLIOTECA UNIVERSITARIA ===")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Listar todos los libros")
    print("5. Registrar usuario")
    print("6. Prestar libro")
    print("7. Devolver libro")
    print("8. Ver préstamos de usuario")
    print("9. Listar usuarios")
    print("0. Salir")

def main():
    """Función principal del programa"""
    # Creación del objeto biblioteca
    biblioteca = Biblioteca("Biblioteca Central Universitaria")
    
    print(f"Bienvenido a {biblioteca.nombre}")
    
    # Agregar algunos datos de ejemplo
    biblioteca.agregar_libro("9780451524935", "1984", "George Orwell")
    biblioteca.agregar_libro("9780061120084", "Matar a un ruiseñor", "Harper Lee")
    biblioteca.registrar_usuario("Juan Pérez", "juan@ejemplo.com", "estudiante", "Informática")
    biblioteca.registrar_usuario("Ana García", "ana@ejemplo.com")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            print(biblioteca.agregar_libro(isbn, titulo, autor))
        
        elif opcion == "2":
            tipo_busqueda = input("Buscar por (1: ISBN, 2: Título): ")
            if tipo_busqueda == "1":
                isbn = input("ISBN: ")
                libro = biblioteca.buscar_libro(isbn=isbn)
            else:
                titulo = input("Título: ")
                libro = biblioteca.buscar_libro(titulo=titulo)
                
            if libro:
                print(libro.mostrar_info(detallado=True))
            else:
                print("Libro no encontrado")
        
        elif opcion == "3":
            isbn = input("ISBN del libro a eliminar: ")
            print(biblioteca.eliminar_libro(isbn))
        
        elif opcion == "4":
            print(biblioteca.listar_libros())
        
        elif opcion == "5":
            nombre = input("Nombre: ")
            email = input("Email: ")
            tipo = input("Tipo (normal/estudiante): ")
            carrera = input("Carrera (solo para estudiantes): ") if tipo.lower() == "estudiante" else None
            print(biblioteca.registrar_usuario(nombre, email, tipo, carrera))
        
        elif opcion == "6":
            isbn = input("ISBN del libro: ")
            nombre = input("Nombre del usuario: ")
            print(biblioteca.prestar_libro(isbn, nombre))
        
        elif opcion == "7":
            isbn = input("ISBN del libro: ")
            nombre = input("Nombre del usuario: ")
            print(biblioteca.devolver_libro(isbn, nombre))
        
        elif opcion == "8":
            nombre = input("Nombre del usuario: ")
            usuario = biblioteca.buscar_usuario(nombre)
            if usuario:
                print(usuario.listar_prestamos())
            else:
                print("Usuario no encontrado")
        
        elif opcion == "9":
            print(biblioteca.listar_usuarios())
        
        elif opcion == "0":
            print("¡Gracias por usar el sistema de biblioteca!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()