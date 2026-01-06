# Write your MySQL query statement below
SELECT *
FROM Cinema C
WHERE C.description != 'boring' and C.id % 2 != 0
ORDER BY c.rating DESC

