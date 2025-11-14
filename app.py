import streamlit as st

import pickle

import numpy as np



# ---------------------------

# Load model

# ---------------------------

with open("concrete_strength_model.pkl", "rb") as f:

    model = pickle.load(f)



# ---------------------------

# Page Config

# ---------------------------

st.set_page_config(page_title="Concrete Strength Predictor", layout="centered")



# ---------------------------

# Minimal CSS Styling

# ---------------------------

st.markdown("""

<style>



body {

    background-color: #f4f7fa;

}



h1 {

    text-align: center;

    color: #0d47a1;

    font-weight: 700;

}



label {

    font-weight: 600 !important;

}



.stButton>button {

    background-color: #0d47a1 !important;

    color: white !important;

    padding: 12px 20px !important;

    border-radius: 8px !important;

    font-size: 18px !important;

}



.stButton>button:hover {

    background-color: #002171 !important;

}



.result {

    background-color: #e3f2fd;

    padding: 12px 20px;

    border-radius: 8px;

    margin-top: 15px;

    font-size: 20px;

    font-weight: bold;

    color: #0d47a1;

    text-align: center;

}



.footer {

    text-align: center;

    margin-top: 40px;

    font-size: 14px;

    color: #555;

}



</style>

""", unsafe_allow_html=True)



# ---------------------------

# Title

# ---------------------------

st.markdown("<h1>🧱 Concrete Strength Prediction App</h1>", unsafe_allow_html=True)

st.write("<center>Enter concrete mix values to get strength prediction.</center>", unsafe_allow_html=True)



st.write("")



# ---------------------------

# Input Fields (No Cards)

# ---------------------------

col1, col2, col3 = st.columns(3)



with col1:

    cement = st.number_input("Cement (kg/m³)", min_value=0.0, step=0.1)

    slag = st.number_input("Slag (kg/m³)", min_value=0.0, step=0.1)



with col2:

    water = st.number_input("Water (kg/m³)", min_value=0.0, step=0.1)

    superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, step=0.1)



with col3:

    coarseaggregate = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, step=0.1)

    fineaggregate = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0, step=0.1)

    age = st.number_input("Age (days)", min_value=1, step=1)



# ---------------------------

# Prediction Button

# ---------------------------

if st.button("Predict Strength"):

    input_data = np.array([[cement, slag, water, superplasticizer,

                            coarseaggregate, fineaggregate, age]])



    prediction = model.predict(input_data)[0]



    st.markdown(f"<div class='result'>🏗️ Predicted Strength: {prediction:.2f} MPa</div>",

                unsafe_allow_html=True)



# ---------------------------

# Footer

# ---------------------------

st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
