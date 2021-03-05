CREATE DATABASE my_database;
use my_database;

CREATE TABLE students (
  name VARCHAR(20),
  surname VARCHAR(20),
  speciality_name VARCHAR(40)
);

INSERT INTO students
  (name, surname, speciality_name)
VALUES
  ('Josh', 'Brown', 'Computer Engineering'),
  ('Tom', 'Smith', 'Computer Science'),
  ('Maria', 'Williams', 'Computer Engineering');
