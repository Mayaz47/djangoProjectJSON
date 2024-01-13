from django.test import TestCase
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler, PowerTransformer

# Create your tests here.
df = pd.read_csv('data.csv')
df['open'] = pd.to_numeric(df['open'], errors='coerce')
df['close'] = pd.to_numeric(df['close'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

plt3, ax1 = plt.subplots(figsize=(10, 6))

# Example: Line Plot with Seaborn
scaler = PowerTransformer(method='yeo-johnson')

# Fit and transform the 'volume' column
df['normalized_close'] = scaler.fit_transform(df[['close']])
df['normalized_open'] = scaler.fit_transform(df[['open']])
df['normalized_volume'] = scaler.fit_transform(df[['volume']])
sns.jointplot(x = 'normalized_close', y = 'normalized_volume', kind = 'kde', data = df, ax=ax1)
ax1.set_title('Normalize Boxplot')

# Show the plot
plt.show()