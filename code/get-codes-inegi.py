#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os, csv

def main():
    archivo = '2014_2015_beneficiarios_diesel.csv'

    estado_archivo = 'estado_codigos_inegi.csv'
    estado_fieldnames = ['Estado', 'Codigo']
    municipio_archivo = 'municipio_codigos_inegi.csv'
    municipio_fieldnames = ['Municipio', 'Codigo']
    localidad_archivo = 'localidad_codigos_inegi.csv'
    localidad_fieldnames = ['Localidad', 'Codigo']

    with open (archivo, 'r') as f:
        reader = csv.DictReader(f)
        # with open(estado_archivo, 'wb') as csvfile:
        #     swe = csv.DictWriter(csvfile, fieldnames=estado_fieldnames)
        #     for row in reader:
        #         new_row = {}
        #         new_row['Estado'] = row['Estado']
        #         new_row['Codigo'] = row['Estado_INEGI']
        #         swe.writerow(new_row)

        # reader = csv.DictReader(f)
        # with open(municipio_archivo, 'wb') as csvfile:
        #     swm = csv.DictWriter(csvfile, fieldnames=municipio_fieldnames)
        #     for row in reader:
        #       new_row = {}
        #       new_row['Municipio'] = row['Municipio']
        #       new_row['Codigo'] = row['Muncipio_INEGI']
        #       swm.writerow(new_row)

        reader = csv.DictReader(f)
        with open(localidad_archivo, 'wb') as csvfile:
            swl = csv.DictWriter(csvfile, fieldnames=localidad_fieldnames)
            for row in reader:
              new_row = {}
              new_row['Localidad'] = row['Localidad']
              new_row['Codigo'] = row['Localidad_INEGI']
              swl.writerow(new_row)


if __name__ == "__main__":
    main()
