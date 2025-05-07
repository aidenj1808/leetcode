/* Write your T-SQL query statement below */
SELECT P.project_id, ROUND(AVG(1.00 * E.experience_years), 2) AS average_years
FROM Project P, Employee E
WHERE P.employee_id = E.employee_id
GROUP BY P.project_id

