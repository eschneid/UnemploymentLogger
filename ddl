-- DDL

create table if not exists person
(
	id serial not null,
	fname varchar(255),
	lname varchar(255)
);

alter table person owner to postgres;

create table if not exists company
(
	id serial not null,
	name varchar(255),
	url varchar(500),
	loc_id integer
);

alter table company owner to postgres;

create table if not exists location
(
	id serial not null,
	street varchar(255),
	city varchar(255),
	state varchar(2),
	zip integer
);

alter table location owner to postgres;

create table if not exists jobsearch
(
	id serial not null,
	person_applying integer,
	company_id integer,
	title varchar(255),
	contract_company varchar(255),
	submitted_method varchar(255),
	outcome varchar(255),
	job_number varchar(255),
	date_submitted timestamp,
	additional_info varchar(500)
);

alter table jobsearch owner to postgres;

create table if not exists cde_outcome
(
	id serial not null,
	outcome varchar(100)
);

alter table cde_outcome owner to postgres;


