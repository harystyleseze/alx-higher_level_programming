-- Task: List all cities of California without using JOIN keyword

-- Select California state ID using a subquery
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;

