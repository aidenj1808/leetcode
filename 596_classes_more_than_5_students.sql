/* Write your T-SQL query statement below */
SELECT C.class
FROM Courses C
GROUP BY C.class
HAVING COUNT(C.class) >= 5

