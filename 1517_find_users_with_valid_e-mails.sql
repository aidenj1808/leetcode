/* Write your T-SQL query statement below */
SELECT *
FROM Users 
WHERE mail LIKE '[a-zA-Z]%@leetcode.com' AND LEFT(mail, LEN(mail) - 13) NOT LIKE '%[^a-zA-Z0-9-_.]%'

