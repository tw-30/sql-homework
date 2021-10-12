import sqlite3
import pandas as pd


db = sqlite3.connect("flight.new.db")


query1 = pd.read_sql("select f.id, f.origin, f.destination, f.carrier, count(distinct p.passenger_id) as Num_of_Passenger from passenger p join flights f on p.flightid = f.id group by f.id, f.origin, f.destination, f.carrier order by 1 ;")
query2 = pd.read_sql("select a.*, count(distinct f.id) as Num_of_Flights from airlines a join flights f on a.carrier = f.carrier group by a.carrier order by 1;")
query3 = pd.read_sql("select b.faa, b.name, b.tzone, count(f.origin) as Num_of_Flights from airports b join flights f on b.faa = f.origin group by b.faa order by 4 desc limit 3 ;")
query4 = pd.read_sql("select b.*, count(f.origin) as num_of_Flights from airports b join flights f on b.faa = f.origin group by b.faa order by 1 ;")
query5 = pd.read_sql("select p.flight_id, p.name, f.origin, f.id, f.destination from passengers p join flights f on p.flight_id = f.id order by 1 ;")
query6 = pd.read_sql("select p.flight_id, p.name, f.origin, f.id, b.name, f.destination, b2.name from passengers p join flights f on p.flight_id = f.id join airports b on b.faa = f.origin join airports b2 on b2.faa = f.destination group by p.flight_id, p.name, f.id, f.origin, b.name, f.destination, b2.name order by 1 ;")
query7 = pd.read_sql("select p.flight_id, p.name, f.id, as flight_id,  f.origin, f.destination, f.duration as duration_minutes from passengers p join flights f on p.flightid = f.id order by 1 ;")

