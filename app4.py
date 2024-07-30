import base64
import streamlit as st
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO

# Load sample data
df = px.data.iris()

# Function to convert image to base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to convert image from URL to base64
def get_placeholder_img_as_base64(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Replace this URL with the URL of your sidebar image
sidebar_img_url = "https://images.unsplash.com/photo-1530456740912-cf00df622fe8" # <-- Placeholder Image URL
sidebar_img = get_placeholder_img_as_base64(sidebar_img_url)

# Replace this URL with the URL of your background image
background_img_url = "https://perryhouseplans.com/wp-content/uploads/home-app-background.jpg" # <-- Placeholder Background Image URL

# Define the HTML styles
page_bg_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        .main {{
            background-image: url("{background_img_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white; /* Ensures text is readable */
        }}

        .sidebar {{
            background-image: url("data:image/jpeg;base64,{sidebar_img}");
            background-position: center; 
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
</head>
<body>
    <div class="main">
        <div class="sidebar">
            <!-- Sidebar content goes here -->
        </div>
        <div class="content">
            <!-- Main content goes here -->
        </div>
    </div>
</body>
</html>
"""

# Apply custom HTML styles
st.markdown(page_bg_html, unsafe_allow_html=True)

# Title and Sidebar
st.title("House Price Prediction App")
st.sidebar.header("Configuration")

# Container 1
with st.container():
    st.header("Introduction")
    st.markdown(
        "Welcome to the House Price Prediction app! Use the sidebar to configure your inputs and get predictions."
    )
    st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))

# Container 2
with st.container():
    st.header("Data Visualization")
    st.markdown(
        "Explore various data visualizations to better understand the dataset."
    )
    st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))

# Container 3
with st.container():
    st.header("Additional Insights")
    st.markdown(
        "Get additional insights and predictions based on the provided data."
    )
    st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))

# Container 4
with st.container():
    st.header("Conclusion")
    st.markdown(
        "Thank you for using the House Price Prediction app. We hope you find it useful!"
    )
    st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))
