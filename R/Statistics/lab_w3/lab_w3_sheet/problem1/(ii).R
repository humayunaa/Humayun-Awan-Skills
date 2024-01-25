num_daughters_prob = c(dgeom(0, .51),
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

num_daughters_prob
num_daughters = c(0:10)
num_daughters

barplot(num_daughters_prob, names.arg = num_daughters,
        xlab = "Number of Daughters",
        ylab = "Probability",
        main = "Daughters before 1st Son",
        col = "blue")
