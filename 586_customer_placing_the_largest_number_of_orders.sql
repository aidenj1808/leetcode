/* Write your T-SQL query statement below */
SELECT TOP 1 O.customer_number
FROM Orders O
GROUP BY O.customer_number
ORDER BY COUNT(O.order_number) DESC

