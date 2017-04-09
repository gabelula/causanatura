# Documentación

## Tareas

- crear json METADATA file template. Normaliza datos.
- convertir todo a CSV y luego SQL
	- XLS (31)
	- XLSX (29)
	- CSV (4)
	- PDF (13)
- usar metadatos para organizar los datos
- crear modelo de datos

# Herramientas a usar

## Convert PDF to XLS/CSV

- Tabula <-- it did not work for OCR
- Cometdocs <-- it did not work for OCR
- Acrobat Pro <-- it works for OCR but it is paid
- PDFTables <-- it did not work for OCR & LIMIT ON USAGE when free
- Tesseract for images
  - tesseract img.tiff out.csv
- FineReader (paid)
- CSVKit: awesome kit on CSV manipulation
- xlsx2csv : it converts XLS to CSV by sheet
- open refine

Leer [Herramientas|herramientas.md]

# Chequeo archivos

- Running code/pdftoxls.py for ./datos when pdftables API.

# Tareas y Herramientas/Procesos usados

## 2011-2013

### Conversión a CSV

Aqui incluimos algunos pasos de normalización y limpieza de datos como unificar archivos por año y normalizar nombres de columnas.

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


### Limpieza

Pasar todos los archivos por herramientas de limpieza:

- csvclean del CSVKit
- Open Refine

### CSV a SQL

Para cada archivo CSV generar archivos sql para generación de tablas.

- csvsql del CSVKit

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


# Talleres

- Lectura y Verificación de datos
- Herramientas usadas y útiles para limpieza de datos futuros
