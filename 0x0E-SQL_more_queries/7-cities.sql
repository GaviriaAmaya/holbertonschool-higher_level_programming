-- Create a DB hbtn usa. Then creates a table of cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
       id INT NOT NULL AUTO_INCREMENT UNIQUE,
       state_id INT NOT NULL,
       name VARCHAR(256),
       PRIMARY KEY (id),
       FOREIGN KEY (state_id)
       REFERENCES hbtn_0d_usa.states(id)
)
