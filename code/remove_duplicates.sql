DELETE FROM beneficiarios
WHERE ID IN (SELECT ID
              FROM (SELECT ID,
                             ROW_NUMBER() OVER (partition BY "Beneficiario", "RNPA" ORDER BY ID) AS rnum
                     FROM beneficiarios) t
              WHERE t.rnum > 1);

DELETE
FROM beneficiarios
WHERE "Beneficiario" is null;

SELECT *
FROM beneficiarios
WHERE "Beneficiario" is null;


DELETE FROM lugares
WHERE "Id" IN (SELECT "Id"
              FROM (SELECT "Id",
                             ROW_NUMBER() OVER (partition BY "Estado", "Municipio", "Localidad" ORDER BY "Id") AS rnum
                     FROM lugares) t
              WHERE t.rnum > 1);
