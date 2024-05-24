-- Task: List all cities with their corresponding state names without using JOIN keyword

-- Select cities.id, cities.name, and states.name
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;

