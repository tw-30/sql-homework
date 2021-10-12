CREATE TABLE airports 
( faa text primary key, 
name text not null,
tzone text not null
);
CREATE TABLE airlines(
carrier text primary key, 
name text not null
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE carrier (
carrier text primary key, 
name text not null
);
CREATE TABLE passengers (
flight_id integer primary key,
name text not null
);
CREATE TABLE flights (
id integer primary key autoincrement, 
origin text not null
,
destination text not null, 
duration integer default null,
name text not null,
carrier text not null,
foreign key (origin) references airports (faa), 
foreign key (destination) references airports (faa)
);
