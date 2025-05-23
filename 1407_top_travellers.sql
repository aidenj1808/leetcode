/* Write your T-SQL query statement below */
SELECT U.name, ISNULL(SUM(R.distance), 0) AS travelled_distance
FROM Users U
LEFT JOIN Rides R
ON U.id = R.user_id
GROUP BY U.id, U.name
ORDER BY SUM(R.distance) DESC, U.name ASC

