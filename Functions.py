# gene_functions.py

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

#functions.py for Genetic_Prediction_gene

def read_gene_data(../Data/raw/gene_condition_source_id.csv):
    # Read the gene data from the specified file path
    return pd.read_csv(../Data/raw/gene_condition_source_id.csv)

def group_genes_by_geneid(data):
    # Group the data by Gene ID and count the number of unique disease names
    gene_counts = data.groupby('GeneID')['DiseaseName'].nunique()
    return gene_counts

def find_unique_genes(data):
    # Get the unique gene IDs from the data
    return data['GeneID'].unique()

def find_max_disease_gene(data):
    # Find the Gene ID with the maximum count of unique disease names
    gene_counts = data.groupby('GeneID')['DiseaseName'].nunique()
    max_gene_id = gene_counts.idxmax()
    return max_gene_id

def calculate_gene_probability(data, gene_id):
    # Calculate the probability of getting a defect on the specified gene ID
    total_gene_ids = len(data['GeneID'].unique())
    gene_id_count = len(data[data['GeneID'] == gene_id])
    probability = gene_id_count / total_gene_ids
    return probability

def find_diseases_by_gene(data, gene_id):
    # Filter the dataset for the disease names associated with the specified gene ID
    filtered_data = data[data['GeneID'] == gene_id]
    disease_names = filtered_data['DiseaseName'].unique()
    return disease_names

def find_top_5_genes(data):
    # Group the data by Gene ID and count the number of unique disease names
    gene_counts = data.groupby('GeneID')['DiseaseName'].nunique()
    top_5_gene_ids = gene_counts.sort_values(ascending=False).head(5)
    return top_5_gene_ids

def plot_top_5_genes(data):
    # Convert to a DataFrame for plotting
    df = pd.DataFrame({'Gene ID': data.index, 'Number of Diseases': data.values})
    
    # Create a bar plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Gene ID', y='Number of Diseases', data=df, color='orange')
    
    # Set the plot labels and title
    plt.xlabel('Gene ID')
    plt.ylabel('Number of Diseases')
    plt.title('Top 5 Gene IDs Causing the Maximum Number of Diseases')
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def calculate_gene_disease_probabilities(data):
    # Calculate the probabilities of getting a disease with associated and related genes
    total_diseases = len(data)
    associated_genes_data = data.dropna(subset=['AssociatedGenes'])
    related_genes_data = data.dropna(subset=['RelatedGenes'])
    
    diseases_with_associated_genes = len(associated_genes_data)
    diseases_with_related_genes = len(related_genes_data)
    
    probability_associated_genes = diseases_with_associated_genes / total_diseases
    probability_related_genes = diseases_with_related_genes / total_diseases
    
    return probability_associated_genes, probability_related_genes

def find_top_5_diseases(data):
    # Get the top 5 most common disease names
    top_5_diseases = data['DiseaseName'].value_counts().head(5).index.tolist()
    
    # Filter the dataset for the top 5 disease names
    filtered_data = data[data['DiseaseName'].isin(top_5_diseases)]
    
    # Create a list of tuples containing gene IDs and their associated disease names
    gene_disease_list = [(row['GeneID'], row['DiseaseName']) for _, row in filtered_data.iterrows()]
    
    return gene_disease_list

def find_cardiomyopathy_genes(data):
    # Filter the dataset for rows with 'Cardiomyopathy' in the 'DiseaseName' column
    cardiomyopathy_data = data[data['DiseaseName'] == 'Cardiomyopathy']
    
    # Count the number of associated genes and related genes for cardiomyopathy
    num_associated_genes = cardiomyopathy_data['AssociatedGenes'].notnull().sum()
    num_related_genes = cardiomyopathy_data['RelatedGenes'].notnull().sum()
    
    return num_associated_genes, num_related_genes


# functions.py for Genetic_Prediction_disorder


def load_data('../Data/raw/gene_condition_source_id.csv'):
    """
    Load data from a CSV file and return a pandas DataFrame.
    """
    return pd.read_csv('../Data/raw/gene_condition_source_id.csv')

def get_most_common_disorder(data):
    """
    Get the most common disorder from the dataset.

    Parameters:
        data (pd.DataFrame): The input dataset.

    Returns:
        str: The most common disorder name.
    """
    most_common_disorder = data['DiseaseName'].value_counts().idxmax()
    return most_common_disorder

def get_genes_for_disorder(data, disorder_name):
    """
    Get associated genes and related genes for a specific disorder.

    Parameters:
        data (pd.DataFrame): The input dataset.
        disorder_name (str): The name of the disorder.

    Returns:
        list: A list of associated genes for the disorder.
        list: A list of related genes for the disorder.
    """
    filtered_data = data[data['DiseaseName'] == disorder_name]
    associated_genes = filtered_data['AssociatedGenes'].dropna().unique().tolist()
    related_genes = filtered_data['RelatedGenes'].dropna().unique().tolist()
    return associated_genes, related_genes

def get_top_5_diseases(data):
    """
    Get the top 5 most common disease names from the dataset.

    Parameters:
        data (pd.DataFrame): The input dataset.

    Returns:
        pd.Series: A pandas Series containing the top 5 disease names and their counts.
    """
    top_5_diseases = data['DiseaseName'].value_counts().head(5)
    return top_5_diseases

def plot_top_5_diseases(data):
    """
    Plot a bar graph for the top 5 most common disease names.

    Parameters:
        data (pd.DataFrame): The input dataset.
    """
    top_5_diseases = get_top_5_diseases(data)
    top_5_df = top_5_diseases.reset_index()
    top_5_df.columns = ['DiseaseName', 'Count']

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(y='Count', x='DiseaseName', data=top_5_df, palette='viridis')

    plt.ylabel("No. of Genes")
    plt.xlabel("Disease Name")
    plt.title("Top 5 Most Common Disease Names")
    plt.tight_layout()

    plt.show()

def filter_data_by_top_5_diseases(data):
    """
    Filter the data to include only the top 5 most common diseases.

    Parameters:
        data (pd.DataFrame): The input dataset.

    Returns:
        pd.DataFrame: The filtered DataFrame with necessary columns.
    """
    top_5_diseases = get_top_5_diseases(data)
    top_5_disease_names = top_5_diseases.index.tolist()
    filtered_data = data[data['DiseaseName'].isin(top_5_disease_names)]
    selected_columns = ['GeneID', 'AssociatedGenes', 'RelatedGenes', 'DiseaseName']
    result = filtered_data[selected_columns]
    return result

def get_diseases_by_most_common_gene(data):
    """
    Find out all the total number and names of the diseases caused by the gene with the most disorders.

    Parameters:
        data (pd.DataFrame): The input dataset.

    Returns:
        int: Number of disease names associated with the most common gene.
        list: A list of disease names associated with the most common gene.
    """
    gene_counts = data.groupby('GeneID')['DiseaseName'].nunique()
    max_gene_id = gene_counts.idxmax()
    filtered_data = data[data['GeneID'] == max_gene_id]
    disease_names = filtered_data['DiseaseName'].unique()
    num_disease_names = len(disease_names)
    return num_disease_names, disease_names

if __name__ == "__main__":
    # You can test the functions here if needed
    file_path = '../Data/raw/gene_condition_source_id.csv'
    data = load_data(file_path)
    most_common_disorder = get_most_common_disorder(data)
    print("The most common disorder is:", most_common_disorder)

    associated_genes, related_genes = get_genes_for_disorder(data, most_common_disorder)
    print("Associated Genes for", most_common_disorder + ":")
    for gene in associated_genes:
        print(gene)

    print("\nRelated Genes for", most_common_disorder + ":")
    for gene in related_genes:
        print(gene)

    plot_top_5_diseases(data)

    filtered_data = filter_data_by_top_5_diseases(data)
    print("Gene ID, Associated Genes, Related Genes, and DiseaseName for the top 5 most common disease names:")
    print(filtered_data)

    num_disease_names, disease_names = get_diseases_by_most_common_gene(data)
    print("Number of disease names associated with the most common gene:", num_disease_names)
    print("Disease names associated with the most common gene:")
    for disease_name in disease_names:
        print(disease_name)

