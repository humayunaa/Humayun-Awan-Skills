?Chisquare
?replicate

#(a) #(b)
set.seed(19)

rchisq(data, df=5)
estimate_2 <- rep(0, 1000)

for (i in 1:1000) {
  y <- rchisq(data, df = 4.5)  # Generating chi-squared samples
  estimate_2[i] <- mean(y)  # Calculating the mean of each sample
}

hist(estimate_2, prob=TRUE, breaks = 20)

#(c)
lines(density(estimate_2), col="blue", lwd=2)

#(d)
empirical_estimate2 <- estimate_2/length(estimate_2)
mean(empirical_estimate2)
sd(empirical_estimate2)