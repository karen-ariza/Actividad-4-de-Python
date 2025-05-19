class Contacto:
    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "correo": self.correo,
            "telefono": self.telefono
        }
