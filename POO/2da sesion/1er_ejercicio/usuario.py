"""
Modulo que contiene las clases relacionadas con usuarios del sistema.
"""

class Usuario:
    """
    Clase base que representa un usuario del sitema de biblioteca.
    
    Atributos:
        __id (int): Identificador unico del usuario (privado)
        __nombre (str): Nombre del usuario (privado)
        __email (str): Email del usuario (privado)
        libros_prestados (list): Lista de libros prestados al usuario (publico)
    """
    
    #Variable de clase (compartida por todas las instancias )
    contador_usuarios = 0
    
    def __init__(self, nombre, email):
        """
        Constructor de la clase Usuario.
        
        Args:
            nombre (str): Nombre del usuario
            email (str): Email del usuario
        """
        #Incrementa el contador de usuarios (variable de clase)
        Usuario.contador_usuarios += 1
        self.__id = Usuario.contador_usuarios
        self.__nombre = nombre
        self.__email = email
        self.libros_prestados = []
    
    def prestar_libro(self, libro):
        """
        Registra un prestamo del libro al usuario
        
        Args:
            libro : Objeto de la clase Libro
        
        Returns:
            str: Mensaje indicando el resultado de la operacion
        """
        resultado = libro.prestar()
        if "exitosamente" in resultado:
            self.libros_prestados.append(libro)
        return resultado
    
    def devolver_libro(self, libro):
        """
        Registra la devolucion de un libro
        
        Args:
            libro: Objeto de la clase Libro
        
        Returns:
            str: Mensaje indicando el resultado de la operacion
        """
        if libro in self.libros_prestados:
            resultado = libro.devolver()
            self.libros_prestados.remove(libro)
            return resultado
        else:
            return f"El usuario no tiene este libro"
    
    def listar_prestamos(self):
        """
        Lista los libros prestados al usuario.
        
        Returns:
            str: Lista de libros prestados o mensaje si no hay prestamos 
        """
        if not self.libros_prestados:
            return "No tiene libros prestados"
        
        resultado = f"Libros prestados a {self.__nombre}:\n"
        for libro in self.libros_prestados:
            resultado += f"- {libro.titulo} por {libro.autor}\n"
        return resultado
    
    @property
    def nombre(self):
        """Getter para el nombre del usuario"""
        return self.__nombre
    
    @property
    def email(self):
        """Getter para el email del usuario"""
        return self.__email
    

class Estudiante(Usuario):
    """
    Clase derivada de Usuario que representa a un estudiante.
    Hereda todos los atributos y metodos de Usuario.
    
    Atributos adicionales:
        __carrera (str): Carrera del estudiante (privada)
        __limite_prestamos (int): Limite de prestamos permitidos (privada)
    """
    
    def __init__(self, nombre, email, carrera):
        """
        Constructor de la clase Estudiante.
        
        Args:
            nombre (str): Nombre del estudiante
            email (str): Email del estudiante
        """
        # Llama al constructor de la clase padre
        super().__init__(nombre, email)
        self.__carrera = carrera
        self.__limite_prestamos = 3
    
    def prestar_libro(self, libro):
        """
        Sobrescribe el metodo de la clase padre para añadir limites de prestamo.
        
        Args:
            libro: Objeto de la clase libro
        
        Returns:
            str: Mensaje indicando el resultado de la operacion
        """
        if len(self.libros_prestados) >= self.__limite_prestamos:
            return f"No puede pedir mas libros. Limite: {self.__limite_prestamos}"
        return super().prestar_libro(libro)
    
    def __str__(self):
        """
        Representacion en string del estudiante.
        
        Returns:
            str: Informacion del estudiante
        """
        return f"Estudiante: {self.nombre} | Carrera: {self.__carrera}"