DELETE FROM beneficiarios
WHERE id IN (SELECT id
              FROM (SELECT id,
                             ROW_NUMBER() OVER (partition BY "Año", "Beneficiario", "RNPA" ORDER BY id) AS rnum
                     FROM tablename) t
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
