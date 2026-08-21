import streamlit as st

st.set_page_config(
    page_title="Test",
    layout="wide"
)

st.title("Customer Churn Intelligence")

st.write("If you can see this normally, Python is working.")

st.markdown(
    """
    <div style="
        background:#2563EB;
        color:white;
        padding:20px;
        border-radius:12px;
        font-size:24px;
        font-weight:bold;
    ">
        TEST DASHBOARD
    </div>
    """,
    unsafe_allow_html=True
)
