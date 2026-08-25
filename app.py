import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import textwrap

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)



# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

</style>
""", unsafe_allow_html=True)