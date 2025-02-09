#Simulación de dispositivos inteligentes (luces vs. termostatos)
class DispositivoInteligente:
    def encender(self):
        pass

class Luz(DispositivoInteligente):
    def encender(self):
        return "💡 Luz encendida."

class Termostato(DispositivoInteligente):
    def encender(self):
        return "🌡️ Termostato ajustado a 22°C."

# Interacción con el usuario
dispositivos = {
    "1": Luz(),
    "2": Termostato()
}

print("Seleccione un dispositivo:")
print("1. Luz\n2. Termostato")
opcion = input("Opción: ")

dispositivo = dispositivos.get(opcion)
if dispositivo:
    print(dispositivo.encender())
else:
    print("Opción inválida.")