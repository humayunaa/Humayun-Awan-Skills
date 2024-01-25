# Problem 2 Possion mean 10 per day

#(i)
#(a)

set.seed(29)
?Poisson
P <- rpois(1000, 10)

#(b) #(c)
hist(P, breaks = seq(-0.5, max(P) + 0.5, by = 1), prob=TRUE, col="skyblue")

#?Normal
mean_P <- mean(P)
sd_P <- sd(P)
x <- seq(min(P), max(P), length.out = 1000)
# Calculate PDF values for the normal distribution
pdf_normal <- dnorm(x, mean = mean_P, sd = sd_P)

# Superimpose the PDF of the normal distribution
lines(x, pdf_normal, col = "red", lwd = 2)