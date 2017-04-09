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

## Convertir PDF a XLS/CSV

- Tabula
- Cometdocs
- Acrobat Pro
- PDFTables
- Tesseract for images
- FineReader (paid)
- CSVKit: awesome kit on CSV manipulation
- xlsx2csv : it converts XLS to CSV by sheet
- open refine
- Open Office

Leer [Herramientas|herramientas.md]

# Chequeo archivos

- Running code/pdftoxls.py for ./datos when pdftables API.

# Tareas y Herramientas/Procesos usados

## Conversión a CSV

Aqui incluimos algunos pasos de normalización y limpieza de datos como unificar archivos por año y normalizar nombres de columnas.

En principio use un script para convertir todos los XLS a CSV mediante PDFTables. Eso funciono para algunos pero no para todos.

### 2011-2013

- Permiso de Pesca
  - convertido a csv mediante script.
- Inspeccion y vigilancia pesquera
  - Dividi el PDF en un PDF por hoja y pase FineReader a las tablas.
- Subsidios
  - convertido a CSV (in2csv & cleaning)

### 2014-2015

- Apoyos y Subsidios
  - Infraestructura
    - Needs to work on Beneficiarios
  - Planeacion
  - Fomento
- Inspeccion y vigilancia
- Permisos y Concesiones
- Produccion

### Otras - Conapesca
### Solicitudes

## Limpieza

Pasar todos los archivos por herramientas de limpieza:

- csvclean del CSVKit
- Open Refine

## CSV a SQL

Para cada archivo CSV generar archivos sql para generación de tablas.

- csvsql del CSVKit


# Talleres

- Lectura y Verificación de datos
- Herramientas usadas y útiles para limpieza de datos futuros
