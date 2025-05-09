# -*- coding: utf-8 -*-
"""houseprice_task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/chrissannahmecanzie/House-Price-Data-Analysis/blob/main/houseprice_task1.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import sklearn

from google.colab import files
upload =files.upload()

dataset=pd.read_csv("house_price.csv")

df=pd.DataFrame(dataset)

df

print(df.head())

print(df.describe())

price_per_sqft = df['price_per_sqft']

print(df.info())

# 1. Mean function
mean = price_per_sqft.mean()
std_dev = price_per_sqft.std()
df_mean = df[(price_per_sqft > (mean - 3*std_dev)) & (price_per_sqft < (mean + 3*std_dev))]

# 2. Percentile method
lower_percentile = price_per_sqft.quantile(0.01)
upper_percentile = price_per_sqft.quantile(0.99)
df_percentile = df[(price_per_sqft > lower_percentile) & (price_per_sqft < upper_percentile)]

# 3. IQR method
Q1 = price_per_sqft.quantile(0.25)
Q3 = price_per_sqft.quantile(0.75)
IQR = Q3 - Q1
df_iqr = df[(price_per_sqft > (Q1 - 1.5 * IQR)) & (price_per_sqft < (Q3 + 1.5 * IQR))]

# 4. Normal distribution method
df_normal = df[(np.abs(stats.zscore(price_per_sqft)) < 3)]

# 5. Z-score method
z_scores = stats.zscore(price_per_sqft)
df_zscore = df[(np.abs(z_scores) < 3)]

plt.figure(figsize=(12, 6))
sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.title('Box Plot for Numerical Columns')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['price_per_sqft'], kde=True)
plt.title('Histogram of Price Per Sqft')
plt.xlabel('Price Per Sqft')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 8))
plt.title('Correlation Heatmap')
plt.show()

sns.pairplot(df.select_dtypes(include=['float64', 'int64']))
plt.show()