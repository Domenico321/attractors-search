#Package installation of "Binarize"
install.packages("Binarize")
#Package loading
library("Binarize")
#Loading the data file
dati=read.table("TRIB3.txt", header=T)
str(dati)
#Setting binarization method
result=binarize.BASC(dati[,"TRIB3"], method="B", tau=0.1)
print(result)







