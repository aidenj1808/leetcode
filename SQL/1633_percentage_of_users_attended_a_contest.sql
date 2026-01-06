/* Write your T-SQL query statement below */
SELECT R.contest_id, ROUND(COUNT(R.contest_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS [percentage]
FROM Register R
GROUP BY R.contest_id
ORDER BY [percentage] DESC, R.contest_id ASC

