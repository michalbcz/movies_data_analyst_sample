import pandas as pd
from sqlalchemy import create_engine, Integer, String

# Create a SQLAlchemy engine
engine = create_engine("sqlite:///imdb_movies.db")

dtype_mapping = {
    "nconst": String(),
    "primaryName": String(),
    "birthYear": Integer(),
    "deathYear": Integer(),
    "primaryProfession": String(),
    "knownForTitles": String()
}

# Insert DataFrame in bulk using SQLAlchemy
# Notes: You can't use to_sql method=multi because it's not supported by SQLite
# This takes 2m20s on my computer to run
chunk_size = 100000  # Define chunk size to manage memory usage
for chunk in pd.read_csv("data/imdb_datasets/name.basics.tsv", chunksize=chunk_size, sep="\t", na_values=["\\N"]):
    chunk.to_sql("name_basics", engine, if_exists="append", index=True, dtype=dtype_mapping)
