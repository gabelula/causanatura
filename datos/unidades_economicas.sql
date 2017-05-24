CREATE TABLE unidades_economicas (
	Tipo VARCHAR(20) NOT NULL, 
	RNPA DECIMAL NOT NULL, 
	Unidad_Economica VARCHAR(116) NOT NULL, 
	Fecha_Registro VARCHAR(8) NOT NULL, 
	Tipo_Persona VARCHAR(6) NOT NULL, 
	Representante_Legal VARCHAR(77), 
	Estado VARCHAR(19) NOT NULL, 
	Municipio VARCHAR(49) NOT NULL, 
	Localidad VARCHAR(60) NOT NULL, 
	Inicio_Operaciones VARCHAR(13) NOT NULL
);
