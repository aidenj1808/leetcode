/* Write your T-SQL query statement below */
SELECT date_id, make_name,
(SELECT COUNT(DISTINCT lead_id)) AS unique_leads, (SELECT COUNT(DISTINCT partner_id)) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name

