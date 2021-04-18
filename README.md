1: BINARIZE THE VALUES of RNA-Seq DATA
The following procedure shows the steps for transforming the values of RNA-Seq data into Boolean values (0, 1) through a binarization technique. For example, the TRIB3 text file represents the RNA-Seq values to be transformed, in which the column indicates the expressed gene (in this case TRIB3), and each row describes the RNA-Seq expression value from every single cell of a given patient.

Using the R script "Binarize.R" to process the text file "TRIB3.txt", boolean gene values are automatically obtained for every single cell in the archive. Adopting the same procedure, for each gene described in each line of the "SUPPLEMENTARY_TABLE_1.xlsx" dataset (supplementary table folder), we obtain the Boolean values for each gene of every cell. After performing this operation for all 103 genes (one per row) of the "SUPPLEMENTARY_TABLE_1.xlsx" dataset, the final result should be the one shown in "SUPPLEMENTARY_TABLE_6.xlsx," in which we transform the actual values of the gene expression of the first dataset into Boolean values (0, 1).


2: SEARCH FOR ATTRACTORS IN THE NETWORK
We proceed to search for network attractors after binarizing the RNA-Seq values. The "attractors.py" script allows achieving this. Note that this script works with python version 2.7. We carried out the search for attractors for every cell where the previously binarized RNA-Seq values are known.  We modified the values obtained in  SUPPLEMENTARY_TABLE_6 before submitting them to the python script. For each boolean gene value, we replaced the value 1 with the word "True" and the value 0 with the word "False." We have done this operation for all cells (columns) before searching for the corresponding attractors. The resulting modified file is the input for the python script.


The python script for finding attractors ("attractors.py") works one cell (or column) at a time. The "model definition" section of the script contains the gene expression status of every single gene belonging to the network for a given cell. The "Update rules" section of the script contains the Boolean functions applied to the inputs of each node making up the network. By inserting the appropriate value relative to the number of iterations to be carried out on the network ("model.iterate (steps = x)"), the script simulate a trajectory where the network evolve for a certain number of steps until eventually reaching a stable state or cyclical set of states of the network representing an attractor. In the case taken as an example, a message equal to "Cycle of length 6 starting at index 7" should be obtained, indicating that the gene network has encountered a cycle of 6 states after 18 iterations.



