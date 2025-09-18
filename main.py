import pandas as pd 
import numpy as np
import os

df = pd.read_csv(r'c:\\Users\\hp\\Downloads\\dataset\\crocodile_dataset.csv')
df = df.iloc[:150, :5]

data_dir= "data"

os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")