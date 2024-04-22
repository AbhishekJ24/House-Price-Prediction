# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cJPKo6RZjSmOQnEC6E6M6EkvO_R37WvL
"""

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
import numpy as np

df = pd.read_csv("/Users/gamingspectrum24/Documents/University Coursework/6th Semester/Application of ML in Industries/Lab/House-Price-Prediction/Data/train.csv")
# Selecting relevant columns
features = ['OverallQual', 'GrLivArea', 'YearBuilt', 'LotArea', 'TotalBsmtSF', 'SalePrice']
df_selected = df[features]

X = df_selected.drop('SalePrice', axis=1)
y = df_selected['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Lasso Regression
lasso_model = Lasso()
lasso_model.fit(X_train, y_train)

# Ridge Regression
ridge_model = Ridge()
ridge_model.fit(X_train, y_train)

# Random Forest Regression
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)

def predict_price(model, inputs):
    input_data = np.array(inputs).reshape(1, -1)
    return model.predict(input_data)[0]

st.title('House Price Prediction App')

# Input components for user input
overall_qual = st.slider('Overall Quality', min_value=1, max_value=10, value=5)
grliv_area = st.number_input('GrLivArea', min_value=0, step=1)
year_built = st.number_input('Year Built', min_value=1800, step=1)
lot_area = st.number_input('Lot Area', min_value=0, step=1)
total_bsmt_sf = st.number_input('Total Bsmt SF', min_value=0, step=1)

# Predictions
lr_prediction = predict_price(lr_model, [overall_qual, grliv_area, year_built, lot_area, total_bsmt_sf])
lasso_prediction = predict_price(lasso_model, [overall_qual, grliv_area, year_built, lot_area, total_bsmt_sf])
ridge_prediction = predict_price(ridge_model, [overall_qual, grliv_area, year_built, lot_area, total_bsmt_sf])
rf_prediction = predict_price(rf_model, [overall_qual, grliv_area, year_built, lot_area, total_bsmt_sf])

# Display predictions
st.subheader('Predictions:')
st.write(f'Linear Regression Prediction: ${lr_prediction:.2f}')
st.write(f'Lasso Regression Prediction: ${lasso_prediction:.2f}')
st.write(f'Ridge Regression Prediction: ${ridge_prediction:.2f}')
st.write(f'Random Forest Regression Prediction: ${rf_prediction:.2f}')