--set the output format of the result set to TSV (Tab-Separated Values) to compare the query results obtained, with the autograder.
!outputformat tsv

CREATE VIEW IF NOT EXISTS "powers" (pk VARCHAR PRIMARY KEY, 
                      "professional"."name" VARCHAR,  
                      "personal"."power" VARCHAR, 
                      "personal"."hero" VARCHAR);

SELECT p."name" AS Name1, p2."name" AS Name2, p."power" AS Power
FROM "powers" AS p
JOIN "powers" AS p2
ON p."power" = p2."power"
WHERE p."hero" = 'yes' AND p2."hero" = 'yes';