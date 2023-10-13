-- 1. 재귀 사용
WITH RECURSIVE num (HOUR) AS
(
    SELECT 0
    UNION ALL
    SELECT HOUR + 1 FROM num WHERE HOUR < 23
)

SELECT num.HOUR, COUNT(A.ANIMAL_ID) AS COUNT
FROM num
LEFT JOIN ANIMAL_OUTS A
    ON num.HOUR = HOUR(A.DATETIME)
GROUP BY HOUR;

-- 변수 선언
SET @HOUR := -1;
SELECT (@HOUR := @HOUR + 1) AS HOUR,
(   
    SELECT COUNT(ANIMAL_ID)
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @HOUR
) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;
