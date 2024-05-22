-- Task: List all records of second_table with a non-empty name value, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

