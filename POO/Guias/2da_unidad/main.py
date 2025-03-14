# Importamos las clases que vamos a utilizar
from tarea import Tarea
from usuario import Usuario
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    # Detecta el sistema operativo y usa el comando apropiado
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal del programa."""
    print("\n=== SISTEMA DE GESTIÓN DE TAREAS ===")
    print("1. Crear una nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Ver tareas pendientes")
    print("4. Completar una tarea")
    print("5. Cambiar prioridad de una tarea")
    print("6. Ver estadísticas")
    print("7. Ver información detallada de tareas")
    print("8. Salir")
    return input("Seleccione una opción (1-8): ")

def crear_tarea(usuario):
    """Permite al usuario crear una nueva tarea."""
    print("\n--- Crear nueva tarea ---")
    titulo = input("Título de la tarea: ")
    
    # Validación de prioridad
    while True:
        prioridad = input("Prioridad (alta/media/baja) [media]: ").lower()
        if prioridad == "":
            prioridad = "media"
        if prioridad in ["alta", "media", "baja"]:
            break
        print("Error: La prioridad debe ser alta, media o baja.")
    
    fecha = input("Fecha límite (formato DD/MM/YYYY) [opcional]: ")
    if fecha.strip() == "":
        fecha = None
    
    # Crear la tarea y agregarla al usuario
    nueva_tarea = Tarea(titulo, prioridad, fecha)
    usuario.agregar_tarea(nueva_tarea)
    
    input("\nPresione Enter para continuar...")

def ver_tareas(usuario, solo_pendientes=False):
    """Muestra las tareas del usuario."""
    limpiar_pantalla()
    print("\n--- Lista de tareas ---")
    usuario.listar_tareas(solo_pendientes)
    input("\nPresione Enter para continuar...")

def completar_tarea(usuario):
    """Permite al usuario marcar una tarea como completada."""
    limpiar_pantalla()
    print("\n--- Completar una tarea ---")
    # Mostramos solo las tareas pendientes
    usuario.listar_tareas(solo_pendientes=True)
    
    titulo = input("\nIntroduce el título exacto de la tarea a completar (o Enter para cancelar): ")
    if titulo.strip():
        usuario.completar_tarea(titulo)
    
    input("\nPresione Enter para continuar...")

def cambiar_prioridad(usuario):
    """Permite cambiar la prioridad de una tarea."""
    limpiar_pantalla()
    print("\n--- Cambiar prioridad de una tarea ---")
    usuario.listar_tareas()
    
    titulo = input("\nIntroduce el título exacto de la tarea (o Enter para cancelar): ")
    if not titulo.strip():
        return
    
    tarea = usuario.buscar_tarea(titulo)
    if tarea:
        while True:
            nueva_prioridad = input("Nueva prioridad (alta/media/baja): ").lower()
            if nueva_prioridad in ["alta", "media", "baja"]:
                if tarea.cambiar_prioridad(nueva_prioridad):
                    print(f"Prioridad cambiada: {tarea.mostrar_info()}")
                break
            print("Error: La prioridad debe ser alta, media o baja.")
    else:
        print(f"No se encontró la tarea '{titulo}'")
    
    input("\nPresione Enter para continuar...")

def mostrar_estadisticas(usuario):
    """Muestra las estadísticas de las tareas del usuario."""
    limpiar_pantalla()
    print("\n--- Estadísticas de tareas ---")
    stats = usuario.obtener_estadisticas()
    
    if stats["total"] == 0:
        print("No hay tareas registradas.")
    else:
        print(f"Total de tareas: {stats['total']}")
        print(f"Tareas completadas: {stats['completadas']} ({stats['porcentaje_completado']:.1f}%)")
        print(f"Tareas pendientes: {stats['pendientes']}")
        print("Por prioridad:")
        print(f"  - Alta: {stats['por_prioridad']['alta']}")
        print(f"  - Media: {stats['por_prioridad']['media']}")
        print(f"  - Baja: {stats['por_prioridad']['baja']}")
    
    input("\nPresione Enter para continuar...")

def ver_informacion_detallada(usuario):
    """Muestra información detallada de todas las tareas."""
    limpiar_pantalla()
    print("\n--- Información detallada de tareas ---")
    
    if not usuario.tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(usuario.tareas, 1):
            print(f"{i}. {tarea.mostrar_info(True)}")
    
    input("\nPresione Enter para continuar...")

def main():
    """Función principal que ejecuta el sistema interactivo."""
    limpiar_pantalla()
    print("=== BIENVENIDO AL SISTEMA DE GESTIÓN DE TAREAS ===")
    
    # Pedimos información del usuario
    nombre = input("Introduce tu nombre: ")
    email = input("Introduce tu email (opcional): ") or None
    
    # Creación del usuario
    usuario = Usuario(nombre, email)
    
    # Menú principal
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu()
        
        if opcion == '1':
            crear_tarea(usuario)
        elif opcion == '2':
            ver_tareas(usuario)
        elif opcion == '3':
            ver_tareas(usuario, solo_pendientes=True)
        elif opcion == '4':
            completar_tarea(usuario)
        elif opcion == '5':
            cambiar_prioridad(usuario)
        elif opcion == '6':
            mostrar_estadisticas(usuario)
        elif opcion == '7':
            ver_informacion_detallada(usuario)
        elif opcion == '8':
            break
        else:
            input("Opción no válida. Presione Enter para continuar...")
    
    print("\n=== Gracias por usar el Sistema de Gestión de Tareas ===")
    print(f"Adiós, {usuario.nombre}!")

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    main()