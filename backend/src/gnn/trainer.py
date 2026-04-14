"""
InnerSight UEBA - Model Training Loop (The Teacher)

This class is used exclusively during the 'Offline Training Phase'.
It feeds thousands of historical daily graphs into the InnerSightGNN, 
calculates how wrong the AI's predictions are (the Loss Function), 
and updates the model's weights. 

Once training is complete, it saves the 'brain' (.pt file) to the /models directory.
"""
import torch

class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train_model(self, graph_dataset, epochs):
        """
        The main loop that iterates over the dataset, running forward passes, 
        calculating loss, and stepping the optimizer.
        """
        pass

    def save_weights(self, filename="innersight_v1.pt"):
        """Saves the trained model state to the disk."""
        pass
