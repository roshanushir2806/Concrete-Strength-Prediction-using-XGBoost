

Concrete Strength Prediction using XGBoost

A simple and interactive Streamlit web application that predicts the compressive strength of concrete using an XGBoost Regression Model trained on the widely used Yeh Concrete dataset.

🔗 Live App:
https://concrete-strength-prediction-using-xgboost-jirjvaxzf99pqsm3hfc.streamlit.app/


---

📌 Project Overview

This project demonstrates how machine learning—specifically XGBoost Regression—can be used to predict concrete compressive strength based on its ingredients.
The application allows users to input concrete mix values and instantly receive a predicted strength value (MPa).


---

🚀 Features

Interactive Streamlit UI

Input fields for:

Cement

Blast Furnace Slag

Fly Ash

Water

Superplasticizer

Coarse Aggregate

Fine Aggregate

Age (days)


Trained XGBoost ML model

Real-time strength prediction

Simple and clean interface

Model loaded using pickle



---

🧠 Machine Learning Model

Algorithm: XGBoost Regressor

Dataset: Yeh Concrete Strength Dataset

Steps performed:

Data cleaning

Scaling (Min-Max Scaling)

Train-test split

Model training

Hyperparameter tuning (optional)

Saving model as .pkl




---

📂 Project Structure

├── app.py                     # Streamlit app
├── model.pkl                  # Saved XGBoost model
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
└── (optional) notebook.ipynb  # Training notebook


---
