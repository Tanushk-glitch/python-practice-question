create database university;

use university;

create table dept(
name varchar(50),
id int primary key
);

create table students(
 name varchar(20),
 gender varchar(1),
 phone_no int,
 address varchar(255),
 dob date,
 dept_id int,
 foreign key (dept_id) references dept(id)
 
 on delete cascade
 on update cascade
);

create table teacher(
name varchar(50),
phone_no int,
teacher_id int primary key,
dept_id int,
foreign key (dept_id) references dept(id)

);

create table courses(
courses_name varchar(50),
credits varchar(1),
course int ,
foreign key (course) references dept(id),
course_id int,
foreign key (course_id) references teacher(teacher_id)
);

create table enrollment(
grade varchar(2),
engrollment_date date,
en_id int,
foreign key (en_id) references students(dept_id),
enrollment int,
foreign key (enrollment) references courses(course_id)

);


