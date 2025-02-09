# Sistema de notificaciones (email vs. SMS).
class Notificacion:
    def __init__(self, mensaje):
        self.__mensaje = mensaje        # Encapsulamiento

    def enviar(self):                   # Abstracción (método a implementar)
        pass

class Email(Notificacion):
    def __init__(self, mensaje, destinatario):
        super().__init__(mensaje)
        self.destinatario = destinatario

    def enviar(self):                   # Polimorfismo
        return f"✉️ Email enviado a {self.destinatario}: '{self._Notificacion__mensaje}'"

class SMS(Notificacion):
    def __init__(self, mensaje, telefono):
        super().__init__(mensaje)
        self.telefono = telefono

    def enviar(self):                   # Polimorfismo
        return f"📱 SMS enviado al {self.telefono}: '{self._Notificacion__mensaje}'"

# Interacción con el usuario
mensaje = input("Ingrese el mensaje a enviar: ")
tipo = input("¿Enviar por Email o SMS? ").lower()

if tipo == "email":
    destinatario = input("Correo electrónico: ")
    notificacion = Email(mensaje, destinatario)
elif tipo == "sms":
    telefono = input("Número de teléfono: ")
    notificacion = SMS(mensaje, telefono)
else:
    print("Tipo inválido.")
    exit()

print(notificacion.enviar())