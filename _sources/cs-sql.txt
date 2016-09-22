sql (``cs-sql.rst``)
""""""""""""""""""""

.. contents:: `Table of contents`
   :depth: 2
   :local:

#####
mysql
#####
***************
Auto completion
***************
http://stackoverflow.com/questions/8332338/autocompletion-in-the-mysql-command-line-client

``mysql> \#``
****************
Random overflows
****************
- http://stackoverflow.com/questions/8096550/mysql-determine-which-database-is-selected
  
  - ``SELECT DATABASE();``

- https://bugs.mysql.com/bug.php?id=74899

#############
Codezen mysql
#############
http://zetcode.com/databases/mysqltutorial/quick/

::

    mysql> pager less

.. code-block:: sql

    mysql> SHOW TABLES;
    +-----------------+
    | Tables_in_world |
    +-----------------+
    | City            |
    | Country         |
    | CountryLanguage |
    +-----------------+

    -- print schema
    DESCRIBE City;
    +-------------+----------+------+-----+---------+----------------+
    | Field       | Type     | Null | Key | Default | Extra          |
    +-------------+----------+------+-----+---------+----------------+
    | ID          | int(11)  | NO   | PRI | NULL    | auto_increment |
    | Name        | char(35) | NO   |     |         |                |
    | CountryCode | char(3)  | NO   | MUL |         |                |
    | District    | char(20) | NO   |     |         |                |
    | Population  | int(11)  | NO   |     | 0       |                |
    +-------------+----------+------+-----+---------+----------------+

*********
mysqldump
*********
.. code-block:: bash

    $ mysqldump -u root -p world City > city.sql

Then you can reload table after DROP TABLE via source

.. code-block:: sql

    mysql> DROP TABLE City;
    mysql> SHOW TABLES;
    +-----------------+
    | Tables_in_world |
    +-----------------+
    | Country         |
    | CountryLanguage |
    +-----------------+

    mysql> source city.sql
    mysql> SHOW TABLES;
    +-----------------+
    | Tables_in_world |
    +-----------------+
    | City            |
    | Country         |
    | CountryLanguage |
    +-----------------+

    mysql> source city.sql

**********************************
Run sql statement from commandline
**********************************
.. code-block:: bash

    $ # -e option :)
    $ mysql -u tak -p world -e "SELECT * FROM City" > city

******************
Bunch of functions
******************
.. code-block:: bash

    mysql> SELECT COUNT(Id) AS 'Number of rows' FROM City;
    +----------------+
    | Number of rows |
    +----------------+
    |           4079 |
    +----------------+

    mysql> SELECT Name, Population FROM City
        -> WHERE Population = (SELECT Max(Population) FROM City);
    +-----------------+------------+
    | Name            | Population |
    +-----------------+------------+
    | Mumbai (Bombay) |   10500000 |
    +-----------------+------------+

    -- shows table is a view or not as well
    mysql> SHOW FULL TABLES;
    +----------------+------------+
    | Tables_in_mydb | Table_type |
    +----------------+------------+
    | AA             | BASE TABLE |
    ...
    | Chars          | BASE TABLE |
    | CheapCars      | VIEW       |
    | Customers      | BASE TABLE |
    | Dates          | BASE TABLE |
    | Decimals       | BASE TABLE |
    | FavoriteCars   | VIEW       |
    ...

    
    mysql> select @autocommit;
    +-------------+
    | @autocommit |
    +-------------+
    | NULL        |
    +-------------+
    1 row in set (0.00 sec)
*************
Write to file
*************
http://zetcode.com/databases/mysqltutorial/select/

::

    mysql> SELECT * INTO OUTFILE '/tmp/cars.txt'
        -> FIELDS TERMINATED BY ','
        -> LINES TERMINATED BY '\n'
        -> FROM Cars;

*****************
Write to csv file
*****************
http://zetcode.com/databases/mysqltutorial/datamanipulation/

::

    mysql> SELECT * INTO OUTFILE '/tmp/books.csv'
        -> FIELDS TERMINATED BY ','
        -> LINES TERMINATED BY '\n'
        -> FROM Books;

    $ cat /tmp/books.csv 
    1,War and Peace,Leo Tolstoy
    2,The Brothers Karamazov,Fyodor Dostoyevsky
    3,Paradise Lost,John Milton
    4,The Insulted and Humiliated,Fyodor Dostoyevsky
    5,Cousin Bette,Honore de Balzac

*************
Read csv file
*************
::

    mysql> LOAD DATA INFILE '/tmp/books.csv'    
        -> INTO TABLE Books    
        -> FIELDS TERMINATED BY ','    
        -> LINES TERMINATED BY '\n';

***********************
write and read xml file
***********************
.. code-block:: bash

    $ # --xml option, -e to exectute statement and then quit monitor
    $ mysql -uroot -p --xml -e 'SELECT * FROM mydb.Books' > books.xml

Read in mysql command line::

    mysql> LOAD XML INFILE '/home/vronskij/programming/mysql/books.xml' INTO TABLE Books;
#############
MYSQL codezen
#############

Started from http://zetcode.com/db/mysqlpython/

.. code-block:: bash

    $ mysql -u root -p
    mysql> CREATE DATABASE testdb;
    mysql> CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'test623';
    mysql> USE testdb;
    mysql> GRANT ALL ON testdb.* TO 'testuser'@'localhost';
    mysql> quit;


.. code-block:: python

    import _mysql
    con = _mysql.connect('localhost', 'testuser', 'test623', 'testdb')
    con.query("SELECT VERSION()")
    result = con.use_result()
    print "MySQL version: %s" % \
        result.fetch_row()[0]
    con.close()

***************************
Create and populate a table
***************************
.. code-block:: python

    import MySQLdb as mdb
    # 1 = host, 2 = username, 3 = password, 4 = database name
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database version : %s " % ver
    #con.close()

    # create database
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
    con.commit() # make insertion persistent

*************
Retrieve data
*************
.. code-block:: python

    >>> import MySQLdb as mdb
    >>> con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
    >>> cur = con.cursor()
    >>> cur.execute("SELECT * FROM Writers")
    >>> 
    >>> rows = cur.fetchall()
    >>> for row in rows:
    >>>     print row
    (1L, 'Jack London')
    (2L, 'Honore de Balzac')
    (3L, 'Lion Feuchtwanger')
    (4L, 'Emile Zola')
    (5L, 'Truman Capote')

    >>> # fetch rows one by one
    >>> cur.execute("SELECT * FROM Writers")
    >>> for i in range(cur.rowcount):
    >>>     row = cur.fetchone()
    >>>     print row[0], row[1]
    1 Jack London
    2 Honore de Balzac
    3 Lion Feuchtwanger
    4 Emile Zola
    5 Truman Capote


***********
cursor type
***********
Default cursor type is **Tuple of Tuples**. 
We can use a **dictionary cursor** too (so we can refer to data by their **column-names**)

.. code-block:: python

    >>> con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
    >>> cur = con.cursor(mdb.cursors.DictCursor)
    >>> cur.execute("SELECT * FROM Writers LIMIT 4")
    >>> rows = cur.fetchall()
    >>> for row in rows:
    >>>     print row["Id"], row["Name"]
    1 Jack London
    2 Honore de Balzac
    3 Lion Feuchtwanger
    4 Emile Zola
    >>> rows
    Out[64]:
    ({'Id': 1L, 'Name': 'Jack London'},
     {'Id': 2L, 'Name': 'Honore de Balzac'},
     {'Id': 3L, 'Name': 'Lion Feuchtwanger'},
     {'Id': 4L, 'Name': 'Emile Zola'})


**************
Column headers
**************
print column headers with the data from the database table.

.. code-block:: python

    >>> cur = con.cursor()
    >>> cur.execute("SELECT * FROM Writers LIMIT 5")
    >>> rows = cur.fetchall()
    >>> # column names are considered to be 'meta data', obtained from the cursor object
    >>> desc = cur.description
    >>> # description attribute of the cursor returns information about each of the result columns of a query.
    >>> print "%s %3s" % (desc[0][0], desc[1][0])
    Id Name

****************************************************************
Use *prepared statements* (placeholders to avoid sql injections)
****************************************************************
- The Python DB API specification suggests **5 different ways** how to build prepared statements. 
- The MySQLdb module supports one of them, the **ANSI printf format codes**.

.. code-block:: python

    >>> cur = con.cursor()
    >>> # ANSI  %s string replacement
    >>> cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", 
    >>>     ("Guy de Maupasant", "4"))        
    >>> print "Number of rows updated:",  cur.rowcount
    Number of rows updated: 1


*****************************
Insert images using BLOB type
*****************************
.. code-block:: bash

    mysql> CREATE TABLE Images(Id INT PRIMARY KEY, Data MEDIUMBLOB);
    Query OK, 0 rows affected (0.08 sec)

.. code-block:: python

    def read_image():
        fin = open("woman.jpg")    
        img = fin.read()
        return img

    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
     
    with con:
        cur = con.cursor()
        data = read_image()
        cur.execute("INSERT INTO Images VALUES(1, %s)", (data, ))


**********
Read image
**********
.. code-block:: python

    def writeImage(data):
        fout = open('woman2.jpg', 'wb')
        with fout:
            fout.write(data)

    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

    with con:
        cur = con.cursor()
        cur.execute("SELECT Data FROM Images WHERE Id=1")
        data = cur.fetchone()[0]
        writeImage(data)    

*******************
Transaction support
*******************
.. admonition:: InnoDB vs MyISAM storage engine
   
   The MySQL database has different types of storage engines. The most common are the **MyISAM** and the **InnoDB** engines. **Since MySQL 5.5, InnoDB becomes the default storage engine**. 

   There is a trade-off between data security and database speed. The MyISAM tables are faster to process and they do not support transactions. The commit() and rollback() methods are not implemented. They do nothing. On the other hand, the InnoDB tables are more safe against the data loss. They support transactions. They are slower to process.

######
SQLite
######
- http://stackoverflow.com/questions/13024525/sqlite3-command-line-how-to-show-less-more-output
- http://superuser.com/questions/561087/strange-keyboard-when-using-sqlite-shell-on-linux
  
  - http://superuser.com/questions/82408/sqlite-with-readline-support-on-ubuntu ``rlwrap sqlite3 database.db``
- http://stackoverflow.com/questions/19710968/sqlite3-prompting-instead-of-sqlite
- http://stackoverflow.com/questions/12730390/copy-table-structure-to-new-table-in-sqlite3

.. code-block:: sql

    SELECT sql FROM sqlite_master WHERE type='table' AND name='mytable'
###############
Overflow stuffs
###############
********************
Random uncategorized
********************
- http://stackoverflow.com/questions/6076984/how-do-i-save-the-result-of-a-query-as-a-csv-file
- http://stackoverflow.com/questions/18387209/sqlite-syntax-for-creating-table-with-foreign-key ``PRAGMA foreign_keys = 1``

**************************
INSERT INTO vs SELECT INTO
**************************
- http://stackoverflow.com/questions/6947983/insert-into-vs-select-into

    Use INSERT when the table exists. Use SELECT INTO when it does not. 

- http://stackoverflow.com/questions/8560619/sql-server-select-into-versus-insert-into-select
- http://stackoverflow.com/questions/10631326/difference-between-select-into-and-insert-into-from-old-table

*********************************
Between clause vs ``<=`` and such
*********************************
- http://stackoverflow.com/questions/4809083/between-clause-versus-and
- http://stackoverflow.com/questions/1960801/why-use-the-between-operator-when-we-can-do-without-it
- http://stackoverflow.com/questions/5125076/sql-query-to-select-dates-between-two-dates
- http://stackoverflow.com/questions/1884818/how-do-i-add-a-foreign-key-to-an-existing-sqlite-3-6-21-table

*************************
Drop unnamed constraints?
*************************
- http://stackoverflow.com/questions/670946/dropping-unnamed-constraints
- http://stackoverflow.com/questions/1430456/how-to-drop-sql-default-constraint-without-knowing-its-name
- http://stackoverflow.com/questions/18334662/how-to-drop-unnamed-primary-key-constraint
- http://stackoverflow.com/questions/13856946/drop-unnamed-foreign-key-in-mysql
- http://dba.stackexchange.com/questions/89346/how-do-you-drop-an-unnamed-check-constraint-in-a-postgresql-table/89347

**********************************
Doing stuffs from the command line
**********************************
.. code-block:: bash

    $ ls
    person-demo.db  readme.md  referencing.sql

    # ah nice, can also use sqlite utility functions
    $ sqlite3 person-demo.db ".table"
    breed       person      person_pet  pet         species   
    $ sqlite3 person-demo.db ".schema breed"
    CREATE TABLE breed (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species_id INTEGER
    );
    $ sqlite3 person-demo.db "SELECT * FROM pet"
    0|Einstein|2|2|1|1
    1|Hollie|1|8|1|1


    $ sqlite3 person-demo.db "SELECT * from breed"
    -- Loading resources from /home/takanori/.sqliterc

    id          name        species_id
    ----------  ----------  ----------
    0           Black       0         
    1           German She  0         
    2           Poodle      1         

    $ sqlite3 person-demo.db ".dump" | pygmentize -l sql | less

    $ sqlite3 --help
    Usage: sqlite3 [OPTIONS] FILENAME [SQL]
    FILENAME is the name of an SQLite database. A new database is created
    if the file does not previously exist.
    OPTIONS include:
       -ascii               set output mode to 'ascii'
       -bail                stop after hitting an error
       -batch               force batch I/O
       -column              set output mode to 'column'
       -cmd COMMAND         run "COMMAND" before reading stdin
       -csv                 set output mode to 'csv'
       -echo                print commands before execution
       -init FILENAME       read/process named file
       -[no]header          turn headers on or off
       -help                show this message
       -html                set output mode to HTML
       -interactive         force interactive I/O
       -line                set output mode to 'line'
       -list                set output mode to 'list'
       -lookaside SIZE N    use N entries of SZ bytes for lookaside memory
       -mmap N              default mmap size set to N
       -newline SEP         set output row separator. Default: '\n'
       -nullvalue TEXT      set text string for NULL values. Default ''
       -pagecache SIZE N    use N slots of SZ bytes each for page cache memory
       -scratch SIZE N      use N slots of SZ bytes each for scratch memory
       -separator SEP       set output column separator. Default: '|'
       -stats               print memory stats before each finalize
       -version             show SQLite version
       -vfs NAME            use NAME as the default VFS

#############################
Style guidelines, conventions
#############################
- http://stackoverflow.com/questions/272210/sql-statement-indentation-good-practice
- http://www.sqlstyle.guide/

#######################
Basic commands/keywords
#######################
.. code-block:: sql
    :linenos:

    WHERE name = 'Japan'
    ORDER BY name
    ORDER BY year DESC, winner
    WHERE name IN ('Norway', 'Sweden', 'Finland', 'Denmark')
    WHERE income BETWEEN 2000 AND 2500 -- same as >=2000 AND <=2500
    WHERE field1 <= 500 OR field2 <10
    WHERE field1 <= 500 AND field2 <10
    WHERE field LIKE '%G' -- end with G
    WHERE field LIKE '____' -- exactly 4 chars
    ROUND(gdp/500,2) -- round to 2 decimcal places
    WHERE gdp IS NULL
    WHERE gdp IS NOT NULL
    x.name != y.name

    WHERE capital = concat(name, ' City')

    -- ``ALL`` to allow >= or > or < or <=to act over a list.
    WHERE population >= ALL(SELECT population FROM world WHERE population>0)


    -- Aggregate functions --
    SELECT SUM(population) FROM world
    SELECT AVG(population) FROM world
    SELECT DISTINCT(continent) FROM world -- list all continents just once
    SELECT COUNT(name) FROM world WHERE area >= 1000000 -- # countries


#######
sql-zoo
#######
http://sqlzoo.net/wiki/SELECT_basics

*************
SELECT basics
*************
- http://sqlzoo.net/wiki/SELECT_basics

  - https://github.com/jisaw/sqlzoo-solutions/blob/master/select-basics.sql
- http://sqlzoo.net/wiki/SELECT_names
- http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial

  - https://github.com/jisaw/sqlzoo-solutions/blob/master/select-from-world.sql


.. code-block:: sql
    :linenos:

    -- ultra basics
    SELECT name, population FROM world
    WHERE name='Germany'

    -- select countries whose capital ends with "City"
    SELECT name FROM world
    WHERE capital = concat(name, ' City')

    -- simple math operation allowed for column display 
    SELECT name, gdp/population FROM world
    WHERE area < 5000 AND gdp > 500000

    SELECT name, population FROM world
    WHERE name IN ('Norway', 'Sweden', 'Finland', 'Denmark')

    SELECT name, area/1000 FROM world
    WHERE area BETWEEN 200000 AND 250000

    SELECT name, population, area FROM world
    WHERE (area > 3000000 AND population < 250000000)
      OR (area < 3000000 and population > 250000000)

    -- round to 2 decimal palces
    SELECT name, ROUND(population/1000,2), ROUND(gdp/10000, 2) FROM world
    WHERE continent = 'South America'

    -- show countries with per-capita GDP > 1 trillion dollars
    SELECT name, ROUND(gdp/population, -3) FROM world -- round to nearest 1000
    WHERE gdp > 1000000000000

    SELECT *
    FROM nobel 
    WHERE (subject='Medicine' AND yr <1910) OR
          (subject='Literature' AND yr>=2004)

sorting records with ORDER BY
=============================
.. code-block:: sql
    :linenos:

    -- simple math operation allowed for column display 
    SELECT name, gdp/population FROM world
    WHERE area < 5000 AND gdp > 500000
    ORDER BY name

    
    -- show most recent first, then by name order
    SELECT winner, yr, subject
    FROM nobel 
    WHERE winner LIKE 'Sir%'
    ORDER BY yr DESC, winner

    SELECT winner, subject
    FROM nobel
    WHERE yr=1984
    ORDER BY subject IN ('Physics','Chemistry'),subject,winner


wildcards
=========
wildcards using ``LIKE`` and ``%`` wildcard

- ``%`` kinda like ``*`` in shell
- ``_`` kinda like ``?`` in shell

.. code-block:: sql
    :linenos:

    
    /* ``%`` here is a wildcard (seems like ``*`` in shell)    */
    SELECT name FROM world
    WHERE name LIKE 'G%' -- counteris beginning with G
    WHERE name LIKE '%G' -- countries ending with G
    WHERE name LIKE '%x%' -- countries containing letter x
    WHERE name LIKE '%oo%' -- contains "oo" in the name
    WHERE name LIKE '%land' -- countries ending with "land"
    WHERE name LIKE 'C%ia' -- begin with "C", aned with "ia" (eg, Cambodia_
    WHERE name LIKE '%a%a%a%' -- contains 3 or more 'a'
    WHERE name LIKE '%o__o%' -- two "o" chars separaeted by two others
    WHERE name LIKE '____' -- countries with exactly 4 chars

    -- countries that have "t" as the 2nd char, and sort order
    SELECT name FROM world
    WHERE name LIKE '_t%'
    ORDER BY name

    -- capital containing the name of the capital (eg, "Mexico city")
    SELECT name FROM world
    WHERE capital LIKE concat('%', name, '%') 

    -- 
    SELECT name, capital FROM world
    WHERE capital LIKE concat(name, '_%')

    /*
    15.
    For Monaco-Ville the name is Monaco and the extension is -Ville.
    Show the name and the extension where the capital is an extension of name of the country
    */
    SELECT name,mid(capital,LENGTH(name)+1) ext FROM world
    WHERE capital LIKE concat(name,'_%')


CASE statement
==============
http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial

.. code-block:: sql
    :linenos:

    /* Show the name - but substitute Australasia for Oceania - 
     for countries beginning with N.    */
    SELECT name, CASE WHEN continent='Oceania' THEN 'Australasia'
                      ELSE continent END
      FROM world
     WHERE name LIKE 'N%'

    /*
    Show the name and the continent - but substitute Eurasia for Europe and Asia; substitute America - for each country in North America or South America or Caribbean. Show countries beginning with A or B
    */
    SELECT name, CASE WHEN continent IN ('Europe','Asia') THEN 'Eurasia'
                      WHEN continent IN ('North America','South America','Caribbean') THEN 'America'
                      ELSE continent END
      FROM world
     WHERE name BETWEEN 'A' AND 'C'


- Countries in Eurasia and Turkey go to Europe/Asia
- Oceania becomes Australasia
- Caribbean islands starting with 'B' go to North America, other Caribbean islands go to South America
- Order by country name in ascending order

**Show the name, the original continent and the new continent of all countries.**

.. code-block:: sql
    :linenos:

     SELECT name,continent,
       CASE WHEN continent = 'Eurasia' OR name='Turkey' THEN 'Europe/Asia'
            WHEN continent IN ('Oceania') THEN 'Australasia'
            WHEN continent = 'Caribbean' AND name LIKE 'B%' THEN 'North America'
            WHEN continent = 'Caribbean' THEN 'South America'
            ELSE continent END
       FROM world
     ORDER BY name


**************
math functions
**************

Aggregate functions (SUM, COUNT, AVG, etc)
==========================================
**Aggregate function** = takes many values and outputs a single-value

.. code-block:: sql
    :linenos:
    
    SELECT SUM(population) FROM world

GROUP BY and HAVING
===================
.. code-block:: sql
    :linenos:

    -- number of countries for each continent
    SELECT continent, COUNT(name)
    FROM world
    GROUP BY(continent)

###############
different RDBMS
###############
To read:

- https://www.digitalocean.com/community/tutorials/understanding-sql-and-nosql-databases-and-different-database-models
- https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems
- https://www.digitalocean.com/community/tutorials/a-comparison-of-nosql-database-management-systems-and-models