import os
import requests
import gzip
import shutil

# It took on my computer: 3m 38.936s

# List of files from the IMDb dataset page
imdb_files = [
    "title.basics.tsv.gz",
    "title.crew.tsv.gz",
    "title.episode.tsv.gz",
    "title.principals.tsv.gz",
    "title.ratings.tsv.gz",
    "name.basics.tsv.gz",
    "title.akas.tsv.gz"
]

# Base URL for downloading IMDb datasets
base_url = "https://datasets.imdbws.com/"

# Directory for saving the downloaded files
download_dir = "data/imdb_datasets"
os.makedirs(download_dir, exist_ok=True)

# Function to download and unzip each file
def download_and_process_file(file_name):
    # Download the file
    file_url = base_url + file_name
    local_gz_path = os.path.join(download_dir, file_name)
    
    print(f"Downloading {file_name}...")
    response = requests.get(file_url, stream=True)
    with open(local_gz_path, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
    print(f"Downloaded {file_name}.")

    # Unzip the file
    local_tsv_path = local_gz_path[:-3]  # Remove '.gz' extension
    print(f"Unzipping {file_name}...")
    with gzip.open(local_gz_path, 'rb') as f_in:
        with open(local_tsv_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Unzipped to {local_tsv_path}.")

    # Create a tail of the first 100 lines
    tail_file_path = local_tsv_path.replace(".tsv", "_tail.tsv")
    print(f"Creating tail with first 100 lines for {file_name}...")
    with open(local_tsv_path, 'r', encoding='utf-8') as full_file, open(tail_file_path, 'w', encoding='utf-8') as tail_file:
        for i, line in enumerate(full_file):
            if i >= 100:
                break
            tail_file.write(line)
    print(f"Created {tail_file_path} with first 100 lines.\n")

# Download, unzip, and process each file
for imdb_file in imdb_files:
    download_and_process_file(imdb_file)

print("All files processed.")
