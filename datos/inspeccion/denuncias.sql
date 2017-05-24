CREATE TABLE denuncias (
	Ano DECIMAL NOT NULL, 
	Folio DECIMAL, 
	Fecha VARCHAR(10), 
	Estado VARCHAR(19) NOT NULL, 
	Municipio VARCHAR(36), 
	Localidad VARCHAR(43), 
	Lugar VARCHAR(50) NOT NULL, 
	Tipo VARCHAR(23), 
	Instrumento VARCHAR(17), 
	Estatus VARCHAR(11) NOT NULL, 
	Especie VARCHAR(12)
);
