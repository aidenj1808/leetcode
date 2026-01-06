/* Write your T-SQL query statement below */
SELECT P.email AS Email
FROM PERSON P
GROUP BY P.email
HAVING COUNT(*) > 1

