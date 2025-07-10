import torch
import torch.nn as nn
import numpy as np

class AEmbedFromMask(nn.Module):
    def __init__(self, mask_file_path):
        super(AEmbedFromMask, self).__init__()
        # Load the pre-computed mask from disk. The shape should be (N,)
        mask_np = np.load(mask_file_path)  # Example: mask.npy
        # Convert to torch.Tensor and register as a buffer (non-trainable parameter, saved with the model)
        self.register_buffer('node_mask', torch.from_numpy(mask_np).float())
        
    def forward(self, x):
        """
        Args:
            x: Input tensor of shape [B, T, N, C]
        Returns:
            Output tensor with mask appended as a new feature channel, shape [B, T, N, C+1]
        """
        B, T, N, C = x.shape
        # Reshape node_mask from [N] to [1, 1, N, 1], then expand to [B, T, N, 1]
        mask = self.node_mask.view(1, 1, N, 1).expand(B, T, N, 1)
        # Concatenate the mask to the last feature dimension
        x_out = torch.cat([x, mask], dim=3)
        return x_out
