-- Creates the table Unique_Id on my server
CREATE TABLE IF NOT EXISTS unique_id(
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
)
