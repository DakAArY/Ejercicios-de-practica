# Importamos las clases necesarias
from contenido import ContenidoMultimedia, Pelicula, Serie

# Clase que gestiona la plataforma de streaming
class PlataformaStreaming:
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []  # Lista para almacenar contenido
        self.usuarios = []  # Lista para usuarios registrados
    
    # Método para añadir contenido
    def agregar_contenido(self, contenido):
        # Verifica que sea contenido multimedia válido
        if isinstance(contenido, ContenidoMultimedia):
            self.catalogo.append(contenido)
            return f"{contenido.titulo} añadido al catálogo de {self.nombre}"
        else:
            return "Error: Tipo de contenido no válido"
    
    # Método para buscar contenido
    def buscar(self, termino):
        resultados = []
        for item in self.catalogo:
            # Busca en el título o género
            if termino.lower() in item.titulo.lower() or termino.lower() in item.genero.lower():
                resultados.append(item)
        return resultados
    
    # Método para listar por tipo
    def listar_por_tipo(self):
        peliculas = []
        series = []
        
        # Clasifica el contenido por tipo
        for item in self.catalogo:
            if isinstance(item, Pelicula):
                peliculas.append(item)
            elif isinstance(item, Serie):
                series.append(item)
        
        return {
            "peliculas": peliculas,
            "series": series
        }
    
    # Método para recomendar contenido
    def recomendar(self):
        # Recomienda el contenido mejor calificado
        if not self.catalogo:
            return "No hay contenido disponible"
            
        mejor_contenido = max(self.catalogo, key=lambda x: x.calificacion)
        return mejor_contenido