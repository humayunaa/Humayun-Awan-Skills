# Count occurrences of daughters before the first son
counts <- table(G)

# Calculate empirical probabilities
empirical_probs <- counts / length(G)

# Display empirical probabilities and compare with specified values
specified_probs <- c(0.9717525, 0.117649, 0.2499)  # Values from part (iii)

# Compare empirical probabilities with specified values
comparison <- data.frame(
  Specified_Probabilities = specified_probs,
  Empirical_Probabilities = empirical_probs
)

comparison
