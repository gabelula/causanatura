# Por hacer

- get json METADATA file template
- convert everything to CSV <--
	- XLS (31)
	- XLSX (29)
	- CSV (4)
	- PDF (13)
- use metadata to get all the data organize
- import to CSV
- crear modelo de datos

# Tools being used

## Convert PDF to XLS/CSV

- Tabula <-- it did not work for OCR
- Cometdocs <-- it did not work for OCR
- Acrobat Pro <-- it works for OCR but it is paid
- PDFTables <-- it did not work for OCR & LIMIT ON USAGE when free
- PDFSandwich <-- OCR
- https://github.com/pdfliberation
- https://github.com/jsfenfen/parsing-prickly-pdfs
- Tesseract for images
  - tesseract img.tiff out.csv
- FineReader (paid)
- CSVKit: awesome kit on CSV manipulation
- xlsx2csv : it converts XLS to CSV by sheet

# Chequeo archivos

- Running code/pdftoxls.py for ./datos when pdftables API.

## 2011-2013

- Permiso de Pesca
  - convertido a csv
- Inspeccion y vigilancia pesquera
  - metadata
  - Opciones:
    1. convertido a xls (con acrobat DC)
    2. convertido a csv con pdftables
    3. convertido a .tiff con acrobat DC y a txt con tesseract
- Subsidios
  - metadata
  - convertirlo a CSV (in2csv & cleaning)
  - chequear metadata está bien en cuanto a campos que contiene

## 2014-2015

- Apoyos y Subsidios
  - Infraestructura
    - Needs to work on Beneficiarios
  - Planeacion
  - Fomento
- Inspeccion y vigilancia
- Permisos y Concesiones
- Produccion

## Otras - Conapesca
## Solicitudes


# Con Causa

- Recorrer todos los datos
- Mostrar herramientas usadas
