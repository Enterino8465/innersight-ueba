"""
InnerSight UEBA - Vector Generation (The Inference Engine)

This class is used during the 'Live Inference Phase' (when the dashboard is running).
It loads a pre-trained AI brain from the disk, looks at today's brand-new graph, 
and compresses it into a high-dimensional Vector Embedding.
"""
import torch

class VectorGenerator:
    def __init__(self, model_path):
        """Loads the pre-trained weights from the /models directory."""
        pass

    def generate_embedding(self, daily_graph):
        """
        Pushes a single daily graph through the network without updating weights,
        returning the final mathematical coordinate representing the user's risk.
        """
        pass
