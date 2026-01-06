/* Write your T-SQL query statement below */
SELECT P.product_id, ISNULL(ROUND(1.0 * SUM(P.price * US.units) / SUM(US.units), 2), 0) AS average_price
FROM Prices P
LEFT JOIN UnitsSold US
ON P.product_id = US.product_id and US.purchase_date >= P.start_date and US.purchase_date <= P.end_date
GROUP BY P.product_id

