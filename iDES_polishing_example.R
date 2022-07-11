# model calculation for NuMRD 181 C to T using UMIdb
# retain the site as afZ > zscore
stdAF <- 0.00859858776477881
meanAF <- 0.0051966133884213
af <- 100*2/2669
afZ <- (af - meanAF)/stdAF
countbg <- 74
z <- 0.05/countbg
zscore <- qnorm(1 - (z))


# model calculation for NuMRD 181 C to T using read-level database
# remove the site as wp > wpval
# Bonferroni correction seems too strict here with a large number of substitutions in the read-level db.
# x 用100*af一个原因是在建数据库，计算shape和scale参数时就用的100*全阴样本中的af，可以让拟合结果更好看
af <- 100 * 2 / 2669
x <- 100 * af
shape <- 2.329148
scale <- 11.23801
frac <- 0.928571428571429
p1 <- pweibull(x,shape,scale,TRUE)
wp <- 1-((1 - frac) + (frac * p1))
countbg <- 9179
wpval <- 0.05/countbg

# model calculation for NuMRD_214 T to C using UMIdb
# retain teh site as wp < wpval
af <- 100 * 2 / 2690
x <- 100 * af
shape <- 3.15777
scale <- 3.065158
frac <- 0.714285714285714
p1 <- pweibull(x,shape,scale,TRUE)
wp <- 1-((1 - frac) + (frac * p1))
countbg <- 74
wpval <- 0.05/countbg


# plot the pweibull and dweibull
curve(dweibull(x, shape=2, scale = 11), from=0, to=10)
curve(pweibull(x, shape=3, scale = 3), from=0, to=20)
