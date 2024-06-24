-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS EatExpress_dev_db;
CREATE USER IF NOT EXISTS 'EatExpress_dev'@'localhost' IDENTIFIED BY 'EatExpress_dev_pwd';
GRANT ALL PRIVILEGES ON `EatExpress_dev_db`.* TO 'EatExpress_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'EatExpress_dev'@'localhost';
FLUSH PRIVILEGES;