1:            BINARIZE THE VALUES of Rna.Seq

The following procedure shows the steps for transforming the values of RNa-Seq into Boolean values (0, 1) through a binarization technique.For example, the TRIB3 text file represents the Rna-Seq values to be transformed, in which the column indicates the expressed gene (in this case TRIB3), and each row describes the Rna-Seq level from each single analyzed  cell of a given patient.

Using the R script "Binarize.R" to process the text file "TRIB3.txt", the Boolean values relating to the Rna-Seq data corresponding to the given gene are automatically obtained for each single cell in the archive. Adopting the same procedure, for each gene described in each line of the "Supplementary_table_1.xlsx" dataset in the supplementary table folder of this repository, the Boolean values of each cell analyzed for each gene are obtained.


2:                RESEARCH NET ATTRACTORS

having binarized the Rna-Seq values of each single cell corresponding to the genes making up the network to be analyzed, we proceed to search for any attractors deriving from the dynamics of the network. The "attractors.py" script allows this to be achieved. Note that this script works with python version 2.7.
The search for attractors must be carried out for each single elaborated cell of which the previously binarized Rna-Seq values are known. The "model definition" section of the script contains the gene expression status of each single gene belonging to the network for a given cell conventionally defined as "True" in the case in which the Boolean value is equal to "1", "False" in the case where this value is equal to "0".
The "Update rules" section of the script contains the indication of the Boolean functions applied to the input inputs of each node making up the network.
By inserting the appropriate value relative to the number of iterations to be carried out on the network ("model.iterate (steps = x)"), the script is allowed to make the network evolve for a certain number of steps until eventually meeting a stable or cyclical state of the network system configuration representing an attractor. in the case taken as an example, a message equal to "Cycle of length 6 starting at index 7" should be reached, indicating that the gene network has encountered a cycle of 6 after setting the program with 18 iterations.

