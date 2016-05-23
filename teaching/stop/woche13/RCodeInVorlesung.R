# Furby 
# Vor Aufgabe b)
require("expm")
Q <- matrix(c(-2,2,0, 2,-4,2, 0,2,-2), nrow=3, byrow=TRUE)
expm(Q*0.5)
expm(Q*100)

# Furby vor c)
(res = eigen(t(Q)))
v = res$vectors[,1]
v / sum(v)




# Kosten
Q <- matrix(c(-1/20,1/20,1/2,-1/2), nrow=2, byrow=T)
expm(Q*5)
require(expm)
integrate(Vectorize(function(t) {expm(Q*t)[1,2]}), lower=0, upper=50)

