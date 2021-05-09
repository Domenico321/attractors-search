

SUPPLEMENTARY FILES FOR THE MANUSCRIPT "Data-Driven Modeling Of Breast Cancer Tumors Using Boolean Networks"

The method for identifying boolean network attractors used in the manuscript is detailed below:

1: BINARIZE THE VALUES of scRNA-Seq DATA - The following procedure shows the steps for transforming the values of scRNA-Seq data into Boolean values (0, 1) through a binarization technique. For example, the TRIB3 text file represents the scRNA-Seq values to be transformed, in which the column indicates the expressed gene (in this case TRIB3), and each row describes the scRNA-Seq expression value from every single cell of a given patient.
Using the R script "Binarize.R" to process the text file "TRIB3.txt", boolean gene values are automatically obtained for every single cell in the archive. Adopting the same procedure, for each gene described in each line of the "SUPPLEMENTARY_TABLE_1.xlsx" dataset (supplementary table folder), we obtain the Boolean values for each gene of every cell. After performing this operation for all 103 genes (one per row) of the "SUPPLEMENTARY_TABLE_1.xlsx" dataset, the final result should be the one shown in "SUPPLEMENTARY_TABLE_6.xlsx," in which we transform the actual values of the gene expression of the first dataset into Boolean values (0, 1).


2: SEARCH FOR ATTRACTORS IN THE NETWORK - We proceed to search for network attractors after binarizing the scRNA-Seq values. The "attractors.py" script allows achieving this. Note that this script works with python version 2.7. We carried out the search for attractors for every cell where the previously binarized scRNA-Seq values are known. We modified the values obtained in SUPPLEMENTARY_TABLE_6 before submitting them to the python script. For each boolean gene value, we replaced the value 1 with the word "True" and the value 0 with the word "False." We have done this operation for all cells (columns) before searching for the corresponding attractors. The resulting modified file is the input for the python script. These are the steps to use the script correctly:

    1) When prompted by the script: "Please enter the excel file name:" enter the complete name of the file, including the extension, of the archive containing the binary values (0 and 1) previously processed with the R script. For example, you may enter "SUPPLEMENTARY_TABLE_6.xlsx". (When the excel file is available in the python workspace. Otherwise, indicate the appropriate path).
    2) At the next prompt, "Please enter the cell name," type the name of the cell from which you want to search for attractors. For example, type "BC01_02".

The python script for finding attractors ("attractors.py") works one cell (or column) at a time. The "model_definition1" section of the script contains the gene expression status of every single gene belonging to the network for a given cell.  The "Update rules" section of the script includes the Boolean functions applied to the inputs of each node making up the network. By inserting the appropriate value relative to the number of iterations ("model.iterate (steps = x)"), the script simulate a trajectory, where the network evolve for a certain number of steps until eventually reaching a stable state or cyclical set of states of the network representing an attractor. For the example provided in this repository, a message equal to "Cycle of length 6 starting at index 7" should be obtained, indicating that the gene network has encountered a cycle of 6 states after 18 iterations.



