# Sistema de reserva de hotel.
class Habitacion:
    def __init__(self, numero, capacidad):
        self.__numero = numero          # Atributo privado (encapsulamiento)
        self.__capacidad = capacidad
        self.__disponible = True        # Estado encapsulado

    def reservar(self):
        if self.__disponible:
            self.__disponible = False
            return f"Habitación {self.__numero} reservada."
        else:
            return "Habitación no disponible."

    def liberar(self):
        self.__disponible = True
        return f"Habitación {self.__numero} liberada."

    def estado(self):
        return "Disponible" if self.__disponible else "Ocupada"

# Interacción con el usuario
habitacion_101 = Habitacion(101, 2)
print("Bienvenido al sistema de reservas.")

while True:
    print("\n1. Reservar habitación\n2. Liberar habitación\n3. Ver estado\n4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(habitacion_101.reservar())
    elif opcion == "2":
        print(habitacion_101.liberar())
    elif opcion == "3":
        print(f"Estado: {habitacion_101.estado()}")
    elif opcion == "4":
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opción inválida.")