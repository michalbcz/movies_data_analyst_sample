import duckdb
import os

# Initialize DuckDB connection (database will be stored in memory, or you can specify a file)
conn = duckdb.connect('movies.duckdb')

# Ensure the 'imdb' schema is created
conn.execute("CREATE SCHEMA IF NOT EXISTS imdb;")

# Path where your CSV files are located
csv_dir = './data/imdb_datasets'

# Get all CSV files in the directory
csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.tsv')]

# Iterate through each CSV file and import it into DuckDB
for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)[0].replace('.', '_')  # Use file name (without extension) as table name
    csv_path = os.path.join(csv_dir, csv_file)
    
    # Import CSV into DuckDB table
    #conn.execute(f"COPY {table_name} FROM '{csv_path}' (AUTO_DETECT TRUE);")
    print(f"Creating table: {table_name} from: {csv_path}")
    conn.execute(f"""
        CREATE TABLE imdb.{table_name} AS 
        SELECT * FROM read_csv(
            '{csv_path}', 
            delim='\t', 
            nullstr='\\N', 
            quote='',   -- Disable quote character
            header=True
        );
    """)

# Optionally, verify that the data was loaded correctly
conn.execute("SHOW TABLES;").fetchall()