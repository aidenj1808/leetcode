/* Write your T-SQL query statement below */
SELECT MAX(T.num) AS num
FROM (
    SELECT *
    FROM MyNumbers MN
    GROUP BY MN.num
    HAVING COUNT(MN.num) = 1
) T

