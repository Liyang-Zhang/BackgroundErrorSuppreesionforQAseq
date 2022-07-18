# Make heatmap for MRD NC databases to explore error rate in different base substitutions

library(ggplot2)
require(reshape2)
require(scales)
require(plyr)

setwd("~/MRD/standardResult/heatmap")
path <- "~/MRD/standardResult/standard_3rdtrial/errorSuppression/ABC/UMIdb/db/report"

mydat73 <- read.csv(file = "C:/Users/admin/Documents/MRD/standardResult/standard_3rdtrial/errorSuppression/ABC/UMIdb/db/report/73-NC_errorRate_prepolish.txt", sep = "\t", header = TRUE)
mydat74 <- read.csv(file = "C:/Users/admin/Documents/MRD/standardResult/standard_3rdtrial/errorSuppression/DEF/UMIdb/db/report/74-NC_errorRate_prepolish.txt", sep = "\t", header = TRUE)
#mydat76 <- read.csv(file = "C:/Users/admin/Documents/MRD/standardResult/standard_3rdtrial/errorSuppression/GHJ/UMIdb/db/report/76-NC_errorRate_prepolish.txt", sep = "\t", header = TRUE)
mydat75 <- read.csv(file = "C:/Users/admin/Documents/MRD/standardResult/standard_3rdtrial/errorSuppression/KLM/UMIdb/db/report/75-NC_errorRate_prepolish.txt", sep = "\t", header = TRUE)
mydat81 <- read.csv(file = "C:/Users/admin/Documents/MRD/standardResult/standard_3rdtrial/errorSuppression/AGAHAJ/UMIdb/db/report/81-NC_errorRate_prepolish.txt", sep = "\t", header = TRUE)
mydat_list <- list(mydat73, mydat74, mydat75, mydat81)
mydat <- Reduce(function(x, y) merge(x, y, all=TRUE), mydat_list)
#mydat <- merge(mydat73, mydat74, by="X")
mydat.m <-reshape2::melt(mydat)
colnames(mydat.m) <- c("substitution", "sample", "errorrate")
#data <- as.matrix(data)

#mydat.m <- ddply(mydat.m, .(sample), transform, rescale = rescale(errorrate))
#mydat.m <- ddply(mydat.m, .(sample), transform)
p <- ggplot(mydat.m, aes(sample, substitution)) +
  geom_tile(aes(fill = errorrate),colour = "navy") +
  scale_fill_gradient(name="error rate (%)", low = "navy",high = "yellow") +
  theme(axis.ticks.x = element_blank(),
        axis.text.x = element_blank())
