-- Task: Create the database 'hbtn_0d_usa' and the table 'cities' with specified constraints

-- Create the database 'hbtn_0d_usa' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the table 'cities' if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

