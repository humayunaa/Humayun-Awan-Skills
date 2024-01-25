?Geometric
x = 0:10
y = c(dgeom(0, .51),
      dgeom(1, .51),
      dgeom(2, .51),
      dgeom(3, .51),
      dgeom(4, .51),
      dgeom(5, .51),
      dgeom(6, .51),
      dgeom(7, .51),
      dgeom(8, .51),
      dgeom(9, .51),
      dgeom(10, .51))

CDF <- cumsum(y)
# cumsum() = CDF values for each point
# ecdf() = CDF function

length(CDF)

# graph
plot(x, CDF, type = "s", lwd = 2, col = "blue", main = "Stepped Graph",
     xlab = "Number of Daughters", ylab = "CDF")
grid()
