CREATE TABLE 2014_beneficiarios_modernizacion_embarcaciones_mayores (
	Ano DECIMAL NOT NULL, 
	Estado VARCHAR(15) NOT NULL, 
	Puerto VARCHAR(14) NOT NULL, 
	Beneficiario VARCHAR(108) NOT NULL, 
	RNPA DECIMAL, 
	Embarcacion VARCHAR(32) NOT NULL, 
	Monto_aprobado DECIMAL NOT NULL, 
	Pagado VARCHAR(12), 
	2014_nov_dic_pasivos DECIMAL, 
	2014_enero_marzo_pasivos VARCHAR(13), 
	desistido DECIMAL, 
	acta_administrativa DECIMAL, 
	reintegro DECIMAL, 
	pdte_comprobar_pago DECIMAL
);
