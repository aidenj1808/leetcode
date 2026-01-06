/* Write your T-SQL query statement below */
WITH CTE AS (
    SELECT
        pid,
        tiv_2015,
        tiv_2016,
        COUNT(CONCAT(lat, lon)) OVER (PARTITION BY CONCAT(lat, lon)) AS location_count,
        COUNT(tiv_2015) OVER (PARTITION BY tiv_2015) AS tiv_2015_count
    FROM Insurance
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM CTE
WHERE location_count = 1 AND tiv_2015_count > 1

