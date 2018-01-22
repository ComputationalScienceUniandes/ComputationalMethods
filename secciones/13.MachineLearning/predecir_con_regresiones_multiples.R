# Modelos de regresión múltiple

## Referencias: Data Science Specialization, James Leek

### Un modelo relaciona una o varias variables que hay que explicar Y a unas variables explicativas X, por una relación funcional Y = F (X)
### Estos modelos pueden ser postulados (se conoce el fenómeno subyacente) o no-postulados (totalmente regidos por los datos que se miden).

## A continuación, trabajaremos con una predicción con datos de ingresos
### Instalar paquetes
### revisar el archivo ml_packages.R para determinar cuáles paquetes necesita instalar.


library(ggplot2)
library(caret)

## leer los datos
Wage <- read.csv("wages.csv")
summary(Wage)

# definir datos de entrenamiento/test
## generar la partición (2/3 training, 1/3 testing)
training <- Wage[inTrain,]
testing <- Wage[-inTrain,]
dim(training)
dim(testing)


## gráfico de pares con respecto a los salarios
featurePlot(x=training[,c("age","education","jobclass")],
            y = training$wage,
            plot="pairs")

## Grafique el salario en términos de la edad
ggplot(training) + geom_point(aes(age,wage)) + theme_bw()

## Ahora agreguémosle información sobre el tipo de trabajo...
  
ggplot(training) + geom_point(aes(age, wage, color = jobclass)) + theme_bw()

## Agregar información sobre educación...
  
ggplot(training) + geom_point(aes(age, wage, color = education)) + theme_bw()


## Ajustemos un de regresión lineal múltiple!
## $$ ED_i = b_0 + b_1 age + b_2 I(Jobclass_i="Information") + \sum_{k=1}^4 \gamma_k I(education_i= level k) $$

## plantear el modelo usando train de caret
modFit<- train(wage ~ age + jobclass + education, method = "lm",data=training)
## seleccionar el modelo final
finMod <- modFit$finalModel

## imprimir los parámetros del modelo final
print(modFit)

plot(finMod,1,pch=19,cex=0.5,col="#00000010")

## Ahora use los colores con las variables que no se usaron en el modelado
qplot(finMod$fitted,finMod$residuals,colour=race,data=training) + theme_bw()

# graficar sólo los residuos
plot(finMod$residuals,pch=19)


## Ahora llega la hora de la verdad:
## Comparar la predicción en nuestro conjunto de entrenamiento en el dataset de prueba.
pred <- predict(modFit, testing)
# agregar predicción al dataset
predict_test <- testing
predict_test$pred <- pred
# graficar la predicción, colorear por año.
ggplot(predict_test) + geom_point(aes(wage,pred,colour=year))

## Nota: que sucede si se utilizan todas las variables independientes disponibles?


# entrene un modelo con todas las variables independientes
drops <- c("sex","region") # sacar las variables que solo tienen un factor.
modFitAll<- train(wage ~ .,data=training[,!(names(training) %in% drops)],method="lm")

# lleve a cabo la predicción
pred_all <- predict(modFitAll, testing[,!(names(testing) %in% drops)])
qplot(wage,pred_all,data=testing[,!(names(testing) %in% drops)]) + theme_bw()

