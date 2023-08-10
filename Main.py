import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from gene_functions import *

# Read the gene data from the file
file_path = '../Data/raw/gene_condition_source_id.csv'
data = read_gene_data(../Data/raw/gene_condition_source_id.csv)

# Group the data by Gene ID and count the number of unique disease names
gene_counts = group_genes_by_geneid(data)
print(gene_counts)

# Get the unique gene IDs
unique_gene_ids = find_unique_genes(data)
print("Unique Gene IDs:")
for gene_id in unique_gene_ids:
    print(gene_id)

# Find the Gene ID with the maximum count of unique disease names
max_gene_id = find_max_disease_gene(data)
print("Gene ID with the maximum number of disease names:", max_gene_id)

# Calculate the probability of getting a defect on the gene ID 1280 out of all gene IDs
probability = calculate_gene_probability(data, max_gene_id)
print("Probability of getting the gene ID", max_gene_id, "out of all gene IDs:", probability)

# Find out the names of Diseases and disorders caused by the defect on gene ID 1280
disease_names = find_diseases_by_gene(data, max_gene_id)
print("Disease names associated with the gene ID", max_gene_id)
for disease_name in disease_names:
    print(disease_name)

# Find out the top 5 gene IDs causing the maximum number of diseases and plot them
top_5_genes = find_top_5_genes(data)
print("Top 5 gene IDs causing the maximum number of diseases:")
for gene_id, count in top_5_genes.items():
    print("Gene ID:", gene_id, " | Number of Diseases:", count)

plot_top_5_genes(top_5_genes)

# Calculate the probabilities of getting a disease with associated and related genes
prob_associated, prob_related = calculate_gene_disease_probabilities(data)
print("Probability of getting a disease with associated genes:", prob_associated)
print("Probability of getting a disease with related genes:", prob_related)

# Find out the Gene IDs and names of the diseases and disorders associated with the top 5 diseases
top_5_disease_genes = find_top_5_diseases(data)
print("Gene IDs and Associated Disease Names for the top 5 diseases:")
for gene_id, disease_name in top_
