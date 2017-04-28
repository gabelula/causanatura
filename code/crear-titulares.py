
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import csv

def extract_from_csv(archivo):
    datos = []
    with open (archivo, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            datos.append(row)
    return datos

def clean_RNPA(rnpa):
    # remove - and " and trim
    crnpa = rnpa.strip().replace('-','').replace('"','')
    # if N/D then is empty
    if crnpa.lower() == 'n/d':
        return ''
    # check that they are digits
    if crnpa.isdigit():
        return crnpa
    return ''

def clean_name(name):
    # trim
    return name.strip().replace("'",'').lower()

def import_titular(titular):
    conn = psycopg2.connect("dbname=causa user=Gabriela")
    cur = conn.cursor()
    try:
        query = "INSERT INTO {0} (nombre, rnpa, rfc) VALUES (\"{1}\",\"{2}\",\"{3}\")".format('titulares', titular['nombre'], titular['rnpa'], titular['rfc'])
        print(cur.execute(query))
        conn.commit()
    except:
        conn.rollback()
        return False
    cur.close()
    conn.close()
    return True

def extract_and_import(archivo):
    datos = extract_from_csv(archivo)
    titulares = []
    for t in datos:
        if (t['RNPA'] == '' and t['TITULAR'] == ''):
            continue
        ct = {}
        ct['rnpa'] = clean_RNPA(t['RNPA'])
        ct['nombre'] = clean_name(t['TITULAR'])
        ct['rfc'] = ''
        if t.has_key('rfc'):
            ct['rfc'] = t['rfc']
        if import_titular(ct):
            titulares.append(ct)
    return titulares

def agregar_csv(titulares):
    archivo = 'titulares.csv'
    fieldnames = ['nombre', 'rnpa', 'rfc']
    with open (archivo, 'ab') as csvfile:
        sw = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
        sw.writeheader()
        for d in titulares:
            sw.write(d)

def main():
    ## Permisos
    archivos = [
    '2_ANEXO_2_2012_MAYORES.csv',
    '5_ANEXO_4_2012_MENORES.csv',
    'embarcaciones_mayores.csv',
    '3_ANEXO_2_2015_MAYORES.csv',
    'ANEXOORDENAMIENTO12316.csv',
    'embarcaciones_extranjeras.csv',
    'embarcaciones_menores.csv'
    ]

    # ir por todos los archivos y tomar titulares y rnpa
    for archivo in archivos:
        titulares = extract_and_import(archivo)
        agregar_csv(titulares)

if __name__ == "__main__":
    main()
