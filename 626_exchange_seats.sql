/* Write your T-SQL query statement below */
SELECT
CASE
    WHEN id % 2 = 0 THEN id - 1
    WHEN id % 2 != 0 AND id + 1 NOT IN (SELECT id from seat) THEN id ELSE id + 1
END AS id,
student
FROM Seat
ORDER BY id

