/* Write your T-SQL query statement below */
SELECT W1.id
FROM Weather W1, Weather W2
WHERE DATEDIFF(day, W2.recordDate, W1.recordDate) = 1 and W1.temperature > W2.temperature

