SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(month) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

