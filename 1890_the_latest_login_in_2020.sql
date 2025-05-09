/* Write your T-SQL query statement below */
SELECT L.user_id, MAX(L.time_stamp) AS last_stamp
FROM Logins L
WHERE YEAR(L.time_stamp) = 2020
GROUP BY L.user_id

