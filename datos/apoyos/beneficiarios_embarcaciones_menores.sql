CREATE TABLE beneficiarios_embarcaciones_menores (
	Componente VARCHAR(13) NOT NULL, 
	Ano DECIMAL NOT NULL, 
	Beneficiario VARCHAR(43) NOT NULL, 
	RNPA DECIMAL NOT NULL, 
	Estado VARCHAR(19) NOT NULL, 
	Municipio VARCHAR(49) NOT NULL, 
	Localidad VARCHAR(47), 
	Monto_federal VARCHAR(32), 
	Monto_estatal DECIMAL
);
