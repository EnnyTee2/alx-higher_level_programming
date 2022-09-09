-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    PRIMARY KEY(id)
    id   INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT_NULL,
    FOREIGN KEY(state_id) REFERENCES states.id,
    name VARCHAR(256) NOT NULL
);
