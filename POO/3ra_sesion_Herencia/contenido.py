# Clase base que representa contenido multimedia genérico
class ContenidoMultimedia:
    # Constructor con atributos comunes
    def __init__(self, titulo, genero, año, calificacion=0):
        self.titulo = titulo
        self.genero = genero
        self.año = año
        self.calificacion = calificacion
        self.reproducciones = 0
    
    # Método para reproducir contenido
    def reproducir(self):
        self.reproducciones += 1
        return f"Reproduciendo {self.titulo}"
    
    # Método para calificar contenido
    def calificar(self, puntuacion):
        if 0 <= puntuacion <= 5:
            self.calificacion = puntuacion
            return f"{self.titulo} calificado con {puntuacion} estrellas"
        return "Calificación debe estar entre 0 y 5"
    
    # Método para mostrar información
    def mostrar_info(self):
        return f"{self.titulo} ({self.año}) - Género: {self.genero}"


# Clase derivada para películas
class Pelicula(ContenidoMultimedia):
    # Constructor con atributos específicos y heredados
    def __init__(self, titulo, genero, año, director, duracion, calificacion=0):
        # Llamamos al constructor de la clase padre
        super().__init__(titulo, genero, año, calificacion)
        # Atributos propios
        self.director = director
        self.duracion = duracion  # en minutos
    
    # Sobrescribe el método mostrar_info
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica} - Director: {self.director} - {self.duracion} min"
    
    # Método específico de esta clase
    def tiempo_restante(self, minutos_vistos):
        restante = max(0, self.duracion - minutos_vistos)
        return f"Tiempo restante: {restante} minutos"


# Otra clase derivada para series
class Serie(ContenidoMultimedia):
    # Constructor con atributos específicos
    def __init__(self, titulo, genero, año, creador, temporadas, episodios, calificacion=0):
        super().__init__(titulo, genero, año, calificacion)
        self.creador = creador
        self.temporadas = temporadas
        self.episodios = episodios
    
    # Sobrescribe el método mostrar_info
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica} - {self.temporadas} temporadas, {self.episodios} episodios"
    
    # Método específico para esta clase
    def agregar_temporada(self, episodios_nuevos):
        self.temporadas += 1
        self.episodios += episodios_nuevos
        return f"Nueva temporada añadida a {self.titulo}"