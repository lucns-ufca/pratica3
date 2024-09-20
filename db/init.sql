CREATE DATABASE library;
USE library;


CREATE TABLE books (
  Autor VARCHAR(50),
  Title VARCHAR(50)
);


INSERT INTO books
  (Autor, Title)
VALUES
  ('Fiódor Dostoiévski', 'Crime e Castigo'),
  ('Machado de Assis', 'Dom Casmurro');   