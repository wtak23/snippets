R (``cs-R.rst``)
""""""""""""""""
.. contents:: `Table of contents`
   :depth: 2
   :local:

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