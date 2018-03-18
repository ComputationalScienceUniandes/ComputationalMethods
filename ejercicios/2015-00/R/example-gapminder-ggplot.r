## Example taken from JennyBc ggplot2 tutorial:
## https://github.com/jennybc/ggplot2-tutorial/

#+ setup, include = FALSE
library(knitr) ## si no está install.packages('knitr')

library(ggplot2)
library(RColorBrewer)

#' load data
gdURL <- "http://tiny.cc/gapminder"
gDat <- read.delim(file = gdURL) 
str(gDat)

#' let just look at four countries
jCountries <- c("Canada", "Rwanda", "Cambodia", "Mexico", "Colombia")
x <- droplevels(subset(gDat, country %in% jCountries))
ggplot(x, aes(x = year, y = lifeExp, color = country)) +
  geom_line() + geom_point()

#' reorder the country factor to reflect lifeExp in 2007
x <- transform(x, country = reorder(country, -1 * lifeExp, max))
ggplot(x, aes(x = year, y = lifeExp, color = country)) +
  geom_line() + geom_point()

