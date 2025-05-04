/* Write your T-SQL query statement below */
SELECT E.name AS Employee
FROM Employee E,
    (SELECT *
    FROM Employee E) M
WHERE E.managerId = M.id and E.salary > M.salary

