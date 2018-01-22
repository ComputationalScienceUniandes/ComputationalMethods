#### Simple KNN Machine Learning in R #### 

# you're going to need the following packages:
# ggplot2, devtools, dplyr, ggvis, dplyr
# if you don't have them, you'll need to install the following packages:
# install.packages('devtools')
# install_github('hadley/ggplot2')
# install_github('hadley/dplyr')
# install_github('hadley/ggvis')

library(ggvis)
library(dplyr)
library(class) # to do classification
library(gmodels)


## STEP1: Read data!
# read data
iris <- read.csv(url("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"), header = FALSE) 
# pretty names
names(iris) <- c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species")


## STEP2: Observe your data
# Graphically: Plot it

# plot points: sepal length vs width
iris %>% ggvis(~Sepal.Length, ~Sepal.Width, fill = ~Species) %>% layer_points()
# plot points: petal length vs width
iris %>% ggvis(~Petal.Length, ~Petal.Width, fill = ~Species) %>% layer_points()

# other ways to explore the dataset
glimpse(iris)
table(iris$Species) #n species
round(prop.table(table(iris$Species)) * 100, digits = 1) #% species
summary(iris) 
summary(iris[c("Petal.Width", "Sepal.Width")])

## STEP3: Prepare Data

#knn algorithm works better with normalized data. Two types:
  # - example normalization: each item individually normalized
  # - feature normalization: each feature is adjusted in the same way across all sample.

# Create a normalization function:

normalize_me <- function(x) {
  num <- x - min(x)
  denom <- max(x) - min(x)
  return (num/denom)
}

# apply the normalization only to numerical attributes
normalized_iris <- as.data.frame(lapply(iris[1:4], normalize_me))
summary(normalized_iris)


#STEP4: Training vs Test Sets
# Usually, it's split (2/3,1/3).
# but you need to be careful in order to include all diversity in the data. Otherwise you'll end up
# classifying less things!

set.seed(1234)
ind <- sample(2, nrow(iris), replace=TRUE, prob=c(2/3, 1/3))

# now use this to define the training/test datasets
iris.training <- iris[ind==1, 1:4]
iris.test <- iris[ind==2, 1:4]

# store the labels independently, so that you can get a decent prediction
iris.trainLabels <- iris[ind==1, 5]
iris.testLabels <- iris[ind==2, 5]

#STEP5: KNN Model
# Run KNN for the training/test sets
iris_pred <- knn(train = iris.training, test = iris.test, cl = iris.trainLabels, k=3)


#STEP6: Measure Performance
#visual inspection
cbind(iris_pred,iris.testLabels)

# using gmodels
CrossTable(x = iris.testLabels, y = iris_pred, prop.chisq=FALSE)

