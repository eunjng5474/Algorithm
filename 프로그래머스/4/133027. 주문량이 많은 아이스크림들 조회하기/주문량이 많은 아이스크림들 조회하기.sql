-- 코드를 입력하세요
SELECT H.FLAVOR FROM FIRST_HALF H
JOIN JULY J ON H.FLAVOR = J.FLAVOR
GROUP BY FLAVOR
ORDER BY SUM(H.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
LIMIT 3;