# Importamos todas las clases necesarias
from contenido import ContenidoMultimedia, Pelicula, Serie
from plataforma import PlataformaStreaming

def mostrar_menu():
    print("\n===== NETFLIX SIMULATOR =====")
    print("1. Ver catálogo de películas")
    print("2. Ver catálogo de series")
    print("3. Buscar contenido")
    print("4. Agregar película")
    print("5. Agregar serie")
    print("6. Reproducir contenido")
    print("7. Calificar contenido")
    print("8. Obtener recomendación")
    print("9. Salir")

def main():
    # Creamos una plataforma de streaming
    plataforma = PlataformaStreaming("StreamFlix")
    
    # Agregamos contenido de ejemplo
    plataforma.agregar_contenido(Pelicula("El Padrino", "Drama", 1972, "Francis Ford Coppola", 175, 4.9))
    plataforma.agregar_contenido(Pelicula("Interestelar", "Ciencia Ficción", 2014, "Christopher Nolan", 169, 4.7))
    plataforma.agregar_contenido(Serie("Breaking Bad", "Drama", 2008, "Vince Gilligan", 5, 62, 4.8))
    plataforma.agregar_contenido(Serie("Stranger Things", "Ciencia Ficción", 2016, "Hermanos Duffer", 4, 34, 4.5))
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            # Mostrar películas
            catalogo = plataforma.listar_por_tipo()
            print("\n--- PELÍCULAS DISPONIBLES ---")
            for i, pelicula in enumerate(catalogo["peliculas"], 1):
                print(f"{i}. {pelicula.mostrar_info()}")
                
        elif opcion == "2":
            # Mostrar series
            catalogo = plataforma.listar_por_tipo()
            print("\n--- SERIES DISPONIBLES ---")
            for i, serie in enumerate(catalogo["series"], 1):
                print(f"{i}. {serie.mostrar_info()}")
                
        elif opcion == "3":
            # Buscar contenido
            termino = input("¿Qué estás buscando? ")
            resultados = plataforma.buscar(termino)
            
            if resultados:
                print(f"\nSe encontraron {len(resultados)} resultados:")
                for i, item in enumerate(resultados, 1):
                    print(f"{i}. {item.mostrar_info()}")
            else:
                print("No se encontraron resultados")
                
        elif opcion == "4":
            # Agregar película
            titulo = input("Título: ")
            genero = input("Género: ")
            año = int(input("Año: "))
            director = input("Director: ")
            duracion = int(input("Duración (minutos): "))
            
            pelicula = Pelicula(titulo, genero, año, director, duracion)
            print(plataforma.agregar_contenido(pelicula))
            
        elif opcion == "5":
            # Agregar serie
            titulo = input("Título: ")
            genero = input("Género: ")
            año = int(input("Año: "))
            creador = input("Creador: ")
            temporadas = int(input("Temporadas: "))
            episodios = int(input("Episodios totales: "))
            
            serie = Serie(titulo, genero, año, creador, temporadas, episodios)
            print(plataforma.agregar_contenido(serie))
            
        elif opcion == "6":
            # Reproducir contenido
            catalogo = plataforma.catalogo
            print("\n--- CONTENIDO DISPONIBLE ---")
            for i, item in enumerate(catalogo, 1):
                print(f"{i}. {item.titulo}")
                
            seleccion = int(input("Seleccione número: ")) - 1
            if 0 <= seleccion < len(catalogo):
                print(catalogo[seleccion].reproducir())
                # Muestra info específica según tipo de contenido
                if isinstance(catalogo[seleccion], Pelicula):
                    print(catalogo[seleccion].tiempo_restante(0))
            else:
                print("Selección no válida")
                
        elif opcion == "7":
            # Calificar contenido
            catalogo = plataforma.catalogo
            print("\n--- CALIFICAR CONTENIDO ---")
            for i, item in enumerate(catalogo, 1):
                print(f"{i}. {item.titulo}")
                
            seleccion = int(input("Seleccione número: ")) - 1
            if 0 <= seleccion < len(catalogo):
                puntuacion = float(input("Calificación (0-5): "))
                print(catalogo[seleccion].calificar(puntuacion))
            else:
                print("Selección no válida")
                
        elif opcion == "8":
            # Obtener recomendación
            recomendacion = plataforma.recomendar()
            print("\n--- RECOMENDACIÓN DEL DÍA ---")
            print(recomendacion.mostrar_info())
            print(f"Calificación: {recomendacion.calificacion}/5")
            
        elif opcion == "9":
            print("¡Gracias por usar StreamFlix!")
            break
            
        else:
            print("Opción no válida")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()