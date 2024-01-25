#(a)
#CORRECT~~~
empirical_prob <- sum(P > 10) / length(P)
empirical_prob

#(b)
###NONE CORRECT~~~
?Normal
dnorm(1000, mean(empirical_prob), sd(empirical_prob))

dnorm(10, mean_P, sd_P)

# Recalculate the standard deviation
sd_P_approx <- sqrt(10)

# Calculate the normal approximation probability of more than 10 claims in a day
prob_normal_approx_corrected <- 1 - pnorm(10 - 0.5, mean = 10, sd = sd_P_approx)
prob_normal_approx_corrected


#(c)
##CORRECT###
?Poisson
# Calculate the exact Poisson probability of more than 10 claims in a day
prob_exact_poisson <- 1 - ppois(10, lambda = 10)
prob_exact_poisson