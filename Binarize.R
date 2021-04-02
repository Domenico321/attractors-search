install.packages("Binarize")
library("Binarize")
dati=read.table("revision.txt", header=T)
str(dati)
result=binarize.BASC(dati[,"TRIB3"], method="B", tau=0.1)
print(result)







