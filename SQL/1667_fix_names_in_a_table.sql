/* Write your T-SQL query statement below */
SELECT U.user_id, CONCAT(UPPER(LEFT(U.name, 1)), LOWER(RIGHT(U.name, LEN(U.name) - 1))) AS [name]
FROM Users U
ORDER BY U.user_id

