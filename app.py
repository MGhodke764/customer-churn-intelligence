%%writefile app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv("telco_churn_powerbi.csv")

# -----------------------------
# Title
# -----------------------------

st.title("📊 Customer Churn Intelligence Platform")
st.caption("AI-Powered Customer Risk & Retention Analytics")

st.divider()

# -----------------------------
# KPI Calculations
# -----------------------------

total_customers = df["customerID"].nunique()

churned_customers = df[
    df["ChurnFlag"] == 1
]["customerID"].nunique()

churn_rate = churned_customers / total_customers

high_risk_customers = df[
    df["RiskLevel"].isin(["High", "Critical"])
]["customerID"].nunique()

avg_churn_probability = df[
    "ChurnProbability"
].mean()

# -----------------------------
# KPI Cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Churn Rate",
    f"{churn_rate:.1%}"
)

col3.metric(
    "High/Critical Risk",
    f"{high_risk_customers:,}"
)

col4.metric(
    "Avg Churn Probability",
    f"{avg_churn_probability:.1%}"
)

st.divider()

# -----------------------------
# Risk Distribution
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Customer Risk Distribution")

    risk_counts = (
        df["RiskLevel"]
        .value_counts()
        .reset_index()
    )

    risk_counts.columns = [
        "RiskLevel",
        "Customers"
    ]

    fig = px.bar(
        risk_counts,
        x="RiskLevel",
        y="Customers",
        title="Customers by Risk Level"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Churn by Contract")

    contract_churn = (
        df.groupby("Contract")["ChurnFlag"]
        .mean()
        .reset_index()
    )

    contract_churn["ChurnRate"] = (
        contract_churn["ChurnFlag"] * 100
    )

    fig = px.bar(
        contract_churn,
        x="Contract",
        y="ChurnRate",
        title="Churn Rate by Contract Type",
        labels={
            "ChurnRate": "Churn Rate (%)"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Customer Segmentation
# -----------------------------

st.divider()

st.subheader("👥 Customer Segmentation")

segment_data = (
    df.groupby("Segment Name")
    .agg(
        Customers=("customerID", "count"),
        AvgTenure=("tenure", "mean"),
        AvgMonthlyCharges=("MonthlyCharges", "mean"),
        ChurnRate=("ChurnFlag", "mean")
    )
    .reset_index()
)

segment_data["ChurnRate"] *= 100

st.dataframe(
    segment_data.round(2),
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Churn Drivers
# -----------------------------

st.divider()

st.subheader("🧠 Top Churn Drivers")

try:

    importance = pd.read_csv(
        "shap_feature_importance.csv"
    )

    importance = importance.sort_values(
        "MeanAbsSHAP",
        ascending=True
    ).tail(10)

    fig = px.bar(
        importance,
        x="MeanAbsSHAP",
        y="Feature",
        orientation="h",
        title="Top Factors Influencing Churn"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except Exception:

    st.info(
        "SHAP feature importance file not found."
    )

# -----------------------------
# Customer Risk Explorer
# -----------------------------

st.divider()

st.subheader("🔎 Customer Risk Explorer")

customer_id = st.selectbox(
    "Select Customer",
    df["customerID"].tolist()
)

customer = df[
    df["customerID"] == customer_id
].iloc[0]

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Churn Probability",
        f"{customer['ChurnProbabilityPct']:.1f}%"
    )

with col2:

    st.metric(
        "Risk Level",
        customer["RiskLevel"]
    )

with col3:

    st.metric(
        "Monthly Charges",
        f"${customer['MonthlyCharges']:.2f}"
    )

st.write(
    f"**Contract:** {customer['Contract']}"
)

st.write(
    f"**Tenure:** {customer['tenure']} months"
)

st.write(
    f"**Internet Service:** {customer['InternetService']}"
)

st.write(
    f"**Customer Segment:** {customer['Segment Name']}"
)

st.success(
    f"💡 Recommended Action: "
    f"{customer['RetentionRecommendation']}"
)

# -----------------------------
# At-Risk Customers
# -----------------------------

st.divider()

st.subheader("🚨 Highest-Risk Customers")

risk_customers = df[
    df["ChurnProbability"] >= 0.35
].sort_values(
    "ChurnProbability",
    ascending=False
)

display_columns = [
    "customerID",
    "Contract",
    "tenure",
    "MonthlyCharges",
    "ChurnProbabilityPct",
    "RiskLevel",
    "RetentionRecommendation"
]

st.dataframe(
    risk_customers[display_columns].head(50),
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Customers with churn probability ≥ 35% are classified as At Risk."
)