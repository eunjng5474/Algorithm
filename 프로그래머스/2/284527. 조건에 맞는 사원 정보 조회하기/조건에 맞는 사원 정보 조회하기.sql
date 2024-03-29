SELECT G.SCORE, G.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E, 
    (SELECT SUM(SCORE) AS SCORE, EMP_NO
    FROM HR_GRADE
    GROUP BY EMP_NO
    ORDER BY SCORE DESC
    LIMIT 1) G
WHERE E.EMP_NO = G.EMP_NO;