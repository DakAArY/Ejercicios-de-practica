class Usuario:
    """
    Clase que representa un usuario del sistema de gestión de tareas.
    
    Atributos:
        nombre (str): Nombre del usuario
        tareas (list): Lista de tareas del usuario
    """
    
    # Constructor
    def __init__(self, nombre, email=None):
        """
        Constructor de la clase Usuario.
        
        Args:
            nombre (str): Nombre del usuario
            email (str, opcional): Email del usuario. Por defecto None
        """
        self.nombre = nombre
        self.email = email
        self.tareas = []  # Lista vacía para almacenar las tareas
        self.tareas_completadas = 0
        print(f"Usuario '{self.nombre}' creado")
    
    # Destructor
    def __del__(self):
        """Destructor de la clase Usuario."""
        print(f"Usuario '{self.nombre}' eliminado del sistema")
    
    # Método para agregar una tarea
    def agregar_tarea(self, tarea):
        """
        Agrega una tarea a la lista del usuario.
        
        Args:
            tarea: Objeto de la clase Tarea a agregar
        """
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.titulo}' agregada a {self.nombre}")
    
    # Sobrecarga del método agregar_tarea: permite agregar múltiples tareas
    def agregar_tarea(self, *tareas):
        """
        Agrega una o varias tareas a la lista del usuario.
        
        Args:
            *tareas: Uno o más objetos de la clase Tarea
        """
        for tarea in tareas:
            self.tareas.append(tarea)
            print(f"Tarea '{tarea.titulo}' agregada a {self.nombre}")
    
    # Método para buscar una tarea por título
    def buscar_tarea(self, titulo):
        """
        Busca una tarea por su título.
        
        Args:
            titulo (str): Título de la tarea a buscar
            
        Returns:
            Tarea o None: La tarea encontrada o None si no existe
        """
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                return tarea
        return None
    
    # Método para listar todas las tareas
    def listar_tareas(self, solo_pendientes=False):
        """
        Lista todas las tareas del usuario.
        
        Args:
            solo_pendientes (bool): Si es True, solo muestra tareas pendientes
        """
        if not self.tareas:
            print(f"{self.nombre} no tiene tareas")
            return
        
        filtro = "pendientes" if solo_pendientes else "todas"
        print(f"Tareas {filtro} de {self.nombre}:")
        
        contador = 0
        for i, tarea in enumerate(self.tareas, 1):
            if not solo_pendientes or not tarea.completada:
                print(f"{i}. {tarea.mostrar_info()}")
                contador += 1
        
        if contador == 0:
            print("No hay tareas que mostrar")
    
    # Método para completar una tarea
    def completar_tarea(self, titulo):
        """
        Marca una tarea como completada.
        
        Args:
            titulo (str): Título de la tarea a completar
            
        Returns:
            bool: True si se pudo completar, False en caso contrario
        """
        tarea = self.buscar_tarea(titulo)
        if tarea and tarea.completar():
            self.tareas_completadas += 1
            print(f"Tarea '{tarea.titulo}' marcada como completada")
            return True
        elif tarea:
            print(f"La tarea '{titulo}' ya estaba completada")
        else:
            print(f"No se encontró la tarea '{titulo}'")
        return False
    
    # Método para contar tareas pendientes
    def contar_pendientes(self):
        """
        Cuenta cuántas tareas pendientes tiene el usuario.
        
        Returns:
            int: Número de tareas pendientes
        """
        pendientes = 0
        for tarea in self.tareas:
            if not tarea.completada:
                pendientes += 1
        return pendientes
    
    # Método para obtener estadísticas de tareas
    def obtener_estadisticas(self):
        """
        Calcula estadísticas sobre las tareas del usuario.
        
        Returns:
            dict: Diccionario con estadísticas de tareas
        """
        total = len(self.tareas)
        pendientes = self.contar_pendientes()
        completadas = total - pendientes
        
        # Conteo por prioridades
        alta = sum(1 for t in self.tareas if t.prioridad == "alta")
        media = sum(1 for t in self.tareas if t.prioridad == "media")
        baja = sum(1 for t in self.tareas if t.prioridad == "baja")
        
        return {
            "total": total,
            "pendientes": pendientes,
            "completadas": completadas,
            "porcentaje_completado": (completadas / total * 100) if total > 0 else 0,
            "por_prioridad": {
                "alta": alta,
                "media": media,
                "baja": baja
            }
        }