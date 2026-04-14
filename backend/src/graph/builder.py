"""
InnerSight UEBA - Graph Construction Module (The Topology Builder)

This class is responsible for translating tabular daily profiles into 
mathematical graphs. It utilizes PyTorch Geometric's HeteroData structure 
to map different types of Nodes (Users, PCs, Resources) and the Edges 
that connect them (Logons, Downloads).
"""
import torch
from torch_geometric.data import HeteroData

class GraphConstructor:
    def __init__(self):
        """Initializes the constructor, preparing it to process daily DataFrames."""
        pass

    def build_daily_graph(self, daily_profile_df):
        """
        Takes a 24-hour Pandas DataFrame and extracts the unique entities to create 
        Node indices, then maps the interactions to create Edge indices.
        Returns a populated HeteroData object.
        """
        pass
