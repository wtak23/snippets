pyspark
"""""""

- http://spark.apache.org/docs/latest/programming-guide.html
- http://spark.apache.org/docs/latest/submitting-applications.html
- https://wtak23.github.io/pyspark_doc/index.html
- https://databricks.com/resources/type/example-notebooks


Good tuorials

- https://s3.amazonaws.com/sparksummit-share/ml-ams-1.0.1/index.html
- `Spark 2016 summit <https://spark-summit.org/2016/>`_


.. contents:: **Table of Contents**
    :depth: 3


###############
Stack overflows
###############
- http://stackoverflow.com/questions/30787635/takeordered-descending-pyspark

.. code-block:: python

    RDD.takeOrdered(5, key = lambda x: x[0])  # sort by keys
    RDD.takeOrdered(5, key = lambda x: -x[0]) # sort by keys (descending)
    RDD.takeOrdered(5, key = lambda x: x[1])  # sort by values
    RDD.takeOrdered(5, key = lambda x: -x[1]) # sort by values (descending)

***********************************************************
numpy array to spark dataframe...trickier than i thought...
***********************************************************
- http://stackoverflow.com/questions/32742004/create-spark-dataframe-can-not-infer-schema-for-type-type-float

This bit me in the ass during edX...

.. code-block:: python

    myFloatRdd = sc.parallelize([1.0,2.0,3.0])
    #df = myFloatRdd.toDF() #<- won't work1 raises a TypeError
    myFloatRdd.map(lambda x: (x, )).toDF().show() # <- need to give in tuple format...
    #+---+
    #| _1|
    #+---+
    #|1.0|
    #|2.0|
    #|3.0|
    #+---+

    # or even better...
    from pyspark.sql import Row
    row = Row("val") # Or some other column name
    myFloatRdd.map(row).toDF().show()
    #+---+
    #|val|
    #+---+
    #|1.0|
    #|2.0|
    #|3.0|
    #+---+


**************************************
Adding new columns to Spark DataFrames
**************************************
- http://stackoverflow.com/questions/33681487/how-do-i-add-a-new-column-to-spark-data-frame-pyspark

You cannot add an arbitrary column to a ``DataFrame`` in Spark.

4 approaches:

1. use ``pyspark.sql.functions.lit``, **literals**

.. code-block:: python

    from pyspark.sql.functions import lit
    df = sqlContext.createDataFrame(
        [(1, "a", 23.0), (3, "B", -23.0)], ("x1", "x2", "x3"))
    df_with_x4 = df.withColumn("x4", lit(0))
    df_with_x4.show()
    ## +---+---+-----+---+
    ## | x1| x2|   x3| x4|
    ## +---+---+-----+---+
    ## |  1|  a| 23.0|  0|
    ## |  3|  B|-23.0|  0|
    ## +---+---+-----+---+

2. transorm an existing column

.. code-block:: python

    from pyspark.sql.functions import exp
    df_with_x5 = df_with_x4.withColumn("x5", exp("x3"))
    df_with_x5.show()
    ## +---+---+-----+---+--------------------+
    ## | x1| x2|   x3| x4|                  x5|
    ## +---+---+-----+---+--------------------+
    ## |  1|  a| 23.0|  0| 9.744803446248903E9|
    ## |  3|  B|-23.0|  0|1.026187963170189...|
    ## +---+---+-----+---+--------------------+

3. use ``.join``

.. code-block:: python

    lookup = sqlContext.createDataFrame([(1, "foo"), (2, "bar")], ("k", "v"))
    df_with_x6 = (df_with_x5
        .join(lookup, col("x1") == col("k"), "leftouter")
        .drop("k")
        .withColumnRenamed("v", "x6"))
    ## +---+---+-----+---+--------------------+----+
    ## | x1| x2|   x3| x4|                  x5|  x6|
    ## +---+---+-----+---+--------------------+----+
    ## |  1|  a| 23.0|  0| 9.744803446248903E9| foo|
    ## |  3|  B|-23.0|  0|1.026187963170189...|null|
    ## +---+---+-----+---+--------------------+----+

4. use udf/function

.. code-block:: python

    from pyspark.sql.functions import rand
    df_with_x7 = df_with_x6.withColumn("x7", rand())
    df_with_x7.show()
    ## +---+---+-----+---+--------------------+----+-------------------+
    ## | x1| x2|   x3| x4|                  x5|  x6|                 x7|
    ## +---+---+-----+---+--------------------+----+-------------------+
    ## |  1|  a| 23.0|  0| 9.744803446248903E9| foo|0.41930610446846617|
    ## |  3|  B|-23.0|  0|1.026187963170189...|null|0.37801881545497873|
    ## +---+---+-----+---+--------------------+----+-------------------+

##############
Handy snippets
##############
https://spark.apache.org/docs/latest/quick-start.html

.. code-block:: python

    # this creates an RDD object
    textFile = sc.textFile("README.md")

    textFile.count() # Number of items in this RDD
    126

    textFile.first() # First item in this RDD
    u'# Apache Spark'

    linesWithSpark = textFile.filter(lambda line: "Spark" in line)
    textFile.filter(lambda line: "Spark" in line).count() # How many lines contain "Spark"?
    15

    # find the line with the most words
    textFile.map(lambda line: len(line.split())).reduce(lambda a, b: a if (a > b) else b)
    15

    # we can also pass a top-level python function (instead of anonymous functions like above)
    def max(a, b):
        if a > b:
            return a
        else:
            return b
    textFile.map(lambda line: len(line.split())).reduce(max)

    #======================================================================#
    # One common data flow pattern is MapReduce, as popularized by Hadoop. 
    # Spark can implement MapReduce flows easily:
    #======================================================================#
    # compute the per-word counts in the file as an RDD of (string, int) pairs
    wordCounts = (textFile
                    .flatMap(lambda line: line.split())
                    .map(lambda word: (word, 1))
                    .reduceByKey(lambda a, b: a+b))

    wordCounts.collect()
    [(u'and', 9), (u'A', 1), (u'webpage', 1), (u'README', 1), (u'Note', 1), (u'"local"', 1), (u'variable', 1), ...]

    # caching can help when you query small "hot" dataset or running iterative
    # alg. like page-rank
    linesWithSpark.cache()
    linesWithSpark.count()
    19
    linesWithSpark.count()
    19

*********************
Todo: run this script
*********************
https://spark.apache.org/docs/latest/quick-start.html#self-contained-applications

.. code-block:: python

    """SimpleApp.py"""
    from pyspark import SparkContext

    logFile = "YOUR_SPARK_HOME/README.md"  # Should be some file on your system
    sc = SparkContext("local", "Simple App")
    logData = sc.textFile(logFile).cache()

    numAs = logData.filter(lambda s: 'a' in s).count()
    numBs = logData.filter(lambda s: 'b' in s).count()

    print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

Submit this script using ``bin/spark-submit`` script 

.. code-block:: bash

    # Use spark-submit to run your application
    $ YOUR_SPARK_HOME/bin/spark-submit --master local[4] SimpleApp.py
    ...
    Lines with a: 46, Lines with b: 23

************************
Bunch of example scripts
************************
https://github.com/apache/spark/tree/master/examples/src/main/python

********************************
Use of persist (RDD persistence)
********************************
- https://spark.apache.org/docs/latest/programming-guide.html#basics
- https://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence

One of the most important capabilities in Spark is persisting (or caching) a 
dataset in memory across operations. When you persist an RDD, each node stores 
any partitions of it that it computes in memory and reuses them in other 
actions on that dataset (or datasets derived from it). This allows future 
actions to be much faster (often by more than 10x). **Caching is a key tool for 
iterative algorithms and fast interactive use**.

You can mark an RDD to be persisted using the ``persist()`` or ``cache()`` methods on it. 

- The first time it is computed in an action, it will be kept in memory on the nodes. 
- Spark's cache is **fault-tolerant** – if any partition of an RDD is lost, 
  it will automatically be recomputed using the transformations that 
  originally created it.


In addition, each persisted RDD can be stored using a different **storage level**, 
allowing you, for example, to persist the dataset on disk, persist it in 
memory but as serialized Java objects (to save space), replicate it across nodes. 

- These levels are set by passing a ``StorageLevel`` object (Scala, Java, Python) to ``persist()``. 
- The ``cache()`` method is a shorthand for using the default storage level, 
  which is ``StorageLevel.MEMORY_ONLY`` (store deserialized objects in memory). 
- The full set of storage levels is 
  (`link <https://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence>`_)

.. code-block:: python

    lines = sc.textFile("data.txt")
    lineLengths = lines.map(lambda s: len(s))
    totalLength = lineLengths.reduce(lambda a, b: a + b)

    # if you want to use lineLengths again later, do this before reduce
    # (saves the data in memory)
    lineLengths.persist()

##############
SQL in pyspark
##############
Using Spark SQL within a Python Notebook

You can use execute SQL commands within a python notebook by invoking %sql or using ``sqlContext.sql(...)``.

.. code-block:: python

    %sql show functions


########################################
Spark SQL, DataFrames and Datasets Guide
########################################

https://spark.apache.org/docs/latest/sql-programming-guide.html


**********
DataFrames
**********
.. code-block:: python

    #======================================================================#
    # create a basic SparkSession using SparkSession.builder
    #======================================================================#
    from pyspark.sql import SparkSession

    # SparkSession in Spark 2.0 provides builtin support for Hive features 
    # including the ability to write queries using HiveQL
    spark = SparkSession\
        .builder\
        .appName("PythonSQL")\
        .config("spark.some.config.option", "some-value")\
        .getOrCreate()

    # spark is an existing SparkSession
    df = spark.read.json("examples/src/main/resources/people.json")
   
    # Displays the content of the DataFrame to stdout
    df.show() 
    ## age  name
    ## null Michael
    ## 30   Andy
    ## 19   Justin

    # Print the schema in a tree format
    df.printSchema()
    ## root
    ## |-- age: long (nullable = true)
    ## |-- name: string (nullable = true)

    # Select only the "name" column
    df.select("name").show()

    # Select everybody, but increment the age by 1
    df.select(df['name'], df['age'] + 1).show()
    ## name    (age + 1)
    ## Michael null
    ## Andy    31
    ## Justin  20

    # Select people older than 21
    df.filter(df['age'] > 21).show()
    ## age name
    ## 30  Andy

    #======================================================================#
    # run SQL Queries programatically
    #======================================================================#
    # spark is an existing SparkSession
    df = spark.sql("SELECT * FROM table")

********************************
Inter-operating RDD & DataFrames
********************************
``Rows`` are constructed from a list of key/value pairs. The key will be 
inferred as the column names of the table.



.. code-block:: python

    # spark is an existing SparkSession.
    from pyspark.sql import Row
    sc = spark.sparkContext

    # Load a text file and convert each line to a Row.
    lines = sc.textFile("examples/src/main/resources/people.txt")
    parts = lines.map(lambda l: l.split(","))
    people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

    #======================================================================#
    # Here, create DF from Row object by inferring scheme
    # (key values will be used as column names)
    #======================================================================#
    # Infer the schema, and register the DataFrame as a table.
    schemaPeople = spark.createDataFrame(people)
    schemaPeople.createOrReplaceTempView("people")

    # SQL can be run over DataFrames that have been registered as a table.
    teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

    # The results of SQL queries are RDDs and support all the normal RDD operations.
    teenNames = teenagers.map(lambda p: "Name: " + p.name)
    for teenName in teenNames.collect():
      print(teenName)

    #======================================================================#
    # Programmatically Specifying the Schema
    #======================================================================#
    from pyspark.sql.types import *

    # The schema is encoded in a string.
    schemaString = "name age"

    fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    schema = StructType(fields)

    # Apply the schema to the RDD.
    schemaPeople = spark.createDataFrame(people, schema)

    # Creates a temporary view using the DataFrame
    schemaPeople.createOrReplaceTempView("people")

    # SQL can be run over DataFrames that have been registered as a table.
    results = spark.sql("SELECT name FROM people")

    # The results of SQL queries are RDDs and support all the normal RDD operations.
    names = results.map(lambda p: "Name: " + p.name)
    for name in names.collect():
      print(name)

####################################
Programming-guide: condensed summary
####################################
From http://spark.apache.org/docs/latest/programming-guide.html

************
Super basics
************


- use the ``bin/spark-submit`` script in the Spark directory to run Spark applications in Python

.. code-block:: bash

    $ PYSPARK_PYTHON=python3.4 bin/pyspark
    $ PYSPARK_PYTHON=/opt/pypy-2.5/bin/pypy bin/spark-submit examples/src/main/python/pi.py



.. code-block:: python

    from pyspark import SparkContext, SparkConf

    #=========================================================================#
    # 1st thing a Spark program must do: create SC object that tells Spark how to access a cluster
    #=========================================================================#
    # create config object (contains information about your application)
    # - `appName` = name of the application to show on the cluster UI
    # - `master` = "local", or URL to Spark, Mesos, or YARN cluster.
    #   (http://spark.apache.org/docs/latest/submitting-applications.html#master-urls)
    conf = SparkConf().setAppName(appName).setMaster(master)

    # create SparkContext object
    sc = SparkContext(conf=conf)

    # === create RDD from an existing collection/iterable ===
    # - use sc.parallelize
    data = [1, 2, 3, 4, 5]
    distData = sc.parallelize(data) # create Parallelized collections
    distData.reduce(lambda a, b: a + b)

    # partitions (typically 2-4 partitions for each CPU in cluster
    distData = sc.parallelize(data,partitions=10) # can also specify 
    wordsRDD = sc.parallelize(["fish", "cats", "dogs"])
    

    # === RDD external dataset ===
    # - use sc.textFile 
    # URI = either a local path on the machine, or a hdfs://, s3n://, etc URI
    distFile = sc.textFile("data.txt")
    distFile.map(lambda s: len(s)).reduce(lambda a, b: a + b)

    # All of Spark’s file-based input methods, including textFile, 
    # support running on directories, compressed files, and wildcards
    sc.textFile("/my/directory")
    sc.textFile("/my/directory/*.txt")
    sc.textFile("/my/directory/*.gz")


    #==========================================================================#
    # saving and loading
    #==========================================================================#
    # Similarly to text files, SequenceFiles can be saved and loaded by specifying the path
    >>> rdd = sc.parallelize(range(1, 4)).map(lambda x: (x, "a" * x ))
    >>> rdd.saveAsSequenceFile("path/to/file")
    >>> sorted(sc.sequenceFile("path/to/file").collect())
    [(1, u'a'), (2, u'aa'), (3, u'aaa')]

****************
Shared variables
****************
- General, read-write shared variables across tasks would be inefficient. 
- However, Spark does provide two limited types of shared variables for two \
  common usage patterns: broadcast variables and accumulators.


Broadast variables
==================
- ``SparkContext.broadcast(v)`` - creates Broadcast variables from variable v. 

  - The broadcast variable is a wrapper around v, and its value can be accessed by 
    calling the ``.value`` method
- Broadcast variables are used to keep a read-only variable cached on each machine 
  (rather than shipping a copy of it with tasks). 

  - example usage: to give every node a copy of a large input dataset in an efficient manner. 
- explicitly creating broadcast variables is only useful when tasks across multiple 
  stages need the same data or when caching the data in deserialized form is important.

.. code-block:: python

    >>> broadcastVar = sc.broadcast([1, 2, 3])
    <pyspark.broadcast.Broadcast object at 0x102789f10>

    >>> broadcastVar.value
    [1, 2, 3]

Accumulators
============
See http://spark.apache.org/docs/latest/programming-guide.html#accumulators

**************
RDD operations
**************

RDD-basics
==========

.. code-block:: python

    lines = sc.textFile("data.txt")
    lineLengths = lines.map(lambda s: len(s))
    totalLength = lineLengths.reduce(lambda a, b: a + b)
    lineLengths.persist() # if you want to use this object again later

Passing functions to Spark
==========================
Spark relies heavily on passing functions in the driver program to run on the cluster. 

3 recommended ways to do this:

1. lambda expressions for simple functions (does not support mult-statement \
functions or statements that do not return a value)
2. Local ``def`` functions
3. Top-level functions in a module

.. code-block:: python

    def myFunc(s):
        words = s.split(" ")
        return len(words)

    sc.textFile("file.txt").map(myFunc)

Some caveats when defining class attributes

.. code-block:: python

    # don't do this (the whole object gets sent to the luster when ``doStuff`` is called)
    class MyClass(object):
        def func(self, s):
            return s
        def doStuff(self, rdd):
            return rdd.map(self.func)

    # or this (accessing fields of the outer object will reference the ENTIRE object)
    class MyClass(object):
        def __init__(self):
            self.field = "Hello"
        def doStuff(self, rdd):
            return rdd.map(lambda s: self.field + s)

    # rather, do this (copy field into a local variable instead of accessing it externally)
    def doStuff(self, rdd):
        field = self.field
        return rdd.map(lambda s: field + s)


RDD Transformations
===================
http://spark.apache.org/docs/latest/programming-guide.html#transformations

RDD Actions
===========
http://spark.apache.org/docs/latest/programming-guide.html#actions

closures
========
Common confusion in Spark:

- understanding the **scope** and **life cycle** of variables and methods when
  executing code across a cluster.
- In general, **closures** - constructs like loops or locally defined methods, 
  should not be used to mutate some global state. 
- Use an **Accumulator** instead if some global aggregation is needed.

Example: wrong way to increment a counter

.. code-block:: python

    counter = 0
    rdd = sc.parallelize(data)

    # Wrong: Don't do this!! (will only work in master="local" mode, but won't work on cluster)
    def increment_counter(x):
        global counter
        counter += x
    rdd.foreach(increment_counter)

    print("Counter value: ", counter)

Working with key-value pairs
============================
.. code-block:: python

    lines = sc.textFile("data.txt")
    pairs = lines.map(lambda s: (s, 1))
    counts = pairs.reduceByKey(lambda a, b: a + b)
    counts.sortByKey() # sort alphabetically
    counts.collect() # bring them back to the driver program as a list of objects

#####################
Random handy snippets
#####################

****************
compute average
****************
.. code-block:: python
    
    # using RDDs
    rdd = sc.textFile(...).map(_.split(" "))
    rdd.map { x => (x(0), (x(1).toFloat, 1)) }.
    reduceByKey { case ((num1, count1), (num2, count2)) =>
    (num1 + num2, count1 + count2)
    }.
    map { case (key, (num, count)) => (key, num / count) }.
    collect()

    # using DF
    import org.apache.spark.sql.functions._
    val df = rdd.map(a => (a(0), a(1))).toDF("key", "value")
    df.groupBy("key")
    .agg(avg("value"))
    .collect()


