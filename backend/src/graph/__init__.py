"""
Graph Translation Module (The Translator)

This module takes the cleaned daily user profiles from the Ingestion engine and translates 
them into mathematical topology using PyTorch Geometric (HeteroData objects). 

It is responsible for defining what constitutes a Node (e.g., Users, PCs) and what 
constitutes an Edge (e.g., Logons, File Transfers) to build the Bipartite Graph.
"""
