# Movie Analysis 

1. Run `python -m pip install -r requirements.txt`
2. Run `python download_imdb_csv.py` (or skip this step if you have already downloaded and unzipped)
3. Run `python load_to_db_full_duckdb.py`
4. Open movies.duckdb with [DBeaver](https://dbeaver.io/) and let's SQL !

Directory structure:
- /data/imdb_datasets
  - Data downloaded from https://datasets.imdbws.com/ as of 10.10.2024. [See dataset documentation](https://developer.imdb.com/non-commercial-datasets/).

## CSFD parsing

Sample of CSFD parsing is in csfd.py


## Notes

* .gitignore is copy&paste from https://github.com/github/gitignore/blob/main/Python.gitignore