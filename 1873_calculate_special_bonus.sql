/* Write your T-SQL query statement below */
SELECT E.employee_id, 0 AS bonus
FROM Employees E
WHERE E.employee_id % 2 = 0 or LEFT(E.name, 1) = 'M'
UNION
SELECT E.employee_id, salary AS bonus
FROM Employees E
WHERE E.employee_id % 2 = 1 and LEFT(E.name, 1) != 'M'

