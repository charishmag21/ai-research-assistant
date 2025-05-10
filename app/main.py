# # streamlit_app.py
# import streamlit as st
# import sys
# import os

# Add the root project directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from pipelines.main_pipeline import run_pipeline

# Page configuration
st.set_page_config(page_title="AI Research Assistant", layout="wide")

# Title & description
st.title("🤖 AI Research Assistant")
st.markdown("Ask your university-related questions like *'What is the co-op eligibility at Northeastern Toronto?'*")

# Input box
query = st.text_input("Enter your query:", placeholder="e.g., What is Northeastern Toronto co-op eligibility")

# Button and processing
if st.button("Run Research"):
    if not query.strip():
        st.warning("Please enter a question before submitting.")
    else:
        with st.spinner("🔍 Running pipeline for: " + query):
            try:
                result = run_pipeline(query)
                st.markdown(result, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
