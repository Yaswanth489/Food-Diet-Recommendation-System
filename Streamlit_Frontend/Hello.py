import streamlit as st

# Set page config
st.set_page_config(
    page_title="MAIN PROJECT",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Header with image
st.markdown("<h1 style='text-align: center; color: #FF5733;'>🌟 Welcome to Food Diet Recommendation System! 🌟</h1>", unsafe_allow_html=True)
st.write("---")

# Sidebar
st.sidebar.markdown("<h3 style='text-align: center; color: #FFFFFF; background-color: #212121; padding: 10px;'>Select a Recommendation App ☝️</h3>", unsafe_allow_html=True)

# Main content
st.markdown("<h2 style='color: #333333;text-align: center;'>About The Project</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='color: #333333;text-align: center;'>We have developed a food diet recommendation web application using a content-based approach with Scikit-Learn, FastAPI, and Streamlit.</h5>", unsafe_allow_html=True)
st.write("---")

st.image("image.png", width=600,use_column_width=True)

# Styling with CSS
st.markdown(
    """
    <style>
    /* Custom CSS for Streamlit components */
    /* Title */
    .stApp stContainer {
        background-color: #f4f4f4;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar */
    .sidebar-content {
        background-color: #212121; /* Set background color for sidebar (dark gray) */
        color: #FFFFFF; /* Set text color for sidebar (white) */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Main content */
    .main {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)
