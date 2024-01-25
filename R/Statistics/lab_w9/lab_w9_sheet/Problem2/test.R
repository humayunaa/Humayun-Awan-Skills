# Set seed for reproducibility
set.seed(79)

# Number of simulations
M <- 10000

# Parameters for the Beta distribution
a <- 2
b <- 3

# Number of trials for the binomial distribution
n <- 12

# Generate random values for p from Beta distribution
p_values <- rbeta(M, a, b)

# Initialize vectors to store simulated values of X
X_values <- numeric(M)

# Simulate X for each value of p using a for loop
for (i in 1:M) {
  p <- p_values[i]
  X_values[i] <- rbinom(1, n, p)
}

X_values
mean(X_values)
# Calculate empirical mean and variance of X
empirical_mean <- mean(X_values)
empirical_variance <- var(X_values)
empirical_mean

# Calculate theoretical mean and variance of X
theoretical_mean <- n * (a / (a + b))
theoretical_variance <- n * (a * b) / ((a + b)^2 * (a + b + 1))

# Display results
cat("Empirical Mean of X:", empirical_mean, "\n")
cat("Empirical Variance of X:", empirical_variance, "\n")
cat("Theoretical Mean of X:", theoretical_mean, "\n")
cat("Theoretical Variance of X:", theoretical_variance, "\n")
