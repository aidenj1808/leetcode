/* Write your T-SQL query statement below */
SELECT C.name AS Customers
FROM Customers C
WHERE C.id not in
    (SELECT O.customerId
    FROM Orders O)

