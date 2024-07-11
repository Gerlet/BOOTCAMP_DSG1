-- para crear y usar base de datos
create database db_codigo;
use db_codigo;
-- para crear tablas
create table alumno(
	id INT not null primary key auto_increment,
	nombre varchar(255) not null,
	email varchar(100) not null,
	celular varchar(20) 
);
-- para modificar tabla
alter  table alumno 
add column nota INT;

ALTER TABLE alumno ADD pais varchar(100) DEFAULT "Perú" NULL;

-- eliminar tabla

drop table alumno;