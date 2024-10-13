import pandas as pd

# This whole script takes 25s on my computer to run

# Load the data from the gzipped TSV file
file_path = "./data/imdb_datasets/name.basics.tsv.gz"
# df = pd.read_csv(file_path, sep='\t', compression='gzip')
df = pd.read_csv("./data/name.basics.tsv", sep="\t", na_values=["\\N"])

# Display the first few rows of the dataframe
print(df.head())
print(df.info())
