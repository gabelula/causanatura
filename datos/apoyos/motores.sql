CREATE TABLE motores (
	Ano DECIMAL NOT NULL, 
	Beneficiario VARCHAR(72) NOT NULL, 
	RNPA VARCHAR(10), 
	Estado VARCHAR(19) NOT NULL, 
	Municipio VARCHAR(40) NOT NULL, 
	Localidad VARCHAR(47), 
	Monto_federal DECIMAL NOT NULL, 
	Monto_estatal DECIMAL
);
