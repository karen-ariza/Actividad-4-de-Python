# utils/gestor_csv.py
import csv
from contacto import Contacto

ARCHIVO_CSV = 'data/contactos.csv'  # Ruta al archivo CSV

def leer_contactos():
    contactos = []
    try:
        with open(ARCHIVO_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                contacto = Contacto(fila['nombre'], fila['correo'], fila['telefono'])
                contactos.append(contacto)
    except FileNotFoundError:
        # Si no existe el archivo, devolvemos lista vacía
        pass
    return contactos

def escribir_contactos(contactos):
    with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
        campos = ['nombre', 'correo', 'telefono']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for contacto in contactos:
            writer.writerow({
                'nombre': contacto.nombre,
                'correo': contacto.correo,
                'telefono': contacto.telefono
            })
