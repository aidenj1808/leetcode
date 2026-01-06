/* Write your T-SQL query statement below */
SELECT TOP 1 T.person_name
FROM (
    SELECT
        Q.turn,
        Q.person_id,
        Q.person_name,
        Q.weight,
        SUM(Q.weight) OVER (ORDER BY Q.turn) AS total_weight
    FROM Queue Q
) T
WHERE total_weight <= 1000
ORDER BY total_weight DESC

