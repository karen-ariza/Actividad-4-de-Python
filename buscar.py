from manejo_csv import leer_contactos

def buscar_contacto(nombre):
    contactos = leer_contactos()
    for c in contactos:
        if c['nombre'] == nombre:
            return c
    return None
