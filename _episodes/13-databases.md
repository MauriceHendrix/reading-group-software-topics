---
title: Introduction to databases
teaching: 45
exercises: 0
questions:
- "I want to do something slightly advanced with structured data: how do I use a database for that?"
objectives:
- "Know the difference between structured and unstructured data."
- "An idea of advantages of databases vs. simpler storage formats (e.g. CSV)."
- "Some idea of different types of popular databases system types (SQL vs NoSQL)."
- "Basic understanding of how to create and query a relational database in SQL."
---

When working with data you will come across the need to store the data. Whether it's for your own use, analysis or to share with others. Today we'll look at using databases to store data.

## Structured vs. unstructured data
![Structured vs. unstructured data](https://lawtomated.com/wp-content/uploads/2019/04/structuredVsUnstructuredIgneos.png)

## Why not just use a CSV file isn't that easier?
CSV files are very good for ata transport & distribution, CSVs are easy to understand and iterate over with a script. So...

- A database is much better at handling multiple users and scaling up in terms of size (imagine the wbelab: what would happen if 2 poeple sign up at same time if user info is stored in a CSV?)
- A database allows more precise structure: data has a specific type and if well designed isn't replicated unnecessarily.
- Answering more complex questions / finding more specific bits of data can be easier
- Some data is difficult to store in a single CSV. e.g.: Store planets and an aribtrary number of moons. What if a new planet or new moon is discovered? If you add more columns to a CSV any of your processing scripts will also need to change!

## Main types of databases
![SQL vs NoSQL](https://miro.medium.com/max/2828/1*RtLmDhbpg2h1I8cG0l4yyg.png)

## Relational databases & SQL query language
Some popular solutions include:
- postgresql (popular open source db, used by weblab)
- MySql (popular open source db, used by weblab)
- Oracle
- Microsoft SQL server
- * SqlLite * (light-weight open source, doesn't require seperate server)


A relational database is based on tables & relations between tables. We'll briefly look at:
- Creating tables
- Relationships
- Inserting data
- import CSV
- Update / delete
- Using database in a python script
- Retreiving data
pk, null, autoincrement
prepared statements

* Top tip: There are tools with a user interface for most database systems (e.q. SqlList workbench) that let you do most things. Use them for one off operations and to perfect more complicated queries! *

## Creating tables
Best done via the tool. You create a table with a name, and fields of a certain type. E.g:
~~~
CREATE TABLE "ions" (
	"id"	INTEGER,
	"name"	TEXT,
	"valence"	INT,
	"mobility"	REAL,
	"activity_solution"	REAL,
	"activity_pipette"	REAL,
	PRIMARY KEY("id")
)
~~~
{: .language-sql}

Interesting options here are:
- Not Null (by default you are allowed to have Null values)
- Default (to fall back on when inserting data with missing / null values)
- Unique (this value must be unique in the column of the table)
- primary key (can be multiple values e.g. name & address: must be unique and be the main way to identify rows, used in other tables to identify relationships)
- Auto increment (let the database pick the next number, often used as conveniant primary key)


## Inserting data
Use a tool if it's a one off insert!

~~~
INSERT INTO ion_species VALUES(NULL, 'CL', -1, 1.0388, 149.6, 134)
~~~
{: .language-sql}


## Using database in a python script
The very basic form for data extraction is:
~~~
import sqlite3

# For SqlListe you specify a file, for most other database systems it would be server address, username & password
# Using the with syntax will automatically close the connection once it's no longer needed
with sqlite3.connect('ion-species.db') as con:
    cur = con.cursor()
    cur.execute('select * from ions')
    data = cur.fetchall()
    print(data)

~~~
{: .language-python}

## Retreiving data
The very basic form for data extraction is:
~~~
SELECT * FROM ions
WHERE ...
~~~
{: .language-sql}

###Other important things:
- where condition
~~~
select count(*) from ions;
select count(*) from ions where mobility >= 1.0;
~~~
{: .language-sql}

- order by
~~~
select * from ions order by valence asc, mobility desc
~~~
{: .language-sql}

- rename with as, add columns
~~~
select name, mobility as mb, 25*mobility/valence as value from ions;
~~~
{: .language-sql}

- count, sum, avg
~~~
select avg(valence) from ions;
select species_id, avg(valence) from ions;
~~~
{: .language-sql}

- group by
~~~
select species_id, avg(valence) from ions group by species_id;
~~~
{: .language-sql}

- join
~~~
select * from ions join species on ions.species_id = species.id;
select * from ions left join species on ions.species_id = species.id;
select avg(ions.valence), species.name from ions join species on ions.species_id = species.id group by species_id;
~~~
{: .language-sql}

- subqueries
~~~
select name, mobility from ions where mobility >= avg(mobility);
select name, mobility from ions where mobility >= (select avg(mobility) from ions);
select name, mobility, (select avg(mobility) from ions) as avgmob from ions where mobility > avgmob;
~~~
{: .language-sql}


## Views
Essentially store a query and access it as if it is a tble:
~~~
CREATE [TEMP] VIEW [IF NOT EXISTS] view_name[(column-name-list)]
AS 
   select-statement;
~~~
{: .language-sql}


## import CSV
Ideally use a tool!

## Delete
This is very similar to retreiving data (more later) except for the delete keyword:
~~~
-- delete data
DELETE FROM ion_species 
WHERE ...

-- or delete table:
DROP TABLE IF EXISTS ion_species
~~~
{: .language-sql}

## Update
Also very similar to data retreival:
~~~
UPDATE ion_species
SET name = 'new name', valance = 99 , ...
WHERE ...;
~~~
{: .language-sql}


[SqlLite tutorial](https://www.sqlitetutorial.net/sqlite-python/)

[DB Browser for SQLite tool](https://sqlitebrowser.org/)

{% include links.md %}
