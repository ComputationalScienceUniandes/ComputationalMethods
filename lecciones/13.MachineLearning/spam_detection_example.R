# load data
# install.packages("kernlab")
# install.packages("devtools")
# install_github("hadley/ggplot2")
library(kernlab); data(spam); set.seed(333)
# picking a small subset (10 values) from spam data set
smallSpam <- spam[sample(dim(spam)[1],size=10),]
# label spam = 2 and ham = 1
spamLabel <- (smallSpam$type=="spam")*1 + 1
# plot the capitalAve values for the dataset with colors differentiated by spam/ham (2 vs 1)
plot(smallSpam$capitalAve,col=spamLabel)

# first rule (over-fitting to capture all variation)
rule1 <- function(x){
  prediction <- rep(NA,length(x))
  prediction[x > 2.7] <- "spam"
  prediction[x < 2.40] <- "nonspam"
  prediction[(x >= 2.40 & x <= 2.45)] <- "spam"
  prediction[(x > 2.45 & x <= 2.70)] <- "nonspam"
  return(prediction)
}
# tabulate results of prediction algorithm 1 (in sample error --> no error in this case)
table(rule1(smallSpam$capitalAve),smallSpam$type)

# second rule (simple, setting a threshold)
rule2 <- function(x){
  prediction <- rep(NA,length(x))
  prediction[x > 2.8] <- "spam"
  prediction[x <= 2.8] <- "nonspam"
  return(prediction)
}
# tabulate results of prediction algorithm 2(in sample error --> 10% in this case)
table(rule2(smallSpam$capitalAve),smallSpam$type)

# tabulate out of sample error for algorithm 1
table(rule1(spam$capitalAve),spam$type)

# tabulate out of sample error for algorithm 2
table(rule2(spam$capitalAve),spam$type)

# accuracy and total correct for algorithm 1 and 2
rbind("Rule 1" = c(Accuracy = mean(rule1(spam$capitalAve)==spam$type),
                   "Total Correct" = sum(rule1(spam$capitalAve)==spam$type)),
      "Rule 2" = c(Accuracy = mean(rule2(spam$capitalAve)==spam$type),
                   "Total Correct" = sum(rule2(spam$capitalAve)==spam$type)))
