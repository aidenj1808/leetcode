/* Write your T-SQL query statement below */
with T as (
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id
    FROM RequestAccepted
)

SELECT TOP 1 T.id, COUNT(T.id) AS num
FROM T
GROUP BY T.id
ORDER BY num DESC

