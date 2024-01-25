?FDist
set.seed(59)
S <- rf(500, 2, 7)

# Calculate proportion of simulated values greater than 1.5
#(a)
empirical_prob <- sum(S > 1.5) / length(S)
empirical_prob

#(b)
# Calculate the x value for which P(F_{2, 7} < x) = 0.38
quantile_value <- quantile(S, 0.38)
quantile_value

##DONE CORRECT##