R (``cs-R.rst``)
""""""""""""""""
.. contents:: `Table of contents`
   :depth: 2
   :local:

.. code-block:: bash

    sudo apt-get install r-base-dev

#####################################
Bunch of quick refresher I find handy
#####################################
************
Getting help
************
http://www.statmethods.net/interface/help.html

.. code-block:: R

    help.start()   # general help
    help(foo)      # help about function foo
    ?foo           # same thing
    apropos("foo") # list all functions containing string foo
    example(foo)   # show an example of function foo

    # search for foo in help manuals and archived mailing lists
    RSiteSearch("foo")

    # get vignettes on using installed packages
    vignette()      # show available vingettes
    vignette("foo") # show specific vignette 

    # show available datasets
    data()
    help(datasetname)

*********
Path info
*********
.. code-block:: R

    getwd()
    setwd(...)

    # Extract System and User Information
    # https://stat.ethz.ch/R-manual/R-devel/library/base/html/Sys.info.html
    Sys.info()

    R.home() # "/usr/lib/R"

    .libPaths() # get library location
    library()   # see all packages installed
    search()    # see packages currently loaded

    > .libPaths()
    [1] "/home/takanori/R/x86_64-pc-linux-gnu-library/3.3"
    [2] "/usr/local/lib/R/site-library"                   
    [3] "/usr/lib/R/site-library"                         
    [4] "/usr/lib/R/library"     

    # very useful help
    ?Startup

*****************
Customize startup
*****************
http://www.statmethods.net/interface/customizing.html

.. code-block:: R

    INSERT-CODE

*************
Get data info
*************
http://www.statmethods.net/input/contents.html

.. code-block:: R

    # list objects in the working environment
    ls()

    # list the variables in mydata
    names(mydata)

    # list the structure of mydata
    str(mydata)

    # list levels of factor v1 in mydata
    levels(mydata$v1)

    # dimensions of an object
    dim(object)

    # class of an object (numeric, matrix, data frame, etc)
    class(object)

    # print mydata
    mydata <- read.csv("http://datasets.flowingdata.com/ppg2008.csv")
    mydata

    # print first 10 rows of mydata
    head(mydata, n=10)

    # print last 5 rows of mydata
    tail(mydata, n=5) 

    # slicing
    mydata[2:5,,]
    mydata
    mydata[c(1,5),,]

******************
Datatypes - quickR
******************
http://www.statmethods.net/input/datatypes.html

.. code-block:: R

    # --- vectors --- #
    a <- c(1,2,5.3,6,-2,4) # numeric vector
    b <- c("one","two","three") # character vector
    c <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE) #logical vector

    # Refer to elements of a vector using subscripts.
    a[c(2,4)] # 2nd and 4th elements of vector

    # --- matrices ---#
    # generates 5 x 4 numeric matrix
    y<-matrix(1:20, nrow=5,ncol=4)

    # another example
    cells <- c(1,26,24,68)
    rnames <- c("R1", "R2")
    cnames <- c("C1", "C2")
    mymatrix <- matrix(cells, nrow=2, ncol=2, byrow=TRUE,
      dimnames=list(rnames, cnames)) 

    x[,4] # 4th column of matrix
    x[3,] # 3rd row of matrix
    x[2:4,1:3] # rows 2,3,4 of columns 1,2,3 

    # --- dataframes --- #
    d <- c(1,2,3,4)
    e <- c("red", "white", "red", NA)
    f <- c(TRUE,TRUE,TRUE,FALSE)
    mydata <- data.frame(d,e,f)
    names(mydata) <- c("ID","Color","Passed") # variable names 

    myframe[3:5] # columns 3,4,5 of data frame
    myframe[c("ID","Age")] # columns ID and Age from data frame
    myframe$X1 # variable x1 in the data frame 

    # --- lists ---
    # example of a list with 4 components -
    # a string, a numeric vector, a matrix, and a scaler
    w <- list(name="Fred", mynumbers=a, mymatrix=y, age=5.3)

    # example of a list containing two lists
    v <- c(list1,list2) 

    mylist[[2]] # 2nd component of the list
    mylist[["mynumbers"]] # component named mynumbers in list

    # --- factors ---
    # variable gender with 20 "male" entries and
    # 30 "female" entries
    gender <- c(rep("male",20), rep("female", 30))
    gender <- factor(gender)
    # stores gender as 20 1s and 30 2s and associates
    # 1=female, 2=male internally (alphabetically)
    # R now treats gender as a nominal variable
    summary(gender) 

    # --- ordered (ordinal variables) --- 
    # variable rating coded as "large", "medium", "small'
    rating <- ordered(rating)
    # recodes rating to 1,2,3 and associates
    # 1=large, 2=medium, 3=small internally
    # R now treats rating as ordinal 

    # --- useful functions ---
    length(object) # number of elements or components
    str(object)    # structure of an object
    class(object)  # class or type of an object
    names(object)  # names

    c(object,object,...)       # combine objects into a vector
    cbind(object, object, ...) # combine objects as columns
    rbind(object, object, ...) # combine objects as rows

    object     # prints the object

    ls()       # list current objects
    rm(object) # delete an object

    newobject <- edit(object) # edit copy and save as newobject
    fix(object)               # edit in place 

*********************
Basic data structures
*********************
This provides a short overview of basic R datastructures

http://www.programcreek.com/2014/01/vector-array-list-and-data-frame-in-r/

.. code-block:: R

    # naming vector
    > vec <- c('linux','november','takanori')
    > names(vec) <- c('os','month','user')
    > vec
            os      month       user 
       "linux" "november" "takanori" 
    > is.vector(vec)
    [1] TRUE
    > is.list(vec)
    [1] FALSE
    > is.data.frame(vec)
    [1] FALSE

    # --- list can contain heterogenous datatypes ---
    > y <- list(name="Mike", gender="M", company="ProgramCreek")
    > y
    $name
    [1] "Mike"

    $gender
    [1] "M"

    $company
    [1] "ProgramCreek"

    # --- dataframes ---#
    > name <- c("Mike", "Lucy", "John") 
    > age <- c(20, 25, 30) 
    > student <- c(TRUE, FALSE, TRUE) 
    > df = data.frame(name, age, student)  
    > df
      name age student
    1 Mike  20    TRUE
    2 Lucy  25   FALSE
    3 John  30    TRUE

***
NAs
***
http://www.statmethods.net/input/missingdata.html

.. code-block:: R

    is.na(x) # returns TRUE of x is missing
    y <- c(1,2,3,NA)
    is.na(y) # returns a vector (F F F T) 

    # recode 99 to missing for variable v1
    # select rows where v1 is 99 and recode column v1
    mydata$v1[mydata$v1==99] <- NA 

    # --- exlucde missing values from analyses ---
    x <- c(1,2,NA,3)
    mean(x) # returns NA
    mean(x, na.rm=TRUE) # returns 2 


    # The function complete.cases() returns a logical vector indicating which cases are complete.
    # list rows of data that have missing values
    mydata[!complete.cases(mydata),]

    # The function na.omit() returns the object with listwise deletion of missing values.
    # create new dataset without missing data
    newdata <- na.omit(mydata) 


##################
Installed packages
##################
.. code-block:: R

    install.packages("R.matlab")

    # to get ``melt``
    # https://www.r-bloggers.com/melt/
    install.packages("reshape2")

    #ftp://cran.r-project.org/pub/R/web/packages/tidyr/vignettes/tidy-data.html
    #https://www.r-bloggers.com/how-to-reshape-data-in-r-tidyr-vs-reshape2/
    #https://blog.rstudio.org/2014/07/22/introducing-tidyr/
    install.packages('tidyr')

    #https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html
    #https://www.r-bloggers.com/data-manipulation-with-dplyr/
    install.packages('dplyr')

#####################################################
Make sure gcc, g++, and gfortran are the same version
#####################################################
Argh, couldn't install some critical bioconductor packages because my gfortran version didn't agree with gcc and g++....killed so much time on this... 10-04-2016 (19:25)

################
Random Overflows
################
********************
locate rprofile path
********************
http://stackoverflow.com/questions/13735745/locate-the-rprofile-file-generating-default-options

.. code-block:: R

    ?Startup

    candidates <- c( Sys.getenv("R_PROFILE"),
                     file.path(Sys.getenv("R_HOME"), "etc", "Rprofile.site"),
                     Sys.getenv("R_PROFILE_USER"),
                     file.path(getwd(), ".Rprofile") )

    Filter(file.exists, candidates)
    [1] "/usr/lib/R/etc/Rprofile.site"
    
*******
Figures
*******
.. code-block:: R

    plot(1:1)
    dev.new()
    plot(2,2)
    dev.set(dev.prev()) # go back to first
    title(main="test dev 1")

    dev.set(dev.next()) # go to second
    title(main="test dev 2")

http://stackoverflow.com/questions/6916129/how-to-get-two-windows-with-different-plots

******************
Packages installed
******************
.. code-block:: R

    # where your package are installed. 
    .libPaths() 

###################
Snippets in RStudio
###################
https://support.rstudio.com/hc/en-us/articles/204463668-Code-Snippets


.. code-block:: bash

    subl ~/.R/snippets/r.snippets


*********************************
Current content in ``r.snippets``
*********************************
.. code-block:: R
    :linenos:

    snippet rem
        rm(list = ls())

    snippet rm
        rm(list = ls())
        
    snippet lib
        library(${1:package})

    snippet req
        require(${1:package})

    snippet src
        source("${1:file.R}")

    snippet ret
        return(${1:code})

    snippet mat
        matrix(${1:data}, nrow = ${2:rows}, ncol = ${3:cols})

    snippet sg
        setGeneric("${1:generic}", function(${2:x, ...}) {
            standardGeneric("${1:generic}")
        })

    snippet sm
        setMethod("${1:generic}", ${2:class}, function(${2:x, ...}) {
            ${0}
        })

    snippet sc
        setClass("${1:Class}", slots = c(${2:name = "type"}))

    snippet if
        if (${1:condition}) {
            ${0}
        }

    snippet el
        else {
            ${0}
        }

    snippet ei
        else if (${1:condition}) {
            ${0}
        }

    snippet fun
        ${1:name} <- function(${2:variables}) {
            ${0}
        }

    snippet for
        for (${1:variable} in ${2:vector}) {
            ${0}
        }

    snippet while
        while (${1:condition}) {
            ${0}
        }

    snippet switch
        switch (${1:object},
            ${2:case} = ${3:action}
        )

    snippet apply
        apply(${1:array}, ${2:margin}, ${3:...})

    snippet lapply
        lapply(${1:list}, ${2:function})

    snippet sapply
        sapply(${1:list}, ${2:function})

    snippet mapply
        mapply(${1:function}, ${2:...})

    snippet tapply
        tapply(${1:vector}, ${2:index}, ${3:function})

    snippet vapply
        vapply(${1:list}, ${2:function}, FUN.VALUE = ${3:type}, ${4:...})

    snippet rapply
        rapply(${1:list}, ${2:function})

    snippet ts
        `r paste("#", date(), "------------------------------\n")`




########################################
TODO: break these down to smaller pieces
########################################

.. literalinclude:: cs-R.R
   :language: R
   :emphasize-lines: 12,15-18
   :linenos: