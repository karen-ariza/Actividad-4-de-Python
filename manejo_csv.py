import csv

CSV_FILE = 'contactos.csv'

def leer_contactos():
    contactos = []
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            contactos = list(reader)
    except FileNotFoundError:
        pass
    return contactos

def escribir_contactos(contactos):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['nombre', 'correo', 'telefono']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contactos)
