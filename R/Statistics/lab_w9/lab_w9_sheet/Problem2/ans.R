?Binomial
# Random variable X follows binomial distribution with parameters n=12 and p,
# where p is a random variable with Beta distribution with parameters a=2 and
# b=3. Using set.seed(79) and M=10,000 simulations with a for loop calculate the
# empirical mean and variance of X. Compare these to the theoretical mean and
# variance of X.

set.seed(79)

M <- 10000

n <- 12

a <- 2
b <- 3
p_vals <- rbeta(M, a, b)

x <- numeric(M)

for(i in 1:10000){
  p <- p_vals[i]
  x[i] <- rbinom(1, n, p)
}
x
mean(x)
emp_mean <- mean(x)
emp_var <- var(x)

emp_mean
emp_var

theo_mean <- n * (mean(p_vals))
theo_mean

theo_var <- (n * (var(p_vals) * (1 - (var(p_vals)))))^0.5
theo_var
var(p_vals)
