# Find 95th Percentile
#(a) normal distribution mean=100, var=50
?Normal
sd = 50^0.5
qnorm(.95, 100, sd)

#(b)
?Uniform
qunif(.95, 90, 170)