/* Write your T-SQL query statement below */
SELECT P.product_id, P.product_name
FROM Product P
WHERE P.product_id NOT IN (
    SELECT S.product_id
    FROM Sales S
    WHERE S.sale_date < '2019-01-01' or S.sale_date > '2019-03-31'
) and P.product_id IN (
    SELECT product_id
    FROM Sales
)

