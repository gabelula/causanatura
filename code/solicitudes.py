#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import csv

def main():
  archivo = "14Solicitudes_Permisos.csv"
  warchivo = "Solicitudes_Permisos.csv"

  with open(warchivo, 'ab') as csvfile:
    fieldnames = ['Año','Estado','Permisos','Concesiones']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
    with open(archivo, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nrow = {}
            nrow['Estado'] = row['Estado']
            nrow['Año'] = '2009'
            nrow['Permisos'] = row['Solicitudes 2009 Permisos ']
            nrow['Concesiones'] = row['Solicitudes 2009 Concesiones']
            writer.writerow(nrow)
            nrow['Año'] = '2012'
            nrow['Permisos'] = row['Solicitudes 2012 ermisos']
            nrow['Concesiones'] = row['Solicitudes 2012Concesiones']
            writer.writerow(nrow)
            nrow['Año'] = '2015'
            nrow['Permisos'] = row['Solicitudes 2015Permisos']
            nrow['Concesiones'] = row['Solicitudes 2015Concesiones']
            writer.writerow(nrow)

if __name__ == "__main__":
    main()
