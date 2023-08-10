# Genetic_prediction_project
The purpose of the project was to find out the most common genetic disorder(based on information available in the dataset), and the genes responsible for causing the disorder. Along with that, finding the most common disorders and most common genes to have a defect was a secondary aim of the project. Finally, finding the probabilities of the above mentioned issues was the most significant purpose of the project.
The file gene_condition_source_id.csv was downloaded from National Institute of Health, ClinVar, which is a freely accessible, public archive of reports of the relationships among human variations and phenotypes, with supporting evidence. ClinVar facilitates access to and communication about the relationships asserted between human variation and observed health status, and the history of that interpretation.

About the dataset (link https://ftp.ncbi.nlm.nih.gov/pub/clinvar/)
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

Questions that will be answered 

1. Which is the most common genetic disorder? -> Cardiomyopathy, which is a disease of the heart muscle that makes it harder for the heart to pump blood to the rest of the body
2. Which Gene  is most likely to cause a disorder? -> The Gene ID causing the maximum number of diseases is 1280
3. Is Cardiomyopathy caused my associated genes or related gene?s -> It is caused by related genes. This proves that the chances of getting Cardiomyopathy at birth are very less. It is mostly acquired over time, The symptoms are elevated due to external factors
4. What are the top 5 most common disease caused by a defect in genes? -> Cardiomyopathy, Hereditary hearing loss and deafness, Retinitis pigmentosa, Charcot-Marie-Tooth disease, Mitochondrial disease
5. What are Top 5 gene IDs causing the maximum number of diseases? -> 3845, 2261, 1280, 5290, 1557
6. What is the probability of getting a genetic disorder by defect on the above-mentioned genes?-> 0.72%
7. What is the probability of getting a defect on Related and Associated gene?-> Probability of getting a disease with associated genes: 0.64, Probability of getting a disease with related genes:0.35

Conclusions:
The most common genetic disorder analyzed in this dataset is Cardiomyopathy. The gene ID 1280 is most likely to cause a genetic disorder, as it is associated with the highest number of diseases in the dataset.
Cardiomyopathy is primarily caused by related genes rather than associated genes. This suggests that the likelihood of being born with Cardiomyopathy is relatively low, and it is more often acquired over time due to external factors. Among the genetic disorders analyzed, the top five caused by gene defects are Cardiomyopathy, Hereditary hearing loss and deafness, Retinitis pigmentosa, Charcot-Marie-Tooth disease, and Mitochondrial disease. The top five gene IDs associated with the maximum number of diseases are 3845, 2261, 1280, 5290, and 1557. The overall probability of getting a genetic disorder due to defects in the mentioned genes is calculated to be 0.72%. The probabilities of getting a disease with associated genes and related genes are 0.64 and 0.35, respectively.

Recommendations:
While Cardiomyopathy appears to be the most common genetic disorder in the analyzed dataset, it is essential to note that the dataset may not cover all possible genes and disorders. Further research using more extensive datasets could provide a more comprehensive understanding of genetic disorders in humans.
To improve the accuracy and applicability of genetic research, it is crucial to invest in more extensive genetic studies and foster collaboration among researchers and medical professionals.

Limitations:
The conclusions drawn in this project are limited to the dataset used and may not reflect the full spectrum of genetic disorders that exist in reality. Therefore, these conclusions should not be considered as medical references. The dataset used may not cover all known genes and their associated disorders, potentially leading to an incomplete picture of genetic disorders' prevalence and impacts.
The dataset was clean but contained null values for where the defect was on one gene(Either on Associated gene or Related gene). the null values did not affect the results in any way.
A more detailed dataset would have helped to create a machine-learning, model to predict if a baby would have any serious genetic disorder with a non-invasive method of diagnosis


