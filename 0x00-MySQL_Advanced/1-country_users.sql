-- A SQL script that creates a table and uses an enumeration

CREATE TABLE IF NOT EXISTS users (
	id int AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US'
);
