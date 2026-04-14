"""
InnerSight UEBA - Configuration and Constants Blueprint

This file serves as the master configuration for the Data Ingestion Engine. 
Instead of hardcoding file paths, column names, or memory limits deep inside 
the parsing logic, all static rules are defined here. 

If the dataset format changes in the future, you only need to update this 
single file, and the entire pipeline will adapt automatically.
"""
import os

# --- Directory Paths ---
# Dynamically locates the root directory to ensure paths work on any machine (Mac or PC)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")

# --- CMU CERT Dataset Files ---
LOGON_FILE = "logon.csv"
HTTP_FILE = "http.csv"
FILE_FILE = "file.csv"

# --- Memory Management ---
# Defines how many rows Pandas should load into RAM at one time to prevent system crashes
CHUNK_SIZE = 100000 

# --- Essential Columns ---
# Defines the exact columns to extract from the messy logs, discarding the rest
LOGON_COLUMNS = ['id', 'date', 'user', 'pc', 'activity']
HTTP_COLUMNS = ['id', 'date', 'user', 'pc', 'url']
