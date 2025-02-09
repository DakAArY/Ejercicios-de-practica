#Sistema de empleados
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre          # Atributo privado
        self.__salario = salario

    def mostrar_info(self):
        return f"{self.__nombre} - Salario: ${self.__salario}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Departamento: {self.departamento}"

# Interacción con el usuario
nombre = input("Nombre del empleado: ")
salario = float(input("Salario: "))
es_gerente = input("¿Es gerente? (s/n): ").lower()

if es_gerente == "s":
    departamento = input("Departamento: ")
    empleado = Gerente(nombre, salario, departamento)
else:
    empleado = Empleado(nombre, salario)

print("\nInformación del empleado:", empleado.mostrar_info())