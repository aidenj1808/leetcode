/* Write your T-SQL query statement below */
SELECT U.name, SUM(T.amount) AS balance
FROM Users U, Transactions T
WHERE U.account = T.account
GROUP BY U.name
HAVING SUM(T.amount) > 10000

