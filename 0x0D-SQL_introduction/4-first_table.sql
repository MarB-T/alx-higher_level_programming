-- Script that creates a table called first_table in the current database
-- The database name will be passed as an argument of the mysql command
-- first_table description:
--             id INT
--             name VARCHAR(256)
-- If table first_table already exists, your script should not fail

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
