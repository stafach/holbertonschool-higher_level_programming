--  Script that lists all records of the table second_table except rows where the name column does not contain a value
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
