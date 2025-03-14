class Tarea:
    """
    Clase que representa una tarea en un sistema de tareas pendientes.
    
    Atributos:
        titulo (str): Título o descripción corta de la tarea
        prioridad (str): Prioridad de la tarea (alta, media, baja)
        completada (bool): Estado de la tarea (completada o pendiente)
        fecha_limite (str): Fecha límite para completar la tarea
    """
    
    # Constructor
    def __init__(self, titulo, prioridad="media", fecha_limite=None):
        """
        Constructor de la clase Tarea.
        
        Args:
            titulo (str): Título o descripción de la tarea
            prioridad (str, opcional): Prioridad de la tarea. Por defecto "media"
            fecha_limite (str, opcional): Fecha límite en formato "dd/mm/yyyy". Por defecto None
        """
        # El uso de self hace referencia al objeto actual
        self.titulo = titulo
        self.prioridad = prioridad.lower()
        self.completada = False
        self.fecha_limite = fecha_limite
        print(f"Tarea '{self.titulo}' creada")
    
    # Destructor
    def __del__(self):
        """Destructor de la clase Tarea."""
        print(f"Tarea '{self.titulo}' eliminada del sistema")
    
    # Método para mostrar información de la tarea
    def mostrar_info(self):
        """
        Muestra la información básica de la tarea.
        
        Returns:
            str: Información de la tarea
        """
        return f"'{self.titulo}' - Prioridad: {self.prioridad}"
    
    # Sobrecarga de método: mismo nombre pero diferentes parámetros
    def mostrar_info(self, detallado=False):
        """
        Muestra información de la tarea, con opción de mostrar detalles adicionales.
        
        Args:
            detallado (bool): Si es True, muestra información más detallada
            
        Returns:
            str: Información de la tarea, básica o detallada
        """
        estado = "Completada" if self.completada else "Pendiente"
        info = f"'{self.titulo}' - Prioridad: {self.prioridad} - Estado: {estado}"
        
        if detallado and self.fecha_limite:
            info += f" - Fecha límite: {self.fecha_limite}"
        
        return info
    
    # Método para marcar la tarea como completada
    def completar(self):
        """
        Marca la tarea como completada si estaba pendiente.
        
        Returns:
            bool: True si se pudo completar, False si ya estaba completada
        """
        if not self.completada:
            self.completada = True
            return True
        return False
    
    # Método para cambiar la prioridad de la tarea
    def cambiar_prioridad(self, nueva_prioridad):
        """
        Cambia la prioridad de la tarea.
        
        Args:
            nueva_prioridad (str): Nueva prioridad para la tarea
            
        Returns:
            bool: True si se cambió correctamente, False si la prioridad no es válida
        """
        if nueva_prioridad.lower() in ["alta", "media", "baja"]:
            self.prioridad = nueva_prioridad.lower()
            return True
        return False