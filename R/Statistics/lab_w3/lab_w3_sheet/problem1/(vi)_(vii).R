#ensure same random
set.seed(47)

G <- rgeom(1000, 0.49)

counts <- table(G)
counts
empirical_probs <- counts / length(G)
empirical_probs

iii_a
iii_b
iii_c

counts1 <- c(iii_a, iii_b, iii_c)
counts1
counts1_table <- table(counts)
counts1_table

emp2 <- counts1_table / length(G)
emp2
