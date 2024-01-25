#plot, lines, labelled graph, PDF, following
# x - (-3.5, 3.5)

#(a)
x <- -3.5:3.5
?TDist
PDFt5 <- dt(x, 5)
plot(x, PDF, type="l", col="blue", lwd=2)

#(b)
PDFt10 <- dt(x, 10)
lines(x, PDFt10, col="red", lwd=2)

#(c)
?NegBinomial
sd_N01 <- 1^0.5
PDF_N01 <- dnorm(x, 0, sd_N01)
lines(x, PDF_N01, col="orange", lwd=2)