-- Creates a database on a server
-- Creates the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
           IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant permissions on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
   TO 'hbnb_dev'@'localhost';

-- Grant permission on performance_schema
GRANT SELECT ON performance_schema.*
   TO 'hbnb_dev'@'localhost';
