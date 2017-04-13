CREATE TABLE "20082009reconversion" (
	"Año" INTEGER NOT NULL,
	"Beneficiario" VARCHAR(60) NOT NULL,
	"Nombre_proyecto" VARCHAR(151) NOT NULL,
	"Tipo_proyecto" VARCHAR(38) NOT NULL,
	"Especie" VARCHAR(40) NOT NULL,
	"Estado" VARCHAR(12) NOT NULL,
	"Municipio" VARCHAR(25) NOT NULL,
	"Localidad" VARCHAR(47) NOT NULL,
	"Monto" INTEGER NOT NULL
);
CREATE TABLE "20082013motores" (
  "Año" INTEGER NOT NULL,
  "Beneficiario" VARCHAR(60) NOT NULL,
  "RNPA" VARCHAR(61),
  "Estado" VARCHAR(12) NOT NULL,
  "Municipio" VARCHAR(25) NOT NULL,
  "Localidad" VARCHAR(47) NOT NULL,
  "Monto_federal" INTEGER NOT NULL,
  "Monto_estatal" INTEGER NOT NULL
);
CREATE TABLE "20112012pesca" (
	"Año" INTEGER NOT NULL,
	"Beneficiario" VARCHAR(165),
	"RNPA" VARCHAR(61),
	"Especie" VARCHAR(70),
	"Entidad" VARCHAR(19) NOT NULL,
	"Municipio " VARCHAR(36),
	"Localidad" VARCHAR(56),
	"Monto_federal" FLOAT
);
CREATE TABLE "20112013diesel" (
	"Año" INTEGER NOT NULL,
	"RAZON SOCIAL" VARCHAR(87),
	"CURP" VARCHAR(205),
	"RFC" VARCHAR(205),
	"RNPA" BIGINT,
	"Localidad" VARCHAR(36) NOT NULL,
	"Municipio" VARCHAR(22) NOT NULL,
	"Entidad" VARCHAR(31) NOT NULL,
	"Monto" FLOAT NOT NULL,
	"Beneficiario" VARCHAR(42)
);
CREATE TABLE "20112013gasolina" (
	"Año" INTEGER NOT NULL,
	"CURP" VARCHAR(205) NOT NULL,
	"RNPA" INTEGER NOT NULL,
	"Localidad" VARCHAR(45) NOT NULL,
	"Municipio" VARCHAR(38) NOT NULL,
	"Entidad" VARCHAR(19) NOT NULL,
	"Monto" FLOAT NOT NULL,
	"Beneficiario" VARCHAR(42) NOT NULL
);
CREATE TABLE "20112013motorescomponentes" (
  "Componente" VARCHAR(60) NOT NULL,
  "Año" INTEGER NOT NULL,
  "Beneficiario" VARCHAR(60) NOT NULL,
  "RNPA" VARCHAR(61),
  "Estado" VARCHAR(12) NOT NULL,
  "Municipio" VARCHAR(25) NOT NULL,
  "Localidad" VARCHAR(47) NOT NULL,
  "Monto_federal" INTEGER NOT NULL,
  "Monto_estatal" INTEGER NOT NULL
);
CREATE TABLE "2011electricos" (
	"Año" INTEGER NOT NULL,
	"Beneficiario" VARCHAR(37) NOT NULL,
	"RNPA" BIGINT NOT NULL,
	"Estado" VARCHAR(6) NOT NULL,
	"Municipio" VARCHAR(10) NOT NULL,
	"Localidad" VARCHAR(14) NOT NULL,
	"Monto_federal" INTEGER NOT NULL,
	"Monto_estatal" INTEGER NOT NULL
);
CREATE TABLE "2011reconversion" (
	"Año" INTEGER NOT NULL,
	"Beneficiario" VARCHAR(60) NOT NULL,
	"Nombre_proyecto" VARCHAR(151) NOT NULL,
	"Tipo_proyecto" VARCHAR(38) NOT NULL,
	"Especie" VARCHAR(40) NOT NULL,
	"Estado" VARCHAR(12) NOT NULL,
	"Municipio" VARCHAR(25) NOT NULL,
	"Localidad" VARCHAR(47) NOT NULL,
	"Monto" INTEGER NOT NULL
);
CREATE TABLE "2012integral" (
	"Año" INTEGER NOT NULL,
	"Beneficiario" VARCHAR(76) NOT NULL,
	"RNPA" VARCHAR(64) NOT NULL,
	"Nombre_proyecto" VARCHAR(156) NOT NULL,
	"Tipo_apoyo" VARCHAR(32) NOT NULL,
	"Especie" VARCHAR(73) NOT NULL,
	"Estado" VARCHAR(19) NOT NULL,
	"Municipio" VARCHAR(17) NOT NULL,
	"Localidad" VARCHAR(30) NOT NULL,
	"Monto_federal" INTEGER NOT NULL
);
CREATE TABLE "2012motoresmarinosecologicos" (
	"Año" INTEGER NOT NULL,
	"Beneficiario" VARCHAR(72) NOT NULL,
	"RNPA" BIGINT NOT NULL,
	"Localidad" VARCHAR(43) NOT NULL,
	"Municipio" VARCHAR(22) NOT NULL,
	"Estado" VARCHAR(4) NOT NULL,
	"Aprobacion Conapesca" INTEGER NOT NULL,
	"Aprobacion Gob. Edo." INTEGER NOT NULL
);
CREATE TABLE sustitucionmotores (
	"Año" INTEGER NOT NULL,
	"Programa" VARCHAR(67) NOT NULL,
	"Componente" VARCHAR(80) NOT NULL
);
