/* Write your T-SQL query statement below */
SELECT SP.name
FROM SalesPerson SP
WHERE SP.sales_id NOT IN (
    SELECT O.sales_id
    FROM Orders O
    WHERE O.com_id = (
        SELECT C.com_id
        FROM Company C
        WHERE C.name = 'RED'
    )
)

