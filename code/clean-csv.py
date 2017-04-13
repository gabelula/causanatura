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
       with open(nuevo_archivo, 'wb') as csvfile:
         fieldnames=reader.fieldnames
         fieldnames.append(nueva_columna)
         sw = csv.DictWriter(csvfile, fieldnames=fieldnames)
         sw.writeheader()
         for row in reader:
           row[nueva_columna] = ' '.join(map(lambda x:row[x].strip(), columnas_a_unir))
           for i in columnas_a_unir:
             row.pop(i, None)
           sw.writerow(row)

def isNone(cell):
  Nones = ['x', '-', 'no tiene', 'no']
  for n in Nones:
    if cell == n:
      return True
  return False

def normalizar_nones(archivo):
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

def main():

  # Crea un archivo clean_XXX uniendo columnas de nombres en una sola 'beneficiario'
  crear_beneficiario(["2011_2013_gasolina.csv", "2011_2013_diesel.csv"])

  # Crea un nuevo archivo clean_XXX con los valores nulos en ''
  # for archivo in archivos:
  #   normalizar_nones(archivo)

    # # Search all the folders in datos
    # for csv in getCSVFiles('../datos'):
    #     new_name = os.path.basename(csv).split('.')[0]
    #     print "CSV {0} converted into {1}".format(csv, new_name)
    #     insert_sql(new_name, csv)

if __name__ == "__main__":
    main()
