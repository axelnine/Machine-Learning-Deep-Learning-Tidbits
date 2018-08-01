library(pander)
library(ggplot2)
library(reshape2)
library(mlbench)
library(caret)
library(randomForest)
mydata <- read.csv("C:/Users/iGuest/Desktop/Project/hrdataset.csv", header=TRUE)
drops <- c("salary")
mydata[ , !(names(mydata) %in% drops)]
print(mydata)
pander(head(mydata, 5), style = "rmarkdown", split.tables = 120)
cormat <- cor(mydata)
head(cormat)

melted_cormat <- melt(cormat)
head(melted_cormat)
ggplot(data = melted_cormat, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile()

emp_population_satisfaction <-mean(mydata$satisfaction_level)
left_pop<-subset(mydata,left==1)

emp_turnover_satisfaction <-mean(left_pop$satisfaction_level)
print( c('The mean for the employee population is: ', emp_population_satisfaction) )
print( c('The mean for the employees that had a turnover is: ' ,emp_turnover_satisfaction) )

t.test(left_pop$satisfaction_level,mu=emp_population_satisfaction) # Employee Population satisfaction mean
dof<-sum(as.numeric(mydata$left))
LQ <-qt(0.025,dof)  # Left Quartile
RQ <-qt(0.975,dof)  # Right Quartile
print (c('The t-distribution left quartile range is: ',LQ))
print (c('The t-distribution right quartile range is: ' ,RQ))

par(mfrow=c(1,3))
hist(mydata$satisfaction_level, col="green")
#hist(data_set$last_evaluation, col="red")
#hist(data_set$average_montly_hours, col="blue")

control <- rfeControl(functions=rfFuncs, method="cv", number=10)

results <- rfe(mydata[,1:8], mydata[,9], sizes=c(1:8), rfeControl=control)
