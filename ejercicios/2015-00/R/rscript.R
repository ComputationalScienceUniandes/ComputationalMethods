# Load packages
library(ggplot2)

# Mi primer script de R
x <- 7+677
plot(x)

str(movies)

ggplot(movies) + geom_point(aes(x = votes,
                                y = rating, color = mpaa)) + facet_wrap(~mpaa)

ggplot(movies) + geom_density(aes(x = rating, color = mpaa)) + facet_grid(mpaa~.)

plot(rnorm(200))

xx <- data.frame(x = rnorm(500))

ggplot(xx) + geom_density(aes(xx))





