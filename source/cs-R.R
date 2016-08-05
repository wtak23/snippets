# see what data i have
#data()
rm(list=ls())

# === examples based on R by Example by J. Albert
# as well as http://hyperpolyglot.org/numerical-analysis

# conditional statements -----------------------------------------------------------
x <- 5
if (x > 0) {
  print('positive')
} else if (x < 0) {
  print('negative')
} else {
  print('zero')
}

for (i in 1:10) {
  print(i)
}

i=0
while (i < 10) {
  i = i + 1
  
  if (i==3){next} # continue
  if (i==8){break}
  print(i)
}
# 1.1.2 basic operations --------------------------------------------------



temps = c(51.9, 51.8, 51.9, 53)
print(temps)

# play around with data frame ---------------------------------------------
#
df = data.frame(UCBAdmissions)


# 1.2 functions -----------------------------------------------------------

# MLE (biased) estimate of variance
var.n = function(x) {
  v = var(x)
  n = NROW(x)
  v * (n - 1) / n
}

temps = c(51.9, 51.8, 51.9, 53)
var(temps)
var.n(temps)

f = function(x, a=1, b=1)
  x^(a-1) * (1-x)^(b-1)


# 1.3 Vectors and matrices ------------------------------------------------

probs = c(.45, .05, .01, .48, .70, .50, .07, .25, .49)
P = matrix(probs, nrow=3, ncol=3)
length(probs)
dim(probs)
dim(P)
length(P)

P
class(P)
#add row/col names
rownames(P) <- colnames(P) <- c("lower", "middle", "upper")
P
nrow(P)
ncol(P)
# package (1.6) --------------------------------------------------------------------
# note: i commented out the ones that switches the editor
library(bootstrap)
df=law82
names(df) # column names
df$School
cor(df$LSAT,df$GPA)

#stuffs from http://hyperpolyglot.org/numerical-analysis
search() # <- list loaded libraries
.libPaths() # library search path

#library() # <- show what library is installed
#library(help=bootstrap) # <- get help for package
help(package=bootstrap) # <- i like this better in R-studio (won't change tab in edtor)
#data(package="bootstrap") # <- show what data is available in a package

# use `help.search` to search any installed packages
help.search('abcnon')
help.search('lm')

# list the objects in the current workspace
ls()
objects()

a <- 5
b <- c(2,1)
d <- 'hey'

# remove a single variable
rm('d')

# remove multiple variables at once
rm(list=c('a','b'))
