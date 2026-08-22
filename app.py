import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ---------------------------------------------------------
   GLOBAL
--------------------------------------------------------- */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F5F7FB;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Remove Streamlit top spacing */
[data-testid="stHeader"] {
    background: transparent;
}

/* ---------------------------------------------------------
   SIDEBAR
--------------------------------------------------------- */

section[data-testid="stSidebar"] {
    background: #0B1424;
    border-right: 1px solid #1E293B;
}

section[data-testid="stSidebar"] > div {
    padding: 1.5rem 1rem;
}

/* Sidebar brand */
.brand-box {
    padding: 12px 8px 25px 8px;
}

.brand-mark {
    font-size: 25px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.5px;
}

.brand-sub {
    color: #94A3B8;
    font-size: 12px;
    margin-top: 6px;
    font-weight: 500;
}

/* Sidebar headings */
.sidebar-section-title {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* ---------------------------------------------------------
   SIDEBAR NAV BUTTONS
--------------------------------------------------------- */

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 42px;
    border-radius: 9px;
    border: 1px solid transparent;
    background: transparent;
    color: #CBD5E1 !important;
    font-size: 13px;
    font-weight: 600;
    text-align: left;
    padding: 9px 13px;
    transition: all 0.2s ease;
    box-shadow: none;
}

section[data-testid="stSidebar"] .stButton > button p {
    color: #CBD5E1 !important;
    font-weight: 600;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #172338;
    border-color: #263752;
    color: #FFFFFF !important;
    transform: translateX(2px);
}

section[data-testid="stSidebar"] .stButton > button:hover p {
    color: #FFFFFF !important;
}

/* ---------------------------------------------------------
   QUICK ACTION BUTTONS
--------------------------------------------------------- */

.quick-action {
    margin-top: 5px;
}

section[data-testid="stSidebar"] .quick-btn .stButton > button {
    background: #172033 !important;
    border: 1px solid #334155 !important;
    color: #E2E8F0 !important;
}

section[data-testid="stSidebar"] .quick-btn .stButton > button p {
    color: #E2E8F0 !important;
}

section[data-testid="stSidebar"] .quick-btn .stButton > button:hover {
    background: #24324A !important;
    border-color: #4F8CFF !important;
}

section[data-testid="stSidebar"] .quick-btn .stButton > button:hover p {
    color: #FFFFFF !important;
}

/* ---------------------------------------------------------
   SIDEBAR MODEL CARD
--------------------------------------------------------- */

.model-card {
    background: #111D31;
    border: 1px solid #23324A;
    border-radius: 12px;
    padding: 14px;
    margin-top: 25px;
}

.model-title {
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
}

.model-value {
    color: #60A5FA;
    font-size: 22px;
    font-weight: 800;
    margin-top: 6px;
}

.model-label {
    color: #64748B;
    font-size: 10px;
    margin-top: 3px;
}

/* ---------------------------------------------------------
   MAIN HEADER
--------------------------------------------------------- */

.hero {
    background: linear-gradient(135deg, #0F172A 0%, #172554 100%);
    border-radius: 18px;
    padding: 28px 32px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(15,23,42,0.12);
}

.hero-eyebrow {
    color: #93C5FD;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 7px;
}

.hero-title {
    color: #FFFFFF;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -1px;
    margin: 0;
}

.hero-subtitle {
    color: #CBD5E1;
    font-size: 14px;
    margin-top: 8px;
}

.status-pill {
    display: inline-block;
    margin-top: 15px;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(34,197,94,0.12);
    color: #86EFAC;
    font-size: 11px;
    font-weight: 700;
}

/* ---------------------------------------------------------
   SECTION HEADINGS
--------------------------------------------------------- */

.section-title {
    font-size: 21px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.4px;
    margin-top: 25px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748B;
    font-size: 12px;
    margin-bottom: 16px;
}

/* ---------------------------------------------------------
   KPI CARDS
--------------------------------------------------------- */

.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 3px 12px rgba(15,23,42,0.04);
}

.kpi-label {
    color: #64748B;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.kpi-value {
    color: #0F172A;
    font-size: 28px;
    font-weight: 800;
    margin-top: 9px;
}

.kpi-note {
    color: #94A3B8;
    font-size: 10px;
    margin-top: 5px;
}

/* ---------------------------------------------------------
   CONTENT CARDS
--------------------------------------------------------- */

.content-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 3px 12px rgba(15,23,42,0.035);
}

/* ---------------------------------------------------------
   INSIGHT CARD
--------------------------------------------------------- */

.insight-card {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 14px;
    padding: 20px 22px;
    margin-top: 15px;
}

.insight-title {
    color: #1D4ED8;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 7px;
}

.insight-text {
    color: #334155;
    font-size: 13px;
    line-height: 1.7;
}

/* ---------------------------------------------------------
   RISK BADGES
--------------------------------------------------------- */

.risk-critical {
    display: inline-block;
    background: #FEF2F2;
    color: #DC2626;
    border: 1px solid #FECACA;
    border-radius: 999px;
    padding: 6px 11px;
    font-size: 11px;
    font-weight: 700;
}

.risk-high {
    display: inline-block;
    background: #FFF7ED;
    color: #EA580C;
    border: 1px solid #FED7AA;
    border-radius: 999px;
    padding: 6px 11px;
    font-size: 11px;
    font-weight: 700;
}

.risk-medium {
    display: inline-block;
    background: #FEFCE8;
    color: #CA8A04;
    border: 1px solid #FEF08A;
    border-radius: 999px;
    padding: 6px 11px;
    font-size: 11px;
    font-weight: 700;
}

.risk-low {
    display: inline-block;
    background: #F0FDF4;
    color: #16A34A;
    border: 1px solid #BBF7D0;
    border-radius: 999px;
    padding: 6px 11px;
    font-size: 11px;
    font-weight: 700;
}

/* ---------------------------------------------------------
   CUSTOMER PROFILE
--------------------------------------------------------- */

.profile-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 24px;
    margin-top: 15px;
}

.profile-title {
    color: #0F172A;
    font-size: 22px;
    font-weight: 800;
}

.profile-subtitle {
    color: #64748B;
    font-size: 12px;
    margin-top: 5px;
}

/* ---------------------------------------------------------
   FOOTER
--------------------------------------------------------- */

.footer {
    text-align: center;
    color: #94A3B8;
    font-size: 10px;
    padding: 35px 0 10px 0;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    file_names = [
        "telco_churn_powerbi.csv",
        "telco_churn.csv",
        "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    ]

    for file in file_names:
        try:
            df = pd.read_csv(file)
            return df
        except:
            pass

    return None


df = load_data()

if df is None:
    st.error(
        "Dataset not found. Upload `telco_churn_powerbi.csv` "
        "to the same GitHub repository as app.py."
    )
    st.stop()

# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip()

# Remove duplicate columns
df = df.loc[:, ~df.columns.duplicated()]

# ------------------------------------------------------------
# COLUMN HELPERS
# ------------------------------------------------------------

def find_column(possible_names):

    for name in possible_names:
        if name in df.columns:
            return name

    return None


customer_col = find_column([
    "customerID",
    "CustomerID",
    "customer_id",
    "Customer Id"
])

contract_col = find_column([
    "Contract",
    "contract"
])

tenure_col = find_column([
    "tenure",
    "Tenure"
])

monthly_col = find_column([
    "MonthlyCharges",
    "monthly_charges",
    "Monthly Charges",
    "AvgMonthlySpend"
])

total_col = find_column([
    "TotalCharges",
    "total_charges",
    "Total Charges"
])

churn_col = find_column([
    "Churn",
    "churn"
])

segment_col = find_column([
    "CustomerSegment",
    "Customer Segment",
    "Segment",
    "Segment Name"
])

risk_col = find_column([
    "RiskLevel",
    "Risk Level",
    "Risk",
    "risk_level"
])

prob_col = find_column([
    "ChurnProbability",
    "Churn Probability",
    "ChurnProb",
    "PredictedProbability",
    "ModelRisk",
    "model_risk"
])

# ============================================================
# DATA CLEANING
# ============================================================

if total_col:
    df[total_col] = pd.to_numeric(
        df[total_col].astype(str).str.strip(),
        errors="coerce"
    )

if monthly_col:
    df[monthly_col] = pd.to_numeric(
        df[monthly_col],
        errors="coerce"
    )

if tenure_col:
    df[tenure_col] = pd.to_numeric(
        df[tenure_col],
        errors="coerce"
    )

# ============================================================
# CREATE CHURN FLAG
# ============================================================

if churn_col:

    df["ChurnFlag"] = (
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
    df["ChurnFlag"] = 0

# ============================================================
# CREATE RISK PROBABILITY
# ============================================================

if prob_col:

    df["RiskProbability"] = pd.to_numeric(
        df[prob_col],
        errors="coerce"
    )

    # Convert percentage to decimal if required
    if df["RiskProbability"].max() > 1:
        df["RiskProbability"] = df["RiskProbability"] / 100

else:

    # If model probability isn't available,
    # use churn status as fallback
    df["RiskProbability"] = df["ChurnFlag"].astype(float)

# ============================================================
# CREATE RISK LEVEL
# ============================================================

def calculate_risk(x):

    if x >= 0.70:
        return "Critical"

    elif x >= 0.50:
        return "High"

    elif x >= 0.35:
        return "Medium"

    else:
        return "Low"


if risk_col:

    df["RiskLevelFinal"] = df[risk_col].astype(str)

else:

    df["RiskLevelFinal"] = df["RiskProbability"].apply(
        calculate_risk
    )

# ============================================================
# CREATE SEGMENT NAMES
# ============================================================

if segment_col:

    # Keep original segment
    df["SegmentID"] = df[segment_col]

else:

    df["SegmentID"] = "Unknown"

# Convert numeric segments into professional names
segment_names = {
    0: "Emerging Customers",
    1: "Loyal High-Value",
    2: "Loyal Low-Cost",
    3: "High-Risk New Customers"
}

def get_segment_name(value):

    try:
        number = int(float(value))

        if number in segment_names:
            return segment_names[number]

    except:
        pass

    return str(value)


df["SegmentNameFinal"] = df["SegmentID"].apply(
    get_segment_name
)

# ============================================================
# KPIs
# ============================================================

total_customers = len(df)

churn_rate = (
    df["ChurnFlag"].mean() * 100
    if len(df) > 0 else 0
)

at_risk = int(
    (df["RiskProbability"] >= 0.35).sum()
)

high_critical = int(
    (df["RiskLevelFinal"].astype(str)
     .str.lower()
     .isin(["high", "critical"]))
    .sum()
)

avg_model_risk = (
    df["RiskProbability"].mean() * 100
    if len(df) > 0 else 0
)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Executive Overview"

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="brand-box">
        <div class="brand-mark">◆ Customer Intelligence</div>
        <div class="brand-sub">AI-Powered Retention Analytics</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section-title">WORKSPACE</div>',
        unsafe_allow_html=True
    )

    # Navigation buttons

    nav_items = [
        ("▣  Executive Overview", "Executive Overview"),
        ("◉  Risk Analytics", "Risk Analytics"),
        ("○  Customer Segments", "Customer Segments"),
        ("✦  Churn Drivers", "Churn Drivers"),
        ("⌕  Customer Explorer", "Customer Explorer")
    ]

    for label, page_name in nav_items:

        if st.button(
            label,
            key="nav_" + page_name,
            use_container_width=True
        ):
            st.session_state.page = page_name
            st.rerun()

    # --------------------------------------------------------
    # QUICK ACTIONS
    # --------------------------------------------------------

    st.markdown(
        '<div class="sidebar-section-title">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="quick-btn">', unsafe_allow_html=True)

    if st.button(
        "⚠  High-Risk Customers",
        key="high_risk_btn",
        use_container_width=True
    ):
        st.session_state.page = "Risk Analytics"
        st.rerun()

    if st.button(
        "↻  Reset Workspace",
        key="reset_btn",
        use_container_width=True
    ):
        st.session_state.page = "Executive Overview"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # MODEL CARD
    # --------------------------------------------------------

    st.markdown("""
    <div class="model-card">
        <div class="model-title">XGBoost Classifier</div>
        <div class="model-value">0.841</div>
        <div class="model-label">ROC-AUC</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        margin-top:22px;
        padding:10px 4px;
        color:#64748B;
        font-size:10px;
        line-height:1.8;
    ">
        <b style="color:#CBD5E1;">Customer Churn Intelligence</b><br>
        Data Science Portfolio Project<br><br>
        EDA • Segmentation • XGBoost • SHAP
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-eyebrow">
        CUSTOMER ANALYTICS PLATFORM
    </div>

    <div class="hero-title">
        Customer Churn Intelligence
    </div>

    <div class="hero-subtitle">
        Retention command center for proactive customer management,
        churn risk analysis and data-driven decision making.
    </div>

    <div class="status-pill">
        ● MODEL ONLINE
    </div>

</div>
""", unsafe_allow_html=True)

# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if st.session_state.page == "Executive Overview":

    st.markdown(
        '<div class="section-title">Executive Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'High-level view of customer retention and churn risk.'
        '</div>',
        unsafe_allow_html=True
    )

    # KPI ROW

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Customers</div>
            <div class="kpi-value">{total_customers:,}</div>
            <div class="kpi-note">Active customer base</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Churn Rate</div>
            <div class="kpi-value">{churn_rate:.1f}%</div>
            <div class="kpi-note">Historical churn</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">At-Risk Customers</div>
            <div class="kpi-value">{at_risk:,}</div>
            <div class="kpi-note">Risk probability ≥ 35%</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">High / Critical</div>
            <div class="kpi-value">{high_critical:,}</div>
            <div class="kpi-note">Priority customers</div>
        </div>
        """, unsafe_allow_html=True)

    with k5:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg Model Risk</div>
            <div class="kpi-value">{avg_model_risk:.1f}%</div>
            <div class="kpi-note">Predicted probability</div>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # CHARTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        risk_counts = (
            df["RiskLevelFinal"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Medium", "Low"],
                fill_value=0
            )
            .reset_index()
        )

        risk_counts.columns = ["Risk Level", "Customers"]

        fig = px.bar(
            risk_counts,
            x="Risk Level",
            y="Customers",
            text="Customers",
            title="Customer Risk Distribution"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            height=390,
            margin=dict(l=20, r=20, t=55, b=20),
            plot_bgcolor="white",
            paper_bgcolor="white",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        if contract_col and churn_col:

            contract_churn = (
                df.groupby(contract_col)["ChurnFlag"]
                .mean()
                .reset_index()
            )

            contract_churn["Churn Rate"] = (
                contract_churn["ChurnFlag"] * 100
            )

            fig2 = px.bar(
                contract_churn,
                x=contract_col,
                y="Churn Rate",
                text="Churn Rate",
                title="Churn Rate by Contract"
            )

            fig2.update_traces(
                texttemplate="%{text:.1f}%",
                textposition="outside"
            )

            fig2.update_layout(
                height=390,
                margin=dict(l=20, r=20, t=55, b=20),
                plot_bgcolor="white",
                paper_bgcolor="white",
                showlegend=False
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

    # --------------------------------------------------------
    # INSIGHT
    # --------------------------------------------------------

    st.markdown("""
    <div class="insight-card">

        <div class="insight-title">
            ◆ Executive Insight
        </div>

        <div class="insight-text">
            Customer churn analytics identifies high-risk customers,
            reveals behavioral patterns and helps prioritize proactive
            retention strategies. The dashboard combines descriptive
            analytics, customer segmentation and machine-learning outputs
            into one decision-support interface.
        </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PAGE 2 — RISK ANALYTICS
# ============================================================

elif st.session_state.page == "Risk Analytics":

    st.markdown(
        '<div class="section-title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Identify and prioritize customers requiring retention intervention.'
        '</div>',
        unsafe_allow_html=True
    )

    # Risk filter

    selected_risk = st.multiselect(
        "Filter Risk Level",
        ["Critical", "High", "Medium", "Low"],
        default=["Critical", "High"]
    )

    risk_df = df[
        df["RiskLevelFinal"].isin(selected_risk)
    ]

    st.metric(
        "Customers in Selected Risk Groups",
        f"{len(risk_df):,}"
    )

    # Risk distribution

    c1, c2 = st.columns(2)

    with c1:

        risk_counts = (
            df["RiskLevelFinal"]
            .value_counts()
            .reset_index()
        )

        risk_counts.columns = ["Risk Level", "Customers"]

        fig = px.pie(
            risk_counts,
            names="Risk Level",
            values="Customers",
            hole=0.55,
            title="Overall Risk Distribution"
        )

        fig.update_layout(
            height=400,
            margin=dict(t=60, l=10, r=10, b=10)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        if contract_col:

            temp = (
                risk_df.groupby(contract_col)
                .size()
                .reset_index(name="Customers")
            )

            fig = px.bar(
                temp,
                x=contract_col,
                y="Customers",
                text="Customers",
                title="High-Risk Customers by Contract"
            )

            fig.update_traces(
                textposition="outside"
            )

            fig.update_layout(
                height=400,
                margin=dict(t=60, l=20, r=20, b=20)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # Customer table

    st.markdown(
        '<div class="section-title">Priority Customer List</div>',
        unsafe_allow_html=True
    )

    display_cols = []

    for col in [
        customer_col,
        contract_col,
        tenure_col,
        monthly_col,
        total_col,
        "RiskProbability",
        "RiskLevelFinal"
    ]:

        if col and col in df.columns:
            display_cols.append(col)

    st.dataframe(
        risk_df[display_cols]
        .sort_values(
            "RiskProbability",
            ascending=False
        )
        .head(100),
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# PAGE 3 — CUSTOMER SEGMENTS
# ============================================================

elif st.session_state.page == "Customer Segments":

    st.markdown(
        '<div class="section-title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'K-Means customer groups based on behavioral and financial characteristics.'
        '</div>',
        unsafe_allow_html=True
    )

    segment_summary = (
        df.groupby("SegmentNameFinal")
        .agg(
            Customers=(df.columns[0], "size"),
            AvgRisk=("RiskProbability", "mean")
        )
        .reset_index()
    )

    segment_summary["AvgRisk"] *= 100

    c1, c2 = st.columns(2)

    with c1:

        fig = px.bar(
            segment_summary,
            x="SegmentNameFinal",
            y="Customers",
            text="Customers",
            title="Customers by Segment"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            height=430,
            xaxis_title="Segment",
            yaxis_title="Customers"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.bar(
            segment_summary,
            x="SegmentNameFinal",
            y="AvgRisk",
            text="AvgRisk",
            title="Average Risk by Segment"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(
            height=430,
            xaxis_title="Segment",
            yaxis_title="Average Risk (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Segment profile

    st.markdown(
        '<div class="section-title">Segment Profile</div>',
        unsafe_allow_html=True
    )

    profile_cols = []

    for col in [
        tenure_col,
        monthly_col,
        total_col,
        "RiskProbability"
    ]:

        if col:
            profile_cols.append(col)

    if profile_cols:

        profile = (
            df.groupby("SegmentNameFinal")[profile_cols]
            .mean()
            .reset_index()
        )

        if "RiskProbability" in profile.columns:
            profile["RiskProbability"] *= 100

        st.dataframe(
            profile.round(2),
            use_container_width=True,
            hide_index=True
        )

# ============================================================
# PAGE 4 — CHURN DRIVERS
# ============================================================

elif st.session_state.page == "Churn Drivers":

    st.markdown(
        '<div class="section-title">Churn Drivers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Key characteristics identified by the churn analysis and model.'
        '</div>',
        unsafe_allow_html=True
    )

    # Your SHAP results from the analysis
    shap_features = pd.DataFrame({
        "Feature": [
            "Two-year Contract",
            "Tenure",
            "Support Risk",
            "One-year Contract",
            "Fiber Optic Internet",
            "Average Monthly Spend",
            "Total Charges",
            "Electronic Check",
            "Monthly Charges",
            "Paperless Billing",
            "Multiple Lines",
            "Online Backup",
            "Streaming Movies",
            "Phone Service",
            "Streaming TV"
        ],
        "Importance": [
            0.520533,
            0.484566,
            0.395179,
            0.239302,
            0.231344,
            0.202580,
            0.192231,
            0.179241,
            0.176551,
            0.149952,
            0.102514,
            0.075721,
            0.063462,
            0.056377,
            0.055720
        ]
    })

    fig = px.bar(
        shap_features.head(10).sort_values("Importance"),
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance",
        title="Top Churn Drivers — SHAP Feature Importance"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=550,
        margin=dict(l=20, r=60, t=60, b=20),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Key findings

    st.markdown("""
    <div class="insight-card">

        <div class="insight-title">
            ◆ Key Findings
        </div>

        <div class="insight-text">

            <b>Contract type</b> is one of the strongest predictors
            of customer churn.<br><br>

            <b>Tenure</b> has a major relationship with retention,
            with newer customers generally requiring more attention.<br><br>

            <b>Support risk</b> is another important indicator of
            potential churn behavior.<br><br>

            <b>Fiber optic service, monthly spending and total charges</b>
            also contribute significantly to the model's churn predictions.

        </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PAGE 5 — CUSTOMER EXPLORER
# ============================================================

elif st.session_state.page == "Customer Explorer":

    st.markdown(
        '<div class="section-title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Search and inspect an individual customer profile.'
        '</div>',
        unsafe_allow_html=True
    )

    if customer_col:

        # ----------------------------------------------------
        # SEARCHABLE CUSTOMER DROPDOWN
        # ----------------------------------------------------

        customer_ids = (
            df[customer_col]
            .dropna()
            .astype(str)
            .sort_values()
            .unique()
            .tolist()
        )

        selected_customer = st.selectbox(
            "Search Customer ID",
            customer_ids,
            index=0,
            placeholder="Type to search customer..."
        )

        customer = df[
            df[customer_col].astype(str) == str(selected_customer)
        ]

        if len(customer) > 0:

            row = customer.iloc[0]

            risk = str(
                row.get(
                    "RiskLevelFinal",
                    "Unknown"
                )
            )

            # Risk badge

            risk_class = {
                "Critical": "risk-critical",
                "High": "risk-high",
                "Medium": "risk-medium",
                "Low": "risk-low"
            }.get(
                risk,
                "risk-low"
            )

            st.markdown(f"""
            <div class="profile-card">

                <div class="profile-title">
                    Customer {selected_customer}
                </div>

                <div class="profile-subtitle">
                    Individual customer risk profile
                </div>

                <div style="margin-top:15px;">
                    <span class="{risk_class}">
                        {risk} Risk
                    </span>
                </div>

            </div>
            """, unsafe_allow_html=True)

            # ------------------------------------------------
            # CUSTOMER PROFILE TABLE
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">Customer Profile</div>',
                unsafe_allow_html=True
            )

            profile_data = {}

            for label, col in [
                ("Customer ID", customer_col),
                ("Contract", contract_col),
                ("Tenure", tenure_col),
                ("Monthly Charges", monthly_col),
                ("Total Charges", total_col),
                ("Churn", churn_col),
                ("Customer Segment", "SegmentNameFinal"),
                ("Risk Level", "RiskLevelFinal")
            ]:

                if col and col in row.index:

                    value = row[col]

                    if pd.isna(value):
                        value = "N/A"

                    profile_data[label] = value

            profile_table = pd.DataFrame(
                list(profile_data.items()),
                columns=["Attribute", "Value"]
            )

            st.dataframe(
                profile_table,
                use_container_width=True,
                hide_index=True
            )

            # ------------------------------------------------
            # METRICS
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">Customer Metrics</div>',
                unsafe_allow_html=True
            )

            m1, m2, m3, m4 = st.columns(4)

            with m1:

                value = row[tenure_col] if tenure_col else 0

                st.metric(
                    "Tenure",
                    f"{value:.0f} months"
                    if isinstance(value, (int, float, np.number))
                    else str(value)
                )

            with m2:

                value = row[monthly_col] if monthly_col else 0

                st.metric(
                    "Monthly Charges",
                    f"${float(value):,.2f}"
                    if pd.notna(value)
                    else "N/A"
                )

            with m3:

                value = row[total_col] if total_col else 0

                st.metric(
                    "Total Charges",
                    f"${float(value):,.2f}"
                    if pd.notna(value)
                    else "N/A"
                )

            with m4:

                churn_value = row[churn_col] if churn_col else "N/A"

                st.metric(
                    "Churn",
                    str(churn_value)
                )

            # ------------------------------------------------
            # CUSTOMER RISK
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">Risk Assessment</div>',
                unsafe_allow_html=True
            )

            probability = row.get(
                "RiskProbability",
                0
            )

            probability = float(probability)

            st.progress(
                min(max(probability, 0), 1)
            )

            st.write(
                f"Estimated churn risk: **{probability * 100:.1f}%**"
            )

    else:

        st.warning(
            "Customer ID column was not found in the dataset."
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    Customer Churn Intelligence &nbsp; • &nbsp;
    Data Science Portfolio Project &nbsp; • &nbsp;
    EDA + Segmentation + XGBoost + SHAP
</div>
""", unsafe_allow_html=True)
