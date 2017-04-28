#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import csv


def isNone(cell):
  Nones = ['x', '-', 'no tiene', 'no', 'NO TIENE', 'NO', 'NO TIENE CLAVE']
  for n in Nones:
    if cell.strip() == n:
      return True
  return False

def convertir(archivo):
  nuevo_archivo = 'clean_' + archivo
  fieldnames = ['Componente', 'Año',	'Estado',	'Municipio',	'Localidad', 'Registradas', 'Apoyadas']
  with open (archivo, 'r') as f:
      reader = csv.DictReader(f)
      with open(nuevo_archivo, 'wb') as csvfile:
        sw = csv.DictWriter(csvfile, fieldnames=fieldnames)
        sw.writeheader()
        for row in reader:
          new_row = {}
          new_row['Año'] = row['Año']
          new_row['Estado'] = row['Estado']
          new_row['Municipio'] = row['Municipio']
          new_row['Localidad'] = row['Localidad']
          new_row['Componente'] = 'Motor'
          new_row['Registradas'] = row['Motor_Registradas']
          new_row['Apoyadas'] = row['Motor_Apoyadas']
          sw.writerow(new_row)
          new_row['Componente'] = 'Embarcación'
          new_row['Registradas'] = row['Embarcacion_Registradas']
          new_row['Apoyadas'] = row['Embarcacion_Apoyadas']
          sw.writerow(new_row)
          new_row['Componente'] = 'Hielera'
          new_row['Registradas'] = row['Hielera_Registradas']
          new_row['Apoyadas'] = row['Hielera_Apoyadas']
          sw.writerow(new_row)
          new_row['Componente'] = 'Sistema'
          new_row['Registradas'] = row['Sistemas_Registradas']
          new_row['Apoyadas'] = row['Sistemas_Apoyadas']
          sw.writerow(new_row)

def main():
    archivo = 'solicitudes_embarcaciones_menores.csv'
    convertir(archivo)

if __name__ == '__main__':
    main()
