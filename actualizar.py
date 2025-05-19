from manejo_csv import leer_contactos, escribir_contactos

def actualizar_contacto(nombre, nuevo_correo, nuevo_telefono):
    contactos = leer_contactos()
    for c in contactos:
        if c['nombre'] == nombre:
            c['correo'] = nuevo_correo
            c['telefono'] = nuevo_telefono
            escribir_contactos(contactos)
            return f"Contacto '{nombre}' actualizado correctamente."
    return f"No se encontró el contacto '{nombre}'."
