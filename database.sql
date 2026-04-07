CREATE DATABASE banquet_crm;

USE banquet_crm;

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    booking_date DATE,
    guests INT
);
