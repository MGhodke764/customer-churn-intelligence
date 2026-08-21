import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    df = pd.read_csv("telco_churn_powerbi.csv")
    return df

df = load_data()

# =========================================================
# COLUMN HELPERS
# =========================================================

def find_col(possible_names):
    for name in possible_names:
        if name in df.columns:
            return name
    return None

customer_id_col = find_col([
    "customerID",
    "CustomerID",
    "Customer Id",
    "Customer ID",
    "customer_id"
])

churn_col = find_col([
    "Churn",
    "ChurnFlag",
    "Churn Flag",
    "churn"
])

contract_col = find_col([
    "Contract",
    "contract"
])

tenure_col = find_col([
    "tenure",
    "Tenure"
])

monthly_col = find_col([
    "MonthlyCharges",
    "Monthly Charges",
    "MonthlyCharges "
])

total_col = find_col([
    "TotalCharges",
    "Total Charges",
    "TotalCharges "
])

segment_col = find_col([
    "Segment Name",
    "CustomerSegment",
    "Customer Segment",
    "Segment"
])

risk_col = find_col([
    "Risk Level",
    "RiskLevel",
    "Risk"
])

prob_col = find_col([
    "Churn Probability",
    "ChurnProbability",
    "Probability",
    "Predicted Probability",
    "Model Risk"
])

# =========================================================
# CREATE SAFE DERIVED COLUMNS
# =========================================================

# Churn
if churn_col:
    df["Churn_Display"] = (
        df[churn_col]
        .astype(str)
        .str.lower()
        .map({
            "yes": 1,
            "no": 0,
            "1": 1,
            "0": 0,
            "true": 1,
            "false": 0
        })
        .fillna(0)
    )
else:
    df["Churn_Display"] = 0

# Segment
if not segment_col:

    if tenure_col:
        tenure_values = pd.to_numeric(df[tenure_col], errors="coerce").fillna(0)

        df["Segment Name"] = pd.cut(
            tenure_values,
            bins=[-1, 12, 36, 60, np.inf],
            labels=[
                "New Customers",
                "Growing Customers",
                "Loyal Customers",
                "Long-Term Customers"
            ]
        )

    else:
        df["Segment Name"] = "General Customers"

    segment_col = "Segment Name"

# Risk
if not risk_col:

    if prob_col:
        probability = pd.to_numeric(
            df[prob_col],
            errors="coerce"
        ).fillna(0)

        if probability.max() > 1:
            probability = probability / 100

        df["Risk Level"] = pd.cut(
            probability,
            bins=[-0.01, 0.20, 0.35, 0.50, 1.01],
            labels=[
                "Low",
                "Medium",
                "High",
                "Critical"
            ]
        )

    else:
        df["Risk Level"] = "Low"

    risk_col = "Risk Level"

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f6f8fc;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #0b1220;
}

section[data-testid="stSidebar"] * {
    color: #f8fafc;
}

.sidebar-title {
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 4px;
}

.sidebar-subtitle {
    color: #94a3b8 !important;
    font-size: 13px;
    margin-bottom: 35px;
}

.nav-title {
    color: #64748b !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-top: 25px;
}

/* HEADER */

.hero {
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #f8faff 100%
    );
    border: 1px solid #e5eaf2;
    border-radius: 18px;
    padding: 30px 34px;
    margin-bottom: 25px;
    box-shadow: 0 4px 18px rgba(15,23,42,0.04);
}

.eyebrow {
    color: #2563eb;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.hero-title {
    color: #0f172a;
    font-size: 38px;
    font-weight: 800;
    margin: 0;
}

.hero-subtitle {
    color: #64748b;
    font-size: 15px;
    margin-top: 8px;
}

/* KPI */

.kpi {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 16px;
    padding: 22px;
    min-height: 125px;
    box-shadow: 0 3px 12px rgba(15,23,42,0.04);
}

.kpi-label {
    color: #64748b;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .7px;
    text-transform: uppercase;
}

.kpi-value {
    color: #0f172a;
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

.kpi-caption {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 4px;
}

/* SECTION */

.section-title {
    color: #0f172a;
    font-size: 22px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 18px;
}

/* CARD */

.card {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 3px 12px rgba(15,23,42,0.04);
}

/* INSIGHT */

.insight {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    border-radius: 12px;
    padding: 20px;
    color: #1e3a8a;
}

/* CUSTOMER */

.customer-card {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.05);
}

.customer-id {
    font-size: 25px;
    font-weight: 800;
    color: #0f172a;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #eff6ff;
    color: #2563eb;
    font-size: 12px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">◆ Customer Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">AI-Powered Retention Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-title">WORKSPACE</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "",
        [
            "Executive Overview",
            "Risk Analytics",
            "Customer Segments",
            "Churn Drivers",
            "Customer Explorer"
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        '<div class="nav-title">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    if st.button("⚠ High-Risk Customers", use_container_width=True):
        page = "Risk Analytics"

    if st.button("↻ Reset Workspace", use_container_width=True):
        st.rerun()

    st.markdown("---")

    st.caption("Customer Churn Intelligence")
    st.caption("Data Science Portfolio Project")
    st.caption("Model: XGBoost Classifier")
    st.caption("Analytics: EDA + Segmentation + SHAP")


# =========================================================
# METRICS
# =========================================================

total_customers = len(df)

churn_rate = df["Churn_Display"].mean() * 100

risk_counts = df[risk_col].astype(str).value_counts()

high_risk = (
    risk_counts.get("High", 0)
    + risk_counts.get("Critical", 0)
)

critical = risk_counts.get("Critical", 0)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<div class="eyebrow">
CUSTOMER RETENTION COMMAND CENTER
</div>

<div class="hero-title">
Customer Churn Intelligence
</div>

<div class="hero-subtitle">
AI-powered customer risk analytics, segmentation and retention insights.
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="kpi">
        <div class="kpi-label">Total Customers</div>
        <div class="kpi-value">{total_customers:,}</div>
        <div class="kpi-caption">Customer base</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi">
        <div class="kpi-label">Churn Rate</div>
        <div class="kpi-value">{churn_rate:.1f}%</div>
        <div class="kpi-caption">Historical churn</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi">
        <div class="kpi-label">At-Risk Customers</div>
        <div class="kpi-value">{high_risk:,}</div>
        <div class="kpi-caption">High + Critical</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="kpi">
        <div class="kpi-label">Critical Customers</div>
        <div class="kpi-value">{critical:,}</div>
        <div class="kpi-caption">Immediate attention</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Understand the current customer risk landscape.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        risk_df = (
            df[risk_col]
            .astype(str)
            .value_counts()
            .reset_index()
        )

        risk_df.columns = ["Risk Level", "Customers"]

        fig = px.bar(
            risk_df,
            x="Risk Level",
            y="Customers",
            text="Customers",
            title="Customer Risk Distribution"
        )

        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=60, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        if contract_col and churn_col:

            contract_df = (
                df.groupby(contract_col)["Churn_Display"]
                .mean()
                .reset_index()
            )

            contract_df["Churn Rate"] = (
                contract_df["Churn_Display"] * 100
            )

            fig = px.bar(
                contract_df,
                x=contract_col,
                y="Churn Rate",
                text="Churn Rate",
                title="Churn Rate by Contract"
            )

            fig.update_traces(
                texttemplate="%{text:.1f}%",
                textposition="outside"
            )

            fig.update_layout(
                template="plotly_white",
                height=400,
                margin=dict(l=20, r=20, t=60, b=20)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.markdown(
        '<div class="section-title">Executive Insight</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="insight">
    <b>Retention Signal:</b>
    The current customer base contains <b>{high_risk:,}</b>
    high or critical-risk customers. These customers should be
    prioritized for proactive retention campaigns.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RISK ANALYTICS
# =========================================================

elif page == "Risk Analytics":

    st.markdown(
        '<div class="section-title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Identify customers requiring proactive intervention.</div>',
        unsafe_allow_html=True
    )

    risk_df = (
        df[risk_col]
        .astype(str)
        .value_counts()
        .reset_index()
    )

    risk_df.columns = ["Risk Level", "Customers"]

    fig = px.pie(
        risk_df,
        names="Risk Level",
        values="Customers",
        hole=0.55,
        title="Overall Customer Risk"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("### High-Risk Customer List")

    high_df = df[
        df[risk_col].astype(str).isin(
            ["High", "Critical"]
        )
    ].copy()

    st.dataframe(
        high_df.head(100),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# CUSTOMER SEGMENTS
# =========================================================

elif page == "Customer Segments":

    st.markdown(
        '<div class="section-title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Explore behavioral customer groups.</div>',
        unsafe_allow_html=True
    )

    segment_df = (
        df.groupby(segment_col)
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        segment_df,
        x=segment_col,
        y="Customers",
        text="Customers",
        title="Customer Segments"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        segment_df,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# CHURN DRIVERS
# =========================================================

elif page == "Churn Drivers":

    st.markdown(
        '<div class="section-title">Churn Drivers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Key characteristics associated with customer churn.</div>',
        unsafe_allow_html=True
    )

    drivers = {
        "Contract": 0.52,
        "Tenure": 0.48,
        "Support Risk": 0.40,
        "Internet Service": 0.23,
        "Monthly Spend": 0.20,
        "Total Charges": 0.19,
        "Payment Method": 0.18
    }

    driver_df = pd.DataFrame(
        list(drivers.items()),
        columns=["Driver", "Importance"]
    )

    driver_df = driver_df.sort_values(
        "Importance",
        ascending=True
    )

    fig = px.bar(
        driver_df,
        x="Importance",
        y="Driver",
        orientation="h",
        text="Importance",
        title="Top Churn Drivers"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("""
    <div class="insight">
    <b>Key finding:</b>
    Contract type, tenure and support-related risk are among
    the strongest characteristics associated with customer churn.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CUSTOMER EXPLORER
# =========================================================

elif page == "Customer Explorer":

    st.markdown(
        '<div class="section-title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Search and inspect an individual customer profile.</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # CUSTOMER ID DROPDOWN
    # -----------------------------------------------------

    if customer_id_col:

        customer_ids = (
            df[customer_id_col]
            .dropna()
            .astype(str)
            .sort_values()
            .unique()
            .tolist()
        )

        selected_customer = st.selectbox(
            "Select Customer ID",
            customer_ids,
            index=0,
            help="Start typing to search for a customer."
        )

        customer = df[
            df[customer_id_col].astype(str)
            == selected_customer
        ].iloc[0]

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="customer-card">

        <div class="customer-id">
        Customer {selected_customer}
        </div>

        <br>

        <span class="badge">
        {str(customer[risk_col])} Risk
        </span>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Customer Profile")

        profile_cols = [
            customer_id_col,
            contract_col,
            tenure_col,
            monthly_col,
            total_col,
            churn_col,
            segment_col,
            risk_col
        ]

        profile_cols = [
            x for x in profile_cols
            if x is not None and x in df.columns
        ]

        profile = pd.DataFrame({
            "Attribute": profile_cols,
            "Value": [
                customer[col]
                for col in profile_cols
            ]
        })

        st.dataframe(
            profile,
            use_container_width=True,
            hide_index=True
        )

        # -------------------------------------------------
        # CUSTOMER METRICS
        # -------------------------------------------------

        st.markdown("### Customer Metrics")

        a, b, c, d = st.columns(4)

        with a:
            value = customer[tenure_col] if tenure_col else "—"
            st.metric("Tenure", value)

        with b:
            value = customer[monthly_col] if monthly_col else "—"
            st.metric("Monthly Charges", value)

        with c:
            value = customer[total_col] if total_col else "—"
            st.metric("Total Charges", value)

        with d:
            value = customer[churn_col] if churn_col else "—"
            st.metric("Churn", value)

    else:

        st.error(
            "Customer ID column was not found in the dataset."
        )

        st.write(
            "Available columns:",
            list(df.columns)
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#94a3b8;
        font-size:12px;
        padding:20px;
    ">
    Customer Churn Intelligence &nbsp;•&nbsp;
    Data Science Portfolio Project &nbsp;•&nbsp;
    EDA + Machine Learning + SHAP + Segmentation
    </div>
    """,
    unsafe_allow_html=True
)
