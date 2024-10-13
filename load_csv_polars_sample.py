import polars as pl

# This script using Polars instead of Pandas takes 6s on my computer to run

# Load the data from the gzipped TSV file
file_path = "./data/imdb_datasets/name.basics.tsv.gz"
# df = pl.read_csv(file_path, sep='\t', compression='gzip')
df = pl.read_csv("./data/name.basics.tsv.gz", separator="\t", null_values=["\\N"])

# Display the first few rows of the dataframe
print(df.head())

# print(df.info())
print(df.describe())
# print(df.schema)
# print(df.shape)
print(df.estimated_size())
