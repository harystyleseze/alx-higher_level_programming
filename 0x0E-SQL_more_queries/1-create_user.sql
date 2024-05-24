-- Task: Create the MySQL server user 'user_0d_1' with all privileges

-- Create the user 'user_0d_1' if it does not exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to 'user_0d_1' on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

