#Gestión de productos en una tienda (electrónicos vs. alimentos).
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def descripcion(self):
        return f"{self.nombre} - ${self.precio}"

class Electronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        super().__init__(nombre, precio)
        self.garantia = garantia_meses

    def descripcion(self):
        return f"{super().descripcion()} | Garantía: {self.garantia} meses"

class Alimento(Producto):
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad

    def descripcion(self):
        return f"{super().descripcion()} | Caduca: {self.fecha_caducidad}"

# Interacción con el usuario
nombre = input("Nombre del producto: ")
precio = float(input("Precio: "))
tipo = input("¿Es electrónico o alimento? ").lower()

if tipo == "electrónico":
    garantia = int(input("Meses de garantía: "))
    producto = Electronico(nombre, precio, garantia)
elif tipo == "alimento":
    caducidad = input("Fecha de caducidad (dd/mm/aaaa): ")
    producto = Alimento(nombre, precio, caducidad)
else:
    print("Tipo inválido.")
    exit()

print("\nDescripción del producto:", producto.descripcion())