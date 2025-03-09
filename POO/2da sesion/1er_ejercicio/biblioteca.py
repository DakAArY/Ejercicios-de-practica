"""
Módulo principal que contiene la clase Biblioteca que integra las funcionalidades.
"""
from libro import Libro
from usuario import Usuario, Estudiante

class Biblioteca:
    """
    Clase que administra la biblioteca y sus operaciones.
    
    Atributos:
        nombre (str): Nombre de la biblioteca
        __libros (dict): Diccionario de libros por ISBN (encapsulado)
        __usuarios (dict): Diccionario de usuarios por ID (encapsulado)
    """
    
    def __init__(self, nombre):
        """
        Constructor de la clase Biblioteca.
        
        Args:
            nombre (str): Nombre de la biblioteca
        """
        self.nombre = nombre
        self.__libros = {}
        self.__usuarios = {}
    
    def agregar_libro(self, isbn, titulo, autor):
        """
        Crea y agrega un nuevo libro a la biblioteca.
        
        Args:
            isbn (str): ISBN del libro
            titulo (str): Título del libro
            autor (str): Autor del libro
            
        Returns:
            str: Mensaje de confirmación o error
        """
        if isbn in self.__libros:
            return f"Ya existe un libro con ISBN {isbn}"
        
        nuevo_libro = Libro(isbn, titulo, autor)
        self.__libros[isbn] = nuevo_libro
        return f"Libro '{titulo}' agregado exitosamente"
    
    def eliminar_libro(self, isbn):
        """
        Elimina un libro de la biblioteca.
        
        Args:
            isbn (str): ISBN del libro a eliminar
            
        Returns:
            str: Mensaje de confirmación o error
        """
        if isbn in self.__libros:
            libro = self.__libros[isbn]
            del self.__libros[isbn]
            # Aquí el objeto libro quedará sin referencias y eventualmente
            # el recolector de basura de Python lo eliminará, llamando al
            # destructor __del__
            return f"Libro eliminado exitosamente"
        else:
            return f"No se encontró un libro con ISBN {isbn}"
    
    def registrar_usuario(self, nombre, email, tipo="normal", carrera=None):
        """
        Registra un nuevo usuario en la biblioteca.
        
        Args:
            nombre (str): Nombre del usuario
            email (str): Email del usuario
            tipo (str, opcional): Tipo de usuario ("normal" o "estudiante")
            carrera (str, opcional): Carrera del estudiante (solo para estudiantes)
            
        Returns:
            str: Mensaje de confirmación
        """
        if tipo.lower() == "estudiante" and carrera:
            usuario = Estudiante(nombre, email, carrera)
        else:
            usuario = Usuario(nombre, email)
        
        self.__usuarios[usuario.nombre] = usuario
        return f"Usuario {nombre} registrado exitosamente"
    
    def buscar_libro(self, isbn=None, titulo=None):
        """
        Busca un libro por ISBN o título.
        Ejemplo de sobrecarga por parámetros opcionales.
        
        Args:
            isbn (str, opcional): ISBN a buscar
            titulo (str, opcional): Título a buscar
            
        Returns:
            Libro o None: Objeto libro encontrado o None
        """
        if isbn and isbn in self.__libros:
            return self.__libros[isbn]
        
        if titulo:
            for libro in self.__libros.values():
                if titulo.lower() in libro.titulo.lower():
                    return libro
        
        return None
    
    def buscar_usuario(self, nombre):
        """
        Busca un usuario por nombre.
        
        Args:
            nombre (str): Nombre del usuario
            
        Returns:
            Usuario o None: Objeto usuario encontrado o None
        """
        return self.__usuarios.get(nombre)
    
    def prestar_libro(self, isbn, nombre_usuario):
        """
        Gestiona el préstamo de un libro a un usuario.
        
        Args:
            isbn (str): ISBN del libro
            nombre_usuario (str): Nombre del usuario
            
        Returns:
            str: Mensaje con el resultado de la operación
        """
        libro = self.buscar_libro(isbn=isbn)
        usuario = self.buscar_usuario(nombre_usuario)
        
        if not libro:
            return f"Libro no encontrado"
        if not usuario:
            return f"Usuario no encontrado"
        
        return usuario.prestar_libro(libro)
    
    def devolver_libro(self, isbn, nombre_usuario):
        """
        Gestiona la devolución de un libro.
        
        Args:
            isbn (str): ISBN del libro
            nombre_usuario (str): Nombre del usuario
            
        Returns:
            str: Mensaje con el resultado de la operación
        """
        libro = self.buscar_libro(isbn=isbn)
        usuario = self.buscar_usuario(nombre_usuario)
        
        if not libro:
            return f"Libro no encontrado"
        if not usuario:
            return f"Usuario no encontrado"
        
        return usuario.devolver_libro(libro)
    
    def listar_libros(self):
        """
        Lista todos los libros en la biblioteca.
        
        Returns:
            str: Lista de libros
        """
        if not self.__libros:
            return "No hay libros en la biblioteca"
        
        resultado = "Libros disponibles:\n"
        for libro in self.__libros.values():
            resultado += f"- {libro}\n"
        return resultado
    
    def listar_usuarios(self):
        """
        Lista todos los usuarios registrados.
        
        Returns:
            str: Lista de usuarios
        """
        if not self.__usuarios:
            return "No hay usuarios registrados"
        
        resultado = "Usuarios registrados:\n"
        for usuario in self.__usuarios.values():
            resultado += f"- {usuario.nombre} ({usuario.__class__.__name__})\n"
        return resultado