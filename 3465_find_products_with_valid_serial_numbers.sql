/* Write your T-SQL query statement below */
SELECT *
FROM products P
WHERE P.description LIKE '%[^a-zA-Z]SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]%' AND
P.description NOT LIKE '%[^a-zA-Z]SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]%'
ORDER BY P.product_id ASC

