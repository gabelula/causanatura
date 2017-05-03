#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import csv

def main():
  archivo = "pesca-ilegal-2013.csv"
  warchivo = "clean-pesca-ilegal.csv"

  with open(warchivo, 'ab') as csvfile:
    fieldnames = ['Año', 'Estado', 'Especie', 'Cantidad']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
    with open(archivo, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
          nrow = {}
          nrow['Año'] = row['Año']
          nrow['Estado'] = row['ESTADO']
          for k in row.keys():
            nrow['Especie'] = k
            nrow['Cantidad'] = row[k]
            writer.writerow(nrow)

if __name__ == "__main__":
    main()

# pesca-ilegal.csv
# Año	ESTADO	ABULON	AGUA MALA- BOLA DE CANON	ALMEJA	ATUN	CALAMAR	CAMARON	CARACOL	DORADO	ESCAMA GENERAL	JAIBA	LANGOSTA	LISA-LISETA	MERO	OSTIÓN	PEPINO	PICUDOS	PULPO	ROBALO	TIBURON Y RAYAS	OTROS

# pesca-ilegal-2013.csv
# Año	ESTADO	ABULON	AGUA MALA- BOLA DE CANON	ALMEJA	ALMEJA CATARINA	ALMEJA CHOCOLATA	ALMEJA GENEROSA	BAGRE	CALAMAR	CALLO DE HACHA	CAMARON	CARACOL	CARPA	CHARAL	CURVINA GOLFINA	DORADO	ERIZO	ESCAMA GENERAL	JAIBA	JUREL		LANGOSTA	LANGOSTINO	LISA-LISETA	LOBINA	MARLIN	MERO	OSTION	PELACICOS MENORES	PEPINO DE MAR	PEZ ESPADA	PEZ VELA	PULPO	ROBALO	SABALO	SIERRA	TIBURON Y RAYAS	TILAPIA	TRUCHA DE AGUADULCE	TUNIDOS	OTROS
