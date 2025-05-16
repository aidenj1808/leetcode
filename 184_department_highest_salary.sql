/* Write your T-SQL query statement below */
SELECT Department, Employee, Salary
FROM (
    SELECT
        D.name AS Department,
        E.name AS Employee,
        E.salary AS Salary,
        RANK() OVER (PARTITION by E.departmentId order by E.salary desc) as [rank]
    FROM Employee E, Department D
    WHERE E.departmentId = D.id
) T
WHERE [rank] = 1

