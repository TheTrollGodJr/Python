import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchaudio
import torchaudio.transforms as audio_transforms
#import torchvision.transforms as vision_transforms


# Define a CNN model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=2, out_channels=32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.fc1 = nn.Linear(64*56*32, 128)
        self.fc2 = nn.Linear(128, 1)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.max_pool2d(x, kernel_size=(2, 2))
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, kernel_size=(2, 2))
        x = x.view(-1, 64*56*32)
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Custom collate function
def collate_fn(batch):
    # Get the maximum length of the spectrograms in the batch
    max_length = max([item[0].shape[2] for item in batch])

    # Pad or trim each spectrogram to have the same length
    padded_batch = []
    for spectrogram, label in batch:
        if spectrogram.shape[2] < max_length:
            padded_spectrogram = torch.nn.functional.pad(spectrogram, (0, max_length - spectrogram.shape[2]))
        elif spectrogram.shape[2] > max_length:
            padded_spectrogram = spectrogram[:, :, :max_length]
        else:
            padded_spectrogram = spectrogram
        padded_batch.append((padded_spectrogram, label))

    # Stack the padded spectrograms and labels
    stacked_spectrograms = torch.stack([item[0] for item in padded_batch])
    labels = torch.tensor([item[1] for item in padded_batch])

    return stacked_spectrograms, labels

# Custom Dataset class with preprocessing
class CustomDataset(Dataset):
    def __init__(self, file_list, max_length):
        self.file_list = file_list
        self.max_length = max_length

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        file_path, label = self.file_list[idx].split('|')
        waveform, sample_rate = torchaudio.load(file_path)
        # Check if waveform has only 1 channel, if not, select first 2 channels
        if waveform.size(0) == 1:
            waveform = torch.cat([waveform, waveform], dim=0)
            
        mel_spec_transform = audio_transforms.MelSpectrogram(sample_rate=sample_rate)
        mel_spectrogram = mel_spec_transform(waveform)
        # Rest of your preprocessing...
        label = int(label == 'True')
        return mel_spectrogram, label

    def preprocess_audio(self, file_path):
        waveform, sample_rate = torchaudio.load(file_path)
        mel_spec_transform = audio_transforms.MelSpectrogram(sample_rate=sample_rate)
        mel_spectrogram = mel_spec_transform(waveform)

        # Pad or trim spectrogram to fixed length
        if mel_spectrogram.shape[2] < self.max_length:
            mel_spectrogram = torch.nn.functional.pad(mel_spectrogram, (0, self.max_length - mel_spectrogram.shape[2]))
        elif mel_spectrogram.shape[2] > self.max_length:
            mel_spectrogram = mel_spectrogram[:, :, :self.max_length]

        return mel_spectrogram

# Load the list of file paths and labels
with open('VOID/AI/WakeWord/dataset/positive/labels.txt', 'r') as f:
    file_labels = f.readlines()

# Splitting the dataset into train and validation
train_size = int(0.8 * len(file_labels))
train_data = file_labels[:train_size]
valid_data = file_labels[train_size:]

# Creating datasets and dataloaders
train_dataset = CustomDataset(train_data, max_length=400)
valid_dataset = CustomDataset(valid_data, max_length=400)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)
valid_loader = DataLoader(valid_dataset, batch_size=32, shuffle=False, collate_fn=collate_fn)

# Initialize the model, loss function, and optimizer
model = CNN()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels.unsqueeze(1).float())
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch {epoch+1}/{num_epochs}, Training Loss: {running_loss/len(train_loader)}")

# Validation loop
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in valid_loader:
        outputs = model(inputs)
        predicted = torch.round(outputs)
        total += labels.size(0)
        correct += (predicted == labels.unsqueeze(1)).sum().item()

print(f'Accuracy on validation set: {100 * correct / total}%')

# Save the trained model
torch.save(model.state_dict(), 'VOID/AI/trained_model.pth')
print("Model saved.")
