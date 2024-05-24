-- Task: Create the table 'id_not_null' with 'id' as INT with default value 1 and 'name' as VARCHAR(256)

-- Create the table 'id_not_null' if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

