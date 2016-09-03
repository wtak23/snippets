sql (``cs-sql.rst``)
""""""""""""""""""""

.. contents:: `Table of contents`
   :depth: 2
   :local:

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