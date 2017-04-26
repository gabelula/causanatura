#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import csv

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

def extract_from_csv(archivo):
    datos = []
    with open (archivo, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            datos.append(row)
            # {k: unicode(v, 'utf-8') for k, v in row.items()})
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
    return name.strip().replace("'",'')

def clean_beneficiarios(beneficiarios):
    clean_beneficiarios = []
    for b in beneficiarios:
        if (b['RNPA'] == '' and b['Beneficiario'] == ''):
            continue
        cb = {}
        cb['id'] = b['ID']
        cb['rnpa'] = clean_RNPA(b['RNPA'])
        cb['nombre'] = clean_name(b['Beneficiario']).lower()
        clean_beneficiarios.append(cb)

    return clean_beneficiarios

def agregar_beneficario(nombre, rnpa):
    conn = psycopg2.connect("dbname=causa user=Gabriela")
    cur = conn.cursor()
    query = """
        INSERT INTO {0} (nombre, rnpa) VALUES ({1},{2})
        """
    cur.execute(query, ('beneficiarios', nombre.lower(), rnpa))
    b =  cur.fetchone()
    print(b)
    return b['id']
    conn.commit()
    cur.close()
    conn.close()

def buscar_beneficiario(nombre, rnpa):
    conn = psycopg2.connect("dbname=causa user=Gabriela")
    cur = conn.cursor()

    query = """
        SELECT id FROM beneficiarios
        WHERE nombre = %s
        AND rnpa = %s;
        """
    try:
        cur.execute(query, (nombre.lower(), rnpa))
        b =  cur.fetchone()
        return b['id']
    except:
        # agregar el beneficiario
        id = agregar_beneficario(nombre, rnpa)
        print('No encontro beneficiario {0}, {1} pero se agrego.'.format(nombre, rnpa))
        return id

    cur.close()
    conn.close()

def buscar_localidad(estado, municipio, localidad):
    conn = psycopg2.connect("dbname=causa user=Gabriela")
    cur = conn.cursor()

    query = """
        SELECT id FROM localidades
        WHERE estado = %s
        AND municipio = %s
        AND localidad = %s;
        """
    try:
        cur.execute(query, (estado.lower(), municipio.lower(), localidad.lower()))
        b =  cur.fetchone()
        return b['id']
    except:
        # todo : agregar la localidad
        print('No encontro localidad {0}, {1}, {2}.'.format(estado, municpio, localidad))
        return 0

    cur.close()
    conn.close()

def clean_reconversion(subsidios, beneficiarios, localidades):
    clean_subsidios = []
    id = 0
    for s in subsidios:
        id = id + 1
        cs = {}
        # cs['id'] = id
        cs['año'] = s['Año']
        cs['id_beneficiario'] = buscar_beneficiario(s['Beneficiario'], s['RNPA'])
        cs['nombre_proyecto'] = clean_name(s['Nombre_proyecto']).lower()
        cs['tipo_proyecto'] = clean_name(s['Tipo_proyecto']).lower()
        cs['especie'] = clean_name(s['Especie']).lower()
        cs['monto'] = int(s['Monto'])
        cs['id_localidad'] = buscar_localidad(s['Estado'], s['Municipio'], s['Localidad'])
        clean_subsidios.append(cs)
    return clean_subsidios

def reverse(phrase):
    if ',' in phrase:
        return ' '.join([phrase.split(',')[1], phrase.split(',')[0]])
    return phrase

def clean_localidades(localidades):
    clean_localidades = []
    for l in localidades:
        cl = {}
        cl['id'] = l['Id']
        cl['estado'] = reverse(l['Estado']).replace('"', ' ').strip().lower()
        cl['municipio'] = reverse(l['Municipio']).replace('"', ' ').strip().lower()
        cl['localidad'] = reverse(l['Localidad']).replace('"', ' ').strip().lower()
        clean_localidades.append(cl)

    return clean_localidades

def import_data(data, table_name, create_query):
    conn = psycopg2.connect("dbname=causa user=Gabriela")
    cur = conn.cursor()

    try:
        cur.execute(create_query)
        conn.commit()
    except:
        print('Error on running query %s.', create_query)
        conn.rollback()

    for d in data:
        query = "INSERT INTO {0} ({1}) VALUES {2};".format(table_name, ','.join(d.keys()), tuple(d.values()))
        try:
            cur.execute(query)
            conn.commit()
        except Exception as inst:
            print('Failed when running {}.'.format(query))
            print(inst)
            conn.rollback()

    cur.close()
    conn.close()

def main():
    ########## BENEFICIARIOS ###########
    # extract & transform
    beneficiarios = clean_beneficiarios(extract_from_csv('beneficiarios.csv'))

    # import
    query = """CREATE TABLE beneficiarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        rnpa VARCHAR(15)
    );
    CREATE UNIQUE INDEX beneficiario_rnpa ON beneficiarios (nombre, rnpa);
    """
    import_data(beneficiarios, 'beneficiarios', query)

    ########## LOCALIDADES ###########
    # extract & transform
    localidades = clean_localidades(extract_from_csv('lugares.csv'))

    # import
    query = """CREATE TABLE localidades (
        id SERIAL PRIMARY KEY,
        estado    VARCHAR(255) NOT NULL,
        municipio VARCHAR(255) NOT NULL,
        localidad VARCHAR(255) NOT NULL
    );
    CREATE INDEX estado ON localidades (estado);
    CREATE INDEX estado_municpio ON localidades (estado, municipio);
    CREATE UNIQUE INDEX estado_municpio_localidad ON localidades (estado, municipio, localidad);
    """
    import_data(localidades, 'localidades', query)

    ########## RECONVERSION - Listado de beneficiarios del SUBSIDIO para PROYECTOS DE RECONVERSIÓN PRODUCTIVA 2008-2011, años 2008, 2009,2010, 2011 ###########
    # extract & transform
    reconversion = clean_reconversion(extract_from_csv('2008_2011_reconversion.csv'), beneficiarios, localidades)

    # import
    query = """CREATE TABLE subsidios_reconversion (
        id SERIAL PRIMARY KEY,
        año VARCHAR(4),
        id_beneficiario INT,
        id_localidad INT,
        nombre_proyecto VARCHAR(255),
        tipo_proyecto VARCHAR(255),
        especie VARCHAR(255),
        monto INT
    );
    CREATE INDEX beneficiario ON subsidios_reconversion (id_beneficiario);
    CREATE INDEX localidad ON subsidios_reconversion (id_localidad);
    """
    import_data(reconversion, 'subsidios_reconversion', query)


if __name__ == "__main__":
    main()
