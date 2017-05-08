#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datapackage, csv, os, json

dp = datapackage.DataPackage()
dp.descriptor['name'] = 'apoyos'
dp.descriptor['resources'] = []

archivos = [
    '2014_2015_solicitudes_diesel.csv',
    '2014_2015_solicitudes_gasolina.csv',
    '2014_beneficiarios_modernizacion_embarcaciones_mayores.csv',
    '2015_beneficiarios_modernizacion_embarcaciones_mayores.csv',
    'beneficiarios_embarcaciones_menores.csv',
    'diesel.csv',
    'electricos.csv',
    'gasolina.csv',
    'integral.csv',
    'motores.csv',
    'pesca.csv',
    'reconversion.csv',
    'solicitudes_embarcaciones_menores.csv',
    'solicitudes_embaraciones_mayores.csv',
    'sustitucion_motores.csv'
]

for i in range(len(archivos)):
    archivo = archivos[i]
    dp.descriptor['resources'].append({'name': os.path.splitext(archivo)[0]})
    resource  = dp.resources[i]
    resource.descriptor['data'] = [
        archivo
    ]
    fields = []
    with open (archivo, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for f in fieldnames:
            field = {}
            field['id'] = f
            field['name'] = f
            field['label'] = f
            field['type'] = 'string'
            field['description'] = f
            if (f == 'año' or f == 'Año'):
                field['format'] = 'YYYY'
                field['type'] = 'date'
            fields.append(field)

    resource.descriptor['format'] = 'CSV'
    resource.descriptor['mediatype'] = 'text/csv'
    resource.descriptor['schema'] = { 'fields': fields }

with open('datapackage.json', 'w') as f:
  f.write(json.dumps(dp.to_json(), sort_keys=True, indent=4))
