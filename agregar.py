from contacto import Contacto
from manejo_csv import leer_contactos, escribir_contactos

def agregar_contacto(nombre, correo, telefono):
    contactos = leer_contactos()
    if any(c['nombre'] == nombre for c in contactos):
        return f"El contacto '{nombre}' ya existe."
    nuevo = Contacto(nombre, correo, telefono)
    contactos.append(nuevo.to_dict())
    escribir_contactos(contactos)
    return f"Contacto '{nombre}' agregado correctamente."
