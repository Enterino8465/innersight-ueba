"""
InnerSight UEBA - Daily Aggregation Module (The Grouper)

This class represents the second phase of the ingestion pipeline. It takes the 
chronologically sorted, cleaned DataFrames from the CertParser and shifts the 
perspective from 'Events' to 'Entities'.

Its primary job is to group isolated network actions into bounded 24-hour windows. 
The final output is a structured profile where a single row represents one specific 
user's total behavior for one specific day, perfectly formatted for the Graph component.
"""
import pandas as pd

class DailyProfileBuilder:
    def __init__(self):
        pass

    def group_by_user_day(self, cleaned_df):
        """
        Takes a cleaned DataFrame of sequential events, isolates them by the 'user' ID, 
        and groups them by calendar day.
        """
        pass
        
    def merge_daily_activities(self, logon_df, http_df):
        """
        Joins the grouped logon behaviors and web behaviors together on the 'user' 
        and 'date' keys to create a single, unified daily profile.
        """
        pass
