#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os, csv

archivos =  {
  "2008_2009_reconversion.csv",
  "2008_2009_reconversion.csv",
  "2011_reconversion.csv",
  "2008_2013_motores.csv",
  "2011_2012_pesca.csv",
  "2011_2013_gasolina.csv",
  "2011_2013_motores_componentes.csv",
  "sustitucion_motores.csv",
  "2011_electricos.csv",
  "2011_2013_diesel.csv",
  "2012_integral.csv",
  "2012_motores_marinos_ecologicos.csv"
  }

def crear_beneficiario(archivos):
 columnas_a_unir = [ "PRIMER APELLIDO", "SEGUNDO APELLIDO", "NOMBRE" ]
 nueva_columna = "Beneficiario"
 for archivo in archivos:
   with open (archivo, 'r') as f:
       nuevo_archivo = 'clean_' + archivo
       reader = csv.DictReader(f)
       fieldnames=reader.fieldnames
       for x in columnas_a_unir:
         print(x)
         fieldnames.remove(x)
       fieldnames.append(nueva_columna)
       with open(nuevo_archivo, 'wb') as csvfile:
         sw = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
         sw.writeheader()
         for row in reader:
           row[nueva_columna] = ' '.join(map(lambda x:row[x].strip(), columnas_a_unir))
           for i in columnas_a_unir:
             row.pop(i, None)
           sw.writerow(row)

def isNone(cell):
  Nones = ['x', '-', 'no tiene', 'no', 'NO TIENE', 'NO', 'NO TIENE CLAVE']
  for n in Nones:
    if cell.strip() == n:
      return True
  return False

def normalizar(archivo):
  nuevo_archivo = 'clean_' + archivo
  with open (archivo, 'r') as f:
      reader = csv.DictReader(f)
      with open(nuevo_archivo, 'wb') as csvfile:
        sw = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        sw.writeheader()
        for row in reader:
          for column in row:
            if isNone(row[column]):
              row[column] = ''
          sw.writerow(row)

def remove_dirt(archivo):
    nuevo_archivo = 'clean_' + archivo
    with open (archivo, 'r') as f:
        reader = csv.DictReader(f)
        with open(nuevo_archivo, 'wb') as csvfile:
          sw = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
          sw.writeheader()
          for row in reader:
              # clean rnpa row
              fields = row["RNPA"].split (" ")
              print(fields)
              if len(fields) > 1:
                  row["RNPA"] = fields[0]
                  row["Estado"] = fields[1]
              sw.writerow(row)

def check_type(archivo):
  with open (archivo, 'r') as f:
      reader = csv.DictReader(f)
      for row in reader:
        for column in row:
          print(type(row[column]))

def transpose(archivo):
    nuevo_archivo = 'clean_' + archivo
    nuevo_fieldnames = ["Año", "Entidad",	"Permisos", "Concesiones"]

    with open (archivo, 'r') as f:
        reader = csv.DictReader(f)
        with open(nuevo_archivo, 'wb') as csvfile:
          sw = csv.DictWriter(csvfile, fieldnames=nuevo_fieldnames)
          sw.writeheader()
          for row in reader:
              row2 = {}
              row2["Entidad"] = row["Entidad"]
              for a in [2009,2012,2015]:
                  row2["Año"] = a
                  row2["Permisos"] = row["Solicitudes {} Permisos".format(a)]
                  row2["Concesiones"] = row["Solicitudes {} Concesiones".format(a)]
                  sw.writerow(row2)

def main():

  # Crea un archivo clean_XXX uniendo columnas de nombres en una sola 'beneficiario'
  #crear_beneficiario(["2011_2013_gasolina.csv", "2011_2013_diesel.csv"])

  # Crea un nuevo archivo clean_XXX con los valores nulos en ''
  # for archivo in archivos:
  #   normalizar(archivo)

  # for archivo in archivos:
  #   check_type(archivo)

  # archivo = "2014_2015_beneficiarios_embarcaciones_menores.csv"
  # remove_dirt(archivo)

  archivo = "1_ANEXO_1.csv"
  transpose(archivo)

if __name__ == "__main__":
    main()
