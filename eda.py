import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOAD KARO
df = pd.read_csv('books_dataset.csv')

# 2. BASIC INFO DEKHO
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nData Types:\n", df.dtypes)
print("\nFirst 5 Rows:\n", df.head())

# 3. BASIC QUESTIONS PUCHHO
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Stats:\n", df.describe())

# 4. VISUALIZATION - EXAMPLE
# Agar price column hai to:
# plt.figure(figsize=(10,6))
# sns.histplot(df['price'], bins=20)
# plt.title('Book Price Distribution')
# plt.show()

print("\nEDA Complete!")