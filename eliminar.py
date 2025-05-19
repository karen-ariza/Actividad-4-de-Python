from manejo_csv import leer_contactos, escribir_contactos

def eliminar_contacto(nombre):
    contactos = leer_contactos()
    nuevos = [c for c in contactos if c['nombre'] != nombre]
    if len(nuevos) == len(contactos):
        return f"No se encontró el contacto '{nombre}'."
    escribir_contactos(nuevos)
    return f"Contacto '{nombre}' eliminado correctamente."
