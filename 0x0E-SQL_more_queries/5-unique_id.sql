-- Task: Create the table 'unique_id' with 'id' as INT with default value 1 and unique constraint, and 'name' as VARCHAR(256)

-- Create the table 'unique_id' if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

