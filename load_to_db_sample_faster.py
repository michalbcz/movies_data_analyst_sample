import pandas as pd
from sqlalchemy import create_engine, Integer, String

# Create a SQLAlchemy engine
engine = create_engine("sqlite:///imdb_movies2.db")

# Insert DataFrame in bulk using SQLAlchemy
# Notes: You can't use to_sql method=multi because it's not supported by SQLite

dtype_mapping = {
    "nconst": String(),
    "primaryName": String(),
    "birthYear": Integer(),
    "deathYear": Integer(),
    "primaryProfession": String(),
    "knownForTitles": String()
}

chunk_size = 300000  # Define chunk size to manage memory usage
# Best time: 1m 48s
for chunk in pd.read_csv("data/imdb_datasets/name.basics.tsv", chunksize=chunk_size, sep="\t", na_values=["\\N"]):

    # Insert chunk into the SQLite database
    with engine.begin() as connection:
        #  Use raw_connection to execute PRAGMA settings for faster inserts
        raw_conn = connection.connection
        raw_conn.execute("PRAGMA synchronous = OFF;")
        raw_conn.execute("PRAGMA journal_mode = MEMORY;")
        raw_conn.execute("PRAGMA cache_size = -500000;")  # 500MB cache

        # Step 5.2: Write the chunk to the SQL table
        chunk.to_sql('my_table', connection, if_exists='append', index=False, dtype=dtype_mapping)

