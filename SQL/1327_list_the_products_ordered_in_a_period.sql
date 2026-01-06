/* Write your T-SQL query statement below */
SELECT P.product_name, SUM(O.unit) AS unit
FROM Products P, Orders O
WHERE P.product_id = O.product_id and O.order_date >= '2020-02-01' and O.order_date <= '2020-02-29'
GROUP BY P.product_name
HAVING SUM(O.unit) >= 100

