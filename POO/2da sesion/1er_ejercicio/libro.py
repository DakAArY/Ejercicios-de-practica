"""
Módulo que contiene la clase Libro y sus funcionalidades.
"""

class Libro:
    """
    Clase que representa un libro en el sistema de biblioteca.
    
    Atributos:
        __isbn (str): Identificador único del libro. (Privado)
        __titulo (str): Título del libro. (Privado)
        __autor (str): Autor del libro. (Privado)
        __dispobible (bool): Estado de disponibilidad del libro. (Privado)
        prestamos (int): Número de veces que el libro ha sido prestado. (Público)
    """
    
    # Constructor: se llama automáticamente al crear un objeto de la clase.
    def __init__(self, isbn, titulo, autor):
        """
        Constructor de la clase Libro.
        Args:
            isbn (str): Identificador único del libro.
            titulo (str): Título del libro.
            autor (str): Autor del libro.
        """
        # Atributos encapsulados (privados) con doble guión bajo.
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True
        # Atributo público sin guión bajo.
        self.prestamos = 0
    
    # Destructor: se llama automáticamente al eliminar un objeto de la clase.
    def __del__(self):
        """
        Destructor de la clase Libro.
        Se ejecuta cuando el objeto es eliminado por el recolector de basura.
        """
        print(f"Libro '{self.__titulo}' eliminado del sistema.")
    
    # Metodo para prestar un libro
    def prestar(self):
        """
        Intenta prestar el libro si está disponible.
        Returns:
            str: Mensaje indicando el resultado de la operación.
        """
        if self.__disponible:
            self.__disponible = False
            self.prestamos += 1
            return f"Libro '{self.__titulo}' prestado exitosamente."
        else:
            return f"Libro '{self.__titulo}' no está disponible"
    
    # Metodo para devolver un libro
    def devolver(self):
        """
        Marca el libro como disponible.
        
        Returns:
            str: Mensaje confirmando la devolucion
        """
        if not self.__disponible:
            self.__disponible = True
            return f"Libro '{self.__titulo}' devuelto exitosamente"
        else:
            return f"El libro '{self.__titulo}' ya estaba disponible"
    
    # Sobrecarga del metodo __str__ para imprimir el objeto 
    def __str__(self):
        """
        Sobrecarga del metodo __str__ para representacion en string del objeto.
        
        Returns:
            str: Representacion del libro en formato legible
        """
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"Libro: {self.__titulo} | Autor: {self.__autor} | Estado: {estado}"

    # Metodo sobrecargado con diferentes parametros
    def mostrar_info(self, detallado=False):
        """
        Muestra informacion del libro, con sobrecarga por parametro opcional.
        
        Args:
            detallado (bool, opcional): si es True, muestra informacion detallada
            
        Returns:
            str: Informacion del libro segun el nivel de detalle solicitado
        """
        if detallado:
            return  f"ISBN: {self.__isbn}\nTitulo: {self.__titulo}\nAutor: {self.__autor}\n" \
                    f"Estado: {'Disponible' if self.__disponible else 'Prestado'}\n" \
                    f"Veces prestado: {self.prestamos}"
        else:
            return f"{self.__titulo} por {self.__autor}"
    
    # Getters y setters (propiedades)
    @property
    def titulo(self):
        """Getter para el titulo del libro"""
        return self.__titulo
    
    @property
    def autor(self):
        """Getter para el autor del libro"""
        return self.__autor
    
    @property
    def disponible(self):
        """Getter para el estado de disponibilidad"""
        return self.__disponible