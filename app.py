import numpy as np
import pickle
import streamlit as st

# Load the model and dictionaries
model = pickle.load(open('model.pkl', 'rb'))
index_dict = pickle.load(open('cat', 'rb'))
location_cat = pickle.load(open('location_cat', 'rb'))

def predict_price(location, area, sqft, bath, balcony, size):
    new_vector = np.zeros(151)

    # Process location
    if location not in location_cat:
        new_vector[146] = 1
    else:
        new_vector[index_dict[str(location)]] = 1

    # Process area
    new_vector[index_dict[str(area)]] = 1

    # Other features
    new_vector[0] = sqft
    new_vector[1] = bath
    new_vector[2] = balcony
    new_vector[3] = size

    # Make prediction
    new = [new_vector]
    prediction = model.predict(new)
    return prediction[0]

# Streamlit UI
st.title("House Price Prediction")

# Input fields
location = st.text_input("Location")
area = st.text_input("Area")
sqft = st.number_input("Square Feet", min_value=0)
bath = st.number_input("Number of Bathrooms", min_value=0)
balcony = st.number_input("Number of Balconies", min_value=0)
size = st.number_input("Size", min_value=0)

# Predict button
if st.button("Predict"):
    if location and area:
        prediction = predict_price(location, area, sqft, bath, balcony, size)
        st.write(f"Your house estimate price is ₹ {prediction} lakhs")
    else:
        st.error("Please provide all the required inputs.")
