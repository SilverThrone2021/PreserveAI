import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the datasets
flux_df = pd.read_csv("C:/Users/Sachin/Downloads/soil_moisture_Barrow_2012_2013.csv", skiprows=[1])
soil_df = pd.read_csv("C:/Users/Sachin/Downloads/flux_CO2_CH4_Barrow_2012_2013.csv", skiprows=[1])

# Convert date columns to datetime objects
flux_df['date'] = pd.to_datetime(flux_df['date'], format='%Y-%m-%d', errors='coerce')
soil_df['date'] = pd.to_datetime(soil_df['date'], format='%Y-%m-%d', errors='coerce')

# Drop rows with invalid date values
flux_df = flux_df.dropna(subset=['date'])
soil_df = soil_df.dropna(subset=['date'])

# Merge datasets
merged_df = pd.merge(flux_df, soil_df, on=['plot_ID', 'date'], how='inner')

# Convert VWC and Ka columns to numeric to avoid multiplication errors
merged_df['VWC'] = pd.to_numeric(merged_df['VWC'], errors='coerce')
merged_df['Ka'] = pd.to_numeric(merged_df['Ka'], errors='coerce')

# Drop rows with NaN values in the VWC or Ka columns (if any remain)
merged_df = merged_df.dropna(subset=['VWC', 'Ka'])

# Add the interaction term
merged_df['VWC_Ka_interaction'] = merged_df['VWC'] * merged_df['Ka']

# Scatter plot of flux_CH4 vs VWC
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='VWC', y='flux_CH4')
plt.title('Scatter Plot of CH4 Flux vs VWC')
plt.xlabel('VWC')
plt.ylabel('CH4 Flux')
plt.show()

# Scatter plot of flux_CH4 vs Ka
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='Ka', y='flux_CH4')
plt.title('Scatter Plot of CH4 Flux vs Ka')
plt.xlabel('Ka')
plt.ylabel('CH4 Flux')
plt.show()

# Heatmap of correlations
plt.figure(figsize=(8, 6))
sns.heatmap(merged_df[['VWC', 'Ka', 'VWC_Ka_interaction', 'flux_CH4']].corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Feature Correlations')
plt.show()

