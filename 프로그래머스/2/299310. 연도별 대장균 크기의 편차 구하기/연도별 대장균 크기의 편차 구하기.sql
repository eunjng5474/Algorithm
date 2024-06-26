SELECT YEAR(A.DIFFERENTIATION_DATE) AS YEAR,
    (B.MAX_SIZE - A.SIZE_OF_COLONY) AS YEAR_DEV,
    A.ID
FROM ECOLI_DATA A
LEFT JOIN (
    SELECT MAX(SIZE_OF_COLONY) AS MAX_SIZE,
        YEAR(DIFFERENTIATION_DATE) AS YEAR
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)) B
ON YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY 1, 2;