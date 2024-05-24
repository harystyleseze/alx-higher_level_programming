-- Task: Create the table 'force_name' with 'id' as INT and 'name' as VARCHAR(256) that can't be null

-- Create the table 'force_name' if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

