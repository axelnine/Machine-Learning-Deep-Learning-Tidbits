data.train = read.csv("C:\\Users\\Prem Shah\\Documents\\University of Washington\\Quarter 4\\MKTG 562\\Project\\data\\train_data.csv")
data.test = read.csv("C:\\Users\\Prem Shah\\Documents\\University of Washington\\Quarter 4\\MKTG 562\\Project\\data\\test_data.csv")

mdata.train = read.csv("C:\\Users\\Prem Shah\\Documents\\University of Washington\\Quarter 4\\MKTG 562\\Project\\data\\modified_train_data.csv")
mdata.test = read.csv("C:\\Users\\Prem Shah\\Documents\\University of Washington\\Quarter 4\\MKTG 562\\Project\\data\\modified_test_data.csv")
drops <- c("X","duration")
x_train<-data.train[ , !(names(data.train) %in% drops)]
x_test<- data.test[ , !(names(data.test) %in% drops)]
y_train <-data.train[,"y"]
y_test <- data.test[,"y"]
mod1 <-glm(y~.,data=x_train, family="binomial")
summary(mod1)

pred = predict(mod1, newdata=mdata.test)


ctrl = rpart.control(maxdepth=6)                        
tree.model <- rpart(y ~ ., method="class", data= x_train, control=rpart.control(minsplit=230, minbucket=95, cp=0.001))

# Display the results 
printcp(tree.model)
# Visualize cross-validation results 
plotcp(tree.model) 
# Detailed summary of splits
summary(tree.model) 
# Plot tree 

rpart.plot(tree.model)

plot(tree.model,uniform=TRUE,main="Classification Tree for Churn Data")
text(tree.model,use.n=TRUE, all=TRUE, cex=.8)
# Predicted Probabilities
tree.prediction.probs <- predict(tree.model,y_train,type = c("prob"),data= data.test)
# Predicted Class (Churn vs. non-churn)
tree.prediction.class <- predict(tree.model,x_test,type = c("class"),data= data.test)

library(gmodels)
CrossTable(tree.prediction.class,y_test,prop.r=FALSE, prop.c=FALSE,prop.t=FALSE,
           prop.chisq=FALSE,dnn = c("Predict", "Actual"))

tree_roc <- tree.model %>%
  predict(newdata = x_test) %>%
  prediction(y_test) %>%
  performance("tpr", "fpr")


data.train$y <- as.factor(data.train$y)

rf.model <- randomForest(y ~ ., data= data.train, ntree=250)

# Display the results 
plot(tree.model, main="Error - Random Forest")
# Predicted Probabilities
rf.prediction.props <- predict(rf.model,data.test,type = c("class"), predict.all=FALSE)

# Predicted Class (Churn vs. non-churn)
rf.prediction.class <- predict(rf.model,mdata.test,type = c("class"), predict.all=FALSE)
summary(rf.model ) 
conf.matrix<-CrossTable(rf.prediction.class,mdata.test$y,prop.r=FALSE, prop.c=FALSE,prop.t=FALSE,
           prop.chisq=FALSE,dnn = c("Predict", "Actual"))

