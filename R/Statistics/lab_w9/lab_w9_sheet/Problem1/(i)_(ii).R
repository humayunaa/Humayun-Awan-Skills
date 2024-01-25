# Problem 1
# sample:


data <- c(4.8, 7.6, 1.2, 3.5, 2.9, 0.8, 0.5, 2.3)

sample(data, replace=TRUE)

set.seed(19)
estimate <- rep(0, 1000)
for(i in 1:1000){
  x <- sample(data, replace=TRUE)   #will be different every time #ignore exp(l)
  estimate[i] <- mean(x)
}

hist(estimate)
estimate_density <- density(estimate)
#lines(estimate_density, col="red")

mean(estimate_density)
estimate_density


empirical_estimate <- estimate/length(estimate)
empirical_estimate
lines(empirical_estimate, col="blue")
mean(empirical_estimate)
sd(empirical_estimate)

##answers are very close. same number just instead of 2 it is 0.002 for mean