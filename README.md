# Genetic_prediction_project

The file gene_condition_source_id.csv was downloaded from National Institute of Health, ClinVar, which is a freely accessible, public archive of reports of the relationships among human variations and phenotypes, with supporting evidence. ClinVar facilitates access to and communication about the relationships asserted between human variation and observed health status, and the history of that interpretation.

# About the dataset
The sources of information for the gene-disease relationship include OMIM, GeneReviews, and a limited amount of curation by NCBI staff. This document is updated daily, and is provided to report gene-disease relationships used in ClinVar, Gene, GTR and MedGen. The scope of disorders reported in this file is a subset of the disease_names file because a gene-to-disease relationship is required.  Explaination of terms mentioned in this data:


GeneID:               The NCBI GeneID
AssociatedGenes:      The preferred symbol corresponding to the GeneID for the gene reported to be causative for a particular disorder
RelatedGenes:         The preferred symbol corresponding to any gene that may contribute to a disorder.  This column is null for monogenic disorders, but will be reported for broader concepts. 
ConceptID:            The identifier assigned to a disorder associated with this gene. If the value starts with a C and is followed by digits, the ConceptID is a value from UMLS; if a value begins with CN, it was created by NCBI-based processing
DiseaseName:          Full name for the condition
SourceName:           Sources that use this name
SourceID:             The identifier used by this source
DiseaseMIM:           MIM number for the condition caused by the genes
LastUpdated:          Last time the record was modified by NCBI 

README.md -> Introduce the purpose of your project and provide your findings and next steps to go. Also, add a link to your data source.

Questions that will be answered 
1. Which is the most common genetic disorder
2. How was the disorder confirmed
3. Regions where it is more common
4. Which chromosome is most likely to be affected
5. What was the diagnostic test used to confirm it (predictive value and reliability)
6. What criteria were set to do this test
7. What is the most common pattern for the test
8. Is it single or multi gene
9. Chances of getting a single and multi-gene defect
