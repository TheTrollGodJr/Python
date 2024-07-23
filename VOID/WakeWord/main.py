import pandas as pd
import torch
import torchaudio
from torch.utils.data import Dataset, DataLoader
import torchaudio.transforms as T
import os
from sklearn.model_selection import train_test_split


# Custom Dataset Class
class BinaryWakeWordDataset(Dataset):
    def __init__(self, dataframe, root_dir, transform=None):
        self.dataframe = dataframe
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        file_path = os.path.join(self.root_dir, self.dataframe.iloc[idx, 0])
        label = torch.tensor(self.dataframe.iloc[idx, 1], dtype=torch.float32)

        # Load audio file using torchaudio
        waveform, sample_rate = torchaudio.load(file_path)

        # Apply transformations if any
        if self.transform:
            waveform = self.transform(waveform)

        return waveform, label

# Load labels from CSV
labels_df = pd.read_csv('dataset/labels.csv')

# Split into training and validation sets
train_df, val_df = train_test_split(labels_df, test_size=0.2, random_state=42)

# Define audio transformations (you can customize these)
transform = T.Compose([
    T.MelSpectrogram(sample_rate=16000, n_mels=128),
    T.FrequencyMasking(freq_mask_param=15),
    T.TimeMasking(time_mask_param=35),
    T.Normalize(mean=0.5, std=0.5),
])

# Create datasets and dataloaders
train_dataset = BinaryWakeWordDataset(train_df, root_dir='dataset', transform=transform)
val_dataset = BinaryWakeWordDataset(val_df, root_dir='dataset', transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)