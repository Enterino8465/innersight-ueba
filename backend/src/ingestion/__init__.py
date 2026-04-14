"""
Data Ingestion Module (The Refinery)

This module is responsible for parsing raw CMU CERT log files (logon.csv, http.csv, etc.).
It cleans the data, handles missing values, and aggregates chronological events into 
24-hour 'User-Day' profiles. 

It acts as the first stage of the InnerSight UEBA pipeline, outputting clean Pandas DataFrames 
for the Graph Translation layer.
"""
