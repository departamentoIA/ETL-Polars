# ETL-Polars
ETL process with Polars. DataFrames (tables) are obtain from csv files.

## 🌎 Repository Structure
```
ETL-Polars/
├── main.py
├── .gitignore
├── env/                # Virtual enviroment (not provided)
└── requirements.txt
└── pkg                 # Contains all needed files (Python package)
    └── __init__.py     # Specifies that folder 'pkg' is a Python package
    └── extract.py      # Contains all functions related to extraction process
    └── transform.py    # Contains all functions related to transform process
    └── globals.py      # Contains all global variables
    └── config.py       # Contains all configuration params
```


## ✨ Details

**main.py:** This script calls 'extract.py' to obtain the DataFrames corresponding to the tables, then 'transform.py' script is called to clean data and to convert the columns into the correct format.

## 🚀 How to run locally
1. Clone this repository:
```
git clone https://github.com/departamentoIA/ETL-Polars.git
```
2. Set virtual environment and install dependencies.

For Windows:
```
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
```
For Linux:
```
python -m venv env && source env/bin/activate && pip install -r requirements.txt
```
3. Run "main.py".
