/* Write your T-SQL query statement below */
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y' or employee_id not in (
    SELECT employee_id
    FROM Employee E1
    WHERE E1.primary_flag = 'Y'
)

