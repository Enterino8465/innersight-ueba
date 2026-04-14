"""
InnerSight UEBA - Log Parsing Module (The Cleaner)

This class is responsible for the first phase of the ingestion pipeline. It safely 
opens the massive CMU CERT log files in manageable chunks using the rules defined 
in constants.py. 

Its primary jobs are:
1. Dropping irrelevant columns to save memory.
2. Handling or dropping missing/null values.
3. Standardizing all datetime strings into universally readable timestamp objects.
"""
import pandas as pd
from backend.ingestion import constants

class CertParser:
    def __init__(self):
        """Initializes the parser by linking it to the local data directory."""
        self.data_dir = constants.DATA_DIR

    def load_and_clean_logons(self):
        """
        Iterates through logon.csv in chunks, filters out unnecessary columns, 
        standardizes the datetime format, and returns a clean DataFrame.
        """
        pass

    def load_and_clean_http(self):
        """
        Iterates through http.csv, extracts domain names from URLs, 
        standardizes timestamps, and returns a clean DataFrame.
        """
        pass
