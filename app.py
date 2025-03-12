import streamlit as st

# Set page title and configuration
st.set_page_config(
    page_title="Hello World App",
    page_icon="👋",
    layout="centered"
)

# Display title
st.title("Hello World!")

# Display welcome message
st.write("Welcome to my first Streamlit app!")

# Add a decorative element
st.balloons()