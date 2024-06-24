-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS EatExpress_test_db;
CREATE USER IF NOT EXISTS 'EatExpress_test'@'localhost' IDENTIFIED BY 'EatExpress_test_pwd';
GRANT ALL PRIVILEGES ON `EatExpress_test_db`.* TO 'EatExpress_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'EatExpress_test'@'localhost';
FLUSH PRIVILEGES;