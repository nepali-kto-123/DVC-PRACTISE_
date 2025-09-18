import pandas as pd 
import numpy as np
import os

df = pd.read_csv(r'c:\\Users\\hp\\Downloads\\dataset\\crocodile_dataset.csv')
df = df.iloc[:100, :5]
print(df)


if os.