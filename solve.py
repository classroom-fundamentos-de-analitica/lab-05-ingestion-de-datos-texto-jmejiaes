import os
import pandas as pd
import zipfile

# Step 1: Unzip the data.zip file
with zipfile.ZipFile('data.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Step 2: Function to read text files and extract data
def extract_data_from_directory(directory):
    data = []
    for sentiment in ['negative', 'positive', 'neutral']:
        sentiment_dir = os.path.join(directory, sentiment)
        for filename in os.listdir(sentiment_dir):
            if filename.endswith('.txt'):
                file_path = os.path.join(sentiment_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    data.append({'phrase': phrase, 'sentiment': sentiment})
    return data

# Step 3: Extract data for train and test directories
train_data = extract_data_from_directory('train')
test_data = extract_data_from_directory('test')

# Step 4: Create DataFrames
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Step 5: Save DataFrames to CSV files
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)