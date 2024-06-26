# -*- coding: utf-8 -*-
"""Serverless_PMUs_E2EE_XGBoost.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RlqlGEPEk1TWyU9Jtc9u6u_ec2peY3Z5
"""

import xgboost as xgb
import pandas as pd

# Define the dataset
data = {
    'Invocation': [100, 200, 150, 120, 180, 170, 140, 210, 160, 190, 200, 150, 130, 180, 160, 120, 200, 170, 150, 180],
    'Memory_Used': [256, 128, 512, 256, 128, 512, 256, 128, 512, 256, 128, 512, 256, 128, 512, 256, 128, 512, 256, 128],
    'Duration': [250, 150, 300, 200, 175, 320, 280, 180, 310, 290, 160, 305, 210, 170, 300, 200, 160, 320, 250, 170],
    'CPU_Utilization': [50, 75, 60, 45, 70, 65, 55, 75, 60, 50, 75, 60, 45, 70, 60, 50, 75, 65, 55, 70],
    'Network_Latency': [5, 8, 10, 7, 9, 6, 7, 10, 5, 9, 8, 10, 6, 9, 8, 5, 8, 6, 7, 9],
    'Breach_Attempts': [50, 60, 55, 40, 45, 48, 55, 60, 50, 45, 60, 55, 50, 45, 50, 50, 60, 50, 55, 45],
    'Successful_Breaches': [17, 21, 19, 15, 16, 18, 19, 21, 18, 16, 20, 18, 16, 14, 15, 14, 17, 12, 13, 10]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define features and target
X = df[['Invocation', 'Memory_Used', 'Duration', 'CPU_Utilization', 'Network_Latency', 'Breach_Attempts']]
y = df['Successful_Breaches']

# Initialize and train XGBoost model
model = xgb.XGBRegressor(objective='reg:squarederror')
model.fit(X, y)

# Simulate new conditions after security measures (assume a 70% reduction in successful breaches)
df['Successful_Breaches_Secured'] = df['Successful_Breaches'] * 0.30

# Define new target
y_secured = df['Successful_Breaches_Secured']

# Evaluate the results
predictions = model.predict(X)
predictions_secured = model.predict(X) * 0.30

# Print results
print("Initial Successful Breaches Predictions:", predictions)
print("Post-Security Successful Breaches Predictions:", predictions_secured)