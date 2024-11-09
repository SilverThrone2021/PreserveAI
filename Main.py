import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

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

# Feature Selection and Target Variable
features = ['VWC', 'Ka']
target = 'flux_CH4'

# Handle Missing Values
imputer = SimpleImputer(strategy='mean')
merged_df[features] = imputer.fit_transform(merged_df[features])

# Add an interaction term between 'VWC' and 'Ka'
merged_df['VWC_Ka_interaction'] = merged_df['VWC'] * merged_df['Ka']
X = merged_df[['VWC', 'Ka', 'VWC_Ka_interaction']]  # Updated feature set with interaction term
y = merged_df[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the Gradient Boosting model with scaled data for comparison
gb_model = GradientBoostingRegressor(n_estimators=200, max_depth=3, random_state=42)
gb_model.fit(X_train_scaled, y_train)

# Make predictions and evaluate Gradient Boosting
y_pred_gb = gb_model.predict(X_test_scaled)
mse_gb = mean_squared_error(y_test, y_pred_gb)
r2_gb = r2_score(y_test, y_pred_gb)

print(f"Mean Squared Error with Gradient Boosting (Scaled): {mse_gb}")
print(f"R-squared with Gradient Boosting (Scaled): {r2_gb}")

# Train the XGBoost model with scaled data
xgb_model = XGBRegressor(n_estimators=200, max_depth=3, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train_scaled, y_train)

# Make predictions and evaluate XGBoost
y_pred_xgb = xgb_model.predict(X_test_scaled)
mse_xgb = mean_squared_error(y_test, y_pred_xgb)
r2_xgb = r2_score(y_test, y_pred_xgb)

print(f"Mean Squared Error with XGBoost: {mse_xgb}")
print(f"R-squared with XGBoost: {r2_xgb}")

# Example prediction with new data (using the XGBoost model)
new_data = pd.DataFrame({'VWC': [60], 'Ka': [40], 'VWC_Ka_interaction': [60 * 40]})
new_data_scaled = scaler.transform(new_data)  # Scale new data using the same scaler

predicted_flux_xgb = xgb_model.predict(new_data_scaled)
print(f"Predicted CH4 Flux for new data using XGBoost with Interaction: {predicted_flux_xgb}")
