-- Creates a database on a server
-- Creates the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test' @ 'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant permissions on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @ 'localhost';

-- Grant permission on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @ 'localhost';
