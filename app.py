import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


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
# PROFESSIONAL CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f6f8fc;
}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b1220;
    border-right: 1px solid #182238;
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

.sidebar-brand {
    padding: 12px 8px 28px 8px;
}

.sidebar-logo {
    font-size: 26px;
    font-weight: 800;
    color: white;
    letter-spacing: -1px;
}

.sidebar-subtitle {
    color: #8d9ab3;
    font-size: 13px;
    margin-top: 7px;
}

.sidebar-section {
    color: #68758e;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-top: 22px;
    margin-bottom: 10px;
}

/* Navigation buttons */
section[data-testid="stSidebar"] .stButton button {
    width: 100%;
    text-align: left;
    background: transparent;
    border: none;
    color: #cbd3e1;
    border-radius: 9px;
    padding: 10px 12px;
    font-size: 14px;
    font-weight: 500;
}

section[data-testid="stSidebar"] .stButton button:hover {
    background: #172238;
    color: white;
    border: none;
}

/* Quick action buttons */
section[data-testid="stSidebar"] .quick-high button {
    background: #182a45 !important;
    color: #7db7ff !important;
    border: 1px solid #29466d !important;
}

section[data-testid="stSidebar"] .quick-high button:hover {
    background: #213a5e !important;
    color: white !important;
}

section[data-testid="stSidebar"] .quick-reset button {
    background: #151f32 !important;
    color: #aeb9ca !important;
    border: 1px solid #27344a !important;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #0b1220 0%, #172442 100%);
    border-radius: 22px;
    padding: 34px 40px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.12);
}

.hero-eyebrow {
    color: #7db7ff;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 0;
}

.hero-subtitle {
    color: #aebbd0;
    font-size: 15px;
    margin-top: 10px;
}

.status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(34, 197, 94, 0.12);
    color: #7ee2a5;
    border: 1px solid rgba(34, 197, 94, 0.25);
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    margin-top: 20px;
}

/* Page headings */
.page-title {
    font-size: 27px;
    font-weight: 800;
    color: #101827;
    letter-spacing: -0.8px;
    margin-top: 8px;
    margin-bottom: 4px;
}

.page-subtitle {
    color: #718096;
    font-size: 14px;
    margin-bottom: 24px;
}

.section-title {
    font-size: 20px;
    font-weight: 800;
    color: #101827;
    margin-top: 28px;
    margin-bottom: 14px;
}

/* KPI Cards */
.kpi-card {
    background: white;
    border: 1px solid #e6eaf1;
    border-radius: 16px;
    padding: 20px;
    min-height: 145px;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
}

.kpi-label {
    color: #6b778c;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.7px;
    text-transform: uppercase;
}

.kpi-value {
    color: #101827;
    font-size: 29px;
    font-weight: 800;
    margin-top: 14px;
}

.kpi-desc {
    color: #9aa5b5;
    font-size: 11px;
    margin-top: 8px;
}

/* Cards */
.card {
    background: white;
    border: 1px solid #e6eaf1;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.035);
}

.card-title {
    font-size: 16px;
    font-weight: 750;
    color: #172033;
    margin-bottom: 5px;
}

.card-subtitle {
    color: #8994a7;
    font-size: 12px;
}

/* Insight box */
.insight {
    background: #eef6ff;
    border: 1px solid #cfe5ff;
    border-radius: 15px;
    padding: 20px 22px;
    margin-top: 18px;
}

.insight-title {
    color: #1259a7;
    font-size: 15px;
    font-weight: 800;
}

.insight-text {
    color: #425466;
    font-size: 13px;
    line-height: 1.7;
    margin-top: 7px;
}

/* Risk badges */
.badge-critical {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #fff0f0;
    color: #d93025;
    font-size: 12px;
    font-weight: 800;
}

.badge-high {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #fff6e8;
    color: #c56b00;
    font-size: 12px;
    font-weight: 800;
}

.badge-medium {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #fffbea;
    color: #9a7900;
    font-size: 12px;
    font-weight: 800;
}

.badge-low {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #edfaf3;
    color: #168447;
    font-size: 12px;
    font-weight: 800;
}

/* Customer profile */
.profile-card {
    background: white;
    border: 1px solid #e4e8ef;
    border-radius: 18px;
    padding: 26px;
    box-shadow: 0 5px 18px rgba(15,23,42,0.04);
}

.profile-title {
    font-size: 24px;
    font-weight: 800;
    color: #101827;
}

.metric-big {
    font-size: 28px;
    font-weight: 800;
    color: #101827;
}

.metric-label {
    color: #7a879a;
    font-size: 12px;
}

/* Footer */
.footer {
    text-align: center;
    color: #98a3b5;
    font-size: 11px;
    padding: 35px 0 10px;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    possible_files = [
        "telco_churn_powerbi.csv",
        "telco_churn.csv",
        "customer_churn.csv",
        "data.csv"
    ]

    file_path = None

    for file in possible_files:
        if Path(file).exists():
            file_path = file
            break

    if file_path is None:
        csv_files = list(Path(".").glob("*.csv"))

        if csv_files:
            file_path = csv_files[0]

    if file_path is None:
        return pd.DataFrame()

    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
    )

    return df


df = load_data()


# ============================================================
# STOP IF DATA NOT FOUND
# ============================================================

if df.empty:

    st.error(
        "Dataset not found. Upload `telco_churn_powerbi.csv` "
        "to the same GitHub repository as `app.py`."
    )

    st.stop()


# ============================================================
# COLUMN FINDER
# ============================================================

def find_column(possible_names):

    lower_map = {
        str(c).lower().replace("_", "").replace(" ", ""): c
        for c in df.columns
    }

    for name in possible_names:

        key = name.lower().replace("_", "").replace(" ", "")

        if key in lower_map:
            return lower_map[key]

    return None


customer_col = find_column([
    "customerID",
    "customer_id",
    "Customer ID"
])

contract_col = find_column([
    "Contract",
    "contract_type"
])

tenure_col = find_column([
    "tenure",
    "Tenure"
])

monthly_col = find_column([
    "MonthlyCharges",
    "monthly_charges",
    "AvgMonthlySpend"
])

total_col = find_column([
    "TotalCharges",
    "total_charges"
])

churn_col = find_column([
    "Churn",
    "churn_status"
])

risk_col = find_column([
    "RiskLevel",
    "risk_level"
])

segment_col = find_column([
    "Segment Name",
    "Segment_Name",
    "CustomerSegment",
    "Customer_Segment"
])

prob_col = find_column([
    "ChurnProbability",
    "churn_probability",
    "Probability",
    "PredictedProbability",
    "Churn_Probability"
])


# ============================================================
# STANDARDIZE IMPORTANT DATA
# ============================================================

if customer_col is None:

    df["customerID"] = [
        f"CUST-{i+1:04d}"
        for i in range(len(df))
    ]

    customer_col = "customerID"


if churn_col is None:

    df["Churn"] = "No"

    churn_col = "Churn"


# Numeric conversions

if tenure_col:
    df[tenure_col] = pd.to_numeric(
        df[tenure_col],
        errors="coerce"
    ).fillna(0)


if monthly_col:
    df[monthly_col] = pd.to_numeric(
        df[monthly_col],
        errors="coerce"
    ).fillna(0)


if total_col:
    df[total_col] = pd.to_numeric(
        df[total_col],
        errors="coerce"
    ).fillna(0)


# ============================================================
# CHURN STANDARDIZATION
# ============================================================

def churn_binary(value):

    value = str(value).strip().lower()

    if value in ["yes", "1", "true", "churned"]:
        return 1

    return 0


df["_churn_binary"] = df[churn_col].apply(churn_binary)


# ============================================================
# RISK PROBABILITY
# ============================================================

if prob_col:

    df["_risk_probability"] = pd.to_numeric(
        df[prob_col],
        errors="coerce"
    )

    # Convert 0-100 to 0-1
    if df["_risk_probability"].max() > 1:
        df["_risk_probability"] = (
            df["_risk_probability"] / 100
        )

else:

    # Build a reasonable fallback from available risk information
    if risk_col:

        risk_map = {
            "critical": 0.85,
            "high": 0.65,
            "medium": 0.45,
            "low": 0.15
        }

        df["_risk_probability"] = (
            df[risk_col]
            .astype(str)
            .str.lower()
            .map(risk_map)
            .fillna(df["_churn_binary"])
        )

    else:

        df["_risk_probability"] = df["_churn_binary"]


# ============================================================
# RISK LEVEL
# ============================================================

def get_risk_level(prob):

    if prob >= 0.75:
        return "Critical"

    elif prob >= 0.50:
        return "High"

    elif prob >= 0.35:
        return "Medium"

    return "Low"


df["_risk_level"] = df["_risk_probability"].apply(
    get_risk_level
)


# ============================================================
# CUSTOMER SEGMENT
# ============================================================

if segment_col is None:

    # Create segments using available business variables
    if monthly_col and tenure_col:

        def make_segment(row):

            spend = row[monthly_col]
            tenure = row[tenure_col]

            if spend >= df[monthly_col].quantile(0.70) and tenure >= df[tenure_col].median():
                return "High Value"

            elif tenure <= df[tenure_col].quantile(0.30):
                return "New Customers"

            elif spend < df[monthly_col].median():
                return "Budget Customers"

            return "Loyal Customers"

        df["_segment"] = df.apply(
            make_segment,
            axis=1
        )

    else:

        df["_segment"] = "General Customers"

else:

    # Handle numeric CustomerSegment
    if pd.api.types.is_numeric_dtype(df[segment_col]):

        segment_mapping = {
            1: "New Customers",
            2: "Loyal Customers",
            3: "High Value Customers",
            4: "At-Risk Customers"
        }

        df["_segment"] = (
            pd.to_numeric(df[segment_col], errors="coerce")
            .map(segment_mapping)
            .fillna("General Customers")
        )

    else:

        df["_segment"] = (
            df[segment_col]
            .astype(str)
            .replace("nan", "General Customers")
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-logo">◆ Customer Intelligence</div>
        <div class="sidebar-subtitle">
            AI-Powered Retention Analytics
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section">WORKSPACE</div>',
        unsafe_allow_html=True
    )

    if "page" not in st.session_state:
        st.session_state.page = "Executive Overview"

    pages = [
        ("▣", "Executive Overview"),
        ("◉", "Risk Analytics"),
        ("○", "Customer Segments"),
        ("✦", "Churn Drivers"),
        ("⌕", "Customer Explorer")
    ]

    for icon, page_name in pages:

        if st.button(
            f"{icon}  {page_name}",
            key=f"nav_{page_name}",
            use_container_width=True
        ):
            st.session_state.page = page_name

    st.markdown(
        '<div class="sidebar-section">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="quick-high">',
        unsafe_allow_html=True
    )

    if st.button(
        "⚠  High-Risk Customers",
        use_container_width=True
    ):
        st.session_state.page = "Risk Analytics"

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="quick-reset">',
        unsafe_allow_html=True
    )

    if st.button(
        "↻  Reset Workspace",
        use_container_width=True
    ):
        st.session_state.page = "Executive Overview"

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="color:#dbe3f0;font-size:12px;font-weight:700;">
        Customer Churn Intelligence
    </div>

    <div style="color:#78869c;font-size:11px;margin-top:7px;">
        Data Science Portfolio Project
    </div>

    <div style="color:#78869c;font-size:11px;margin-top:18px;">
        Model: XGBoost Classifier
    </div>

    <div style="color:#78869c;font-size:11px;margin-top:6px;">
        Analytics: EDA + Segmentation + SHAP
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HERO HEADER
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

    <div class="status">
        ● MODEL ONLINE
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

if st.session_state.page == "Executive Overview":

    st.markdown(
        '<div class="page-title">Executive Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'High-level view of customer retention, churn behavior and model risk.'
        '</div>',
        unsafe_allow_html=True
    )

    total_customers = len(df)

    churn_rate = df["_churn_binary"].mean() * 100

    at_risk = (df["_risk_probability"] >= 0.35).sum()

    high_critical = (
        df["_risk_level"]
        .isin(["High", "Critical"])
        .sum()
    )

    avg_risk = df["_risk_probability"].mean() * 100

    kpis = [
        ("TOTAL CUSTOMERS",
         f"{total_customers:,}",
         "Active customer base"),

        ("CHURN RATE",
         f"{churn_rate:.1f}%",
         "Historical churn"),

        ("AT-RISK CUSTOMERS",
         f"{at_risk:,}",
         "Risk probability ≥ 35%"),

        ("HIGH / CRITICAL",
         f"{high_critical:,}",
         "Priority customers"),

        ("AVG MODEL RISK",
         f"{avg_risk:.1f}%",
         "Predicted probability")
    ]

    cols = st.columns(5)

    for col, (label, value, desc) in zip(cols, kpis):

        with col:

            st.markdown(f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    {label}
                </div>

                <div class="kpi-value">
                    {value}
                </div>

                <div class="kpi-desc">
                    {desc}
                </div>

            </div>
            """, unsafe_allow_html=True)


    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)


    # Risk distribution
    with col1:

        risk_counts = (
            df["_risk_level"]
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
            category_orders={
                "Risk Level":
                ["Critical", "High", "Medium", "Low"]
            }
        )

        fig.update_traces(
            marker_color="#146dcc",
            textposition="outside"
        )

        fig.update_layout(
            title="Customer Risk Distribution",
            title_font_size=16,
            plot_bgcolor="white",
            paper_bgcolor="white",
            height=380,
            margin=dict(l=20, r=20, t=55, b=20),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Contract churn
    with col2:

        if contract_col:

            contract_churn = (
                df.groupby(contract_col)["_churn_binary"]
                .mean()
                .reset_index()
            )

            contract_churn["_churn_rate"] = (
                contract_churn["_churn_binary"] * 100
            )

            fig = px.bar(
                contract_churn,
                x=contract_col,
                y="_churn_rate",
                text="_churn_rate"
            )

            fig.update_traces(
                marker_color="#146dcc",
                texttemplate="%{text:.1f}%",
                textposition="outside"
            )

            fig.update_layout(
                title="Churn Rate by Contract",
                title_font_size=16,
                yaxis_title="Churn Rate (%)",
                plot_bgcolor="white",
                paper_bgcolor="white",
                height=380,
                margin=dict(l=20, r=20, t=55, b=20)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # Executive insight

    if contract_col:

        monthly_mask = (
            df[contract_col]
            .astype(str)
            .str.lower()
            .str.contains("month")
        )

        if monthly_mask.any():

            monthly_rate = (
                df.loc[monthly_mask, "_churn_binary"].mean() * 100
            )

            insight = (
                f"Customers on month-to-month contracts show a "
                f"{monthly_rate:.1f}% churn rate. "
                f"The ML system currently flags "
                f"{at_risk:,} customers as requiring proactive retention."
            )

        else:

            insight = (
                f"The model identifies {at_risk:,} customers "
                f"above the 35% operating risk threshold."
            )

    else:

        insight = (
            f"The model identifies {at_risk:,} customers "
            f"above the 35% operating risk threshold."
        )


    st.markdown(f"""
    <div class="insight">

        <div class="insight-title">
            ◆ Executive Insight
        </div>

        <div class="insight-text">
            {insight}
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# RISK ANALYTICS
# ============================================================

elif st.session_state.page == "Risk Analytics":

    st.markdown(
        '<div class="page-title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Analyze predicted churn probability and prioritize retention actions.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        critical = (
            df["_risk_level"] == "Critical"
        ).sum()

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">CRITICAL RISK</div>
            <div class="kpi-value">{critical:,}</div>
            <div class="kpi-desc">Probability ≥ 75%</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        high = (
            df["_risk_level"] == "High"
        ).sum()

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">HIGH RISK</div>
            <div class="kpi-value">{high:,}</div>
            <div class="kpi-desc">Probability 50–75%</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        medium = (
            df["_risk_level"] == "Medium"
        ).sum()

        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">MEDIUM RISK</div>
            <div class="kpi-value">{medium:,}</div>
            <div class="kpi-desc">Probability 35–50%</div>
        </div>
        """, unsafe_allow_html=True)


    st.markdown(
        '<div class="section-title">Risk Probability Distribution</div>',
        unsafe_allow_html=True
    )

    fig = px.histogram(
        df,
        x="_risk_probability",
        nbins=25
    )

    fig.update_traces(
        marker_color="#146dcc"
    )

    fig.add_vline(
        x=0.35,
        line_dash="dash",
        line_color="#d93025",
        annotation_text="35% Threshold"
    )

    fig.update_layout(
        xaxis_title="Predicted Churn Probability",
        yaxis_title="Customers",
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=430
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.markdown(
        '<div class="section-title">Highest Risk Customers</div>',
        unsafe_allow_html=True
    )

    display_cols = [customer_col]

    if contract_col:
        display_cols.append(contract_col)

    if tenure_col:
        display_cols.append(tenure_col)

    if monthly_col:
        display_cols.append(monthly_col)

    display_cols += ["_risk_probability", "_risk_level"]

    risk_table = (
        df.sort_values(
            "_risk_probability",
            ascending=False
        )[display_cols]
        .head(15)
        .copy()
    )

    risk_table.columns = [
        "Customer ID",
        *[
            str(c).replace("_", " ")
            for c in risk_table.columns[1:]
        ]
    ]

    if " _risk_probability" in risk_table.columns:
        pass

    st.dataframe(
        risk_table,
        use_container_width=True,
        hide_index=True
    )


    st.info(
        "Model operating point: 35% probability threshold | "
        "XGBoost ROC-AUC: 0.841"
    )


# ============================================================
# CUSTOMER SEGMENTS
# ============================================================

elif st.session_state.page == "Customer Segments":

    st.markdown(
        '<div class="page-title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Understand customer groups based on behavior, tenure and value.'
        '</div>',
        unsafe_allow_html=True
    )


    segment_summary = (
        df.groupby("_segment")
        .agg(
            Customers=(customer_col, "count"),
            Avg_Risk=("_risk_probability", "mean"),
            Churn_Rate=("_churn_binary", "mean")
        )
        .reset_index()
    )

    segment_summary["Avg_Risk"] *= 100
    segment_summary["Churn_Rate"] *= 100

    segment_summary.columns = [
        "Segment",
        "Customers",
        "Avg Risk (%)",
        "Churn Rate (%)"
    ]


    col1, col2 = st.columns(2)


    with col1:

        fig = px.bar(
            segment_summary,
            x="Segment",
            y="Customers",
            text="Customers"
        )

        fig.update_traces(
            marker_color="#146dcc",
            textposition="outside"
        )

        fig.update_layout(
            title="Customers by Segment",
            plot_bgcolor="white",
            paper_bgcolor="white",
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:

        fig = px.bar(
            segment_summary,
            x="Segment",
            y="Churn Rate (%)",
            text="Churn Rate (%)"
        )

        fig.update_traces(
            marker_color="#0d8a5f",
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(
            title="Churn Rate by Segment",
            plot_bgcolor="white",
            paper_bgcolor="white",
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.markdown(
        '<div class="section-title">Segment Performance</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        segment_summary.round(2),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CHURN DRIVERS
# ============================================================

elif st.session_state.page == "Churn Drivers":

    st.markdown(
        '<div class="page-title">Churn Drivers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Key factors influencing customer churn according to the ML analysis.'
        '</div>',
        unsafe_allow_html=True
    )


    # Your actual SHAP ranking
    shap_features = [
        ("Contract — Two year", 0.520533),
        ("Tenure", 0.484566),
        ("Support Risk", 0.395179),
        ("Contract — One year", 0.239302),
        ("Internet Service — Fiber optic", 0.231344),
        ("Average Monthly Spend", 0.202580),
        ("Total Charges", 0.192231),
        ("Payment Method — Electronic check", 0.179241),
        ("Monthly Charges", 0.176551),
        ("Paperless Billing", 0.149952),
        ("Multiple Lines", 0.102514),
        ("Online Backup", 0.075721),
        ("Streaming Movies", 0.063462),
        ("Phone Service", 0.056377),
        ("Streaming TV", 0.055720)
    ]

    shap_df = pd.DataFrame(
        shap_features,
        columns=["Feature", "Importance"]
    )


    fig = px.bar(
        shap_df.sort_values("Importance"),
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance"
    )

    fig.update_traces(
        marker_color="#146dcc",
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        title="Top 15 Factors Influencing Customer Churn",
        xaxis_title="Mean Absolute SHAP Value",
        yaxis_title="",
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=650,
        margin=dict(l=20, r=60, t=60, b=30)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.markdown("""
    <div class="insight">

        <div class="insight-title">
            ◆ Model Interpretation
        </div>

        <div class="insight-text">
            Contract type, customer tenure and support-related risk
            are among the strongest factors influencing the model's
            churn predictions. These variables can be used to prioritize
            retention campaigns and customer outreach.
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CUSTOMER EXPLORER
# ============================================================

elif st.session_state.page == "Customer Explorer":

    st.markdown(
        '<div class="page-title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Search and inspect individual customer profiles and retention risk.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # CUSTOMER DROPDOWN
    # ========================================================

    customer_ids = (
        df[customer_col]
        .astype(str)
        .dropna()
        .unique()
        .tolist()
    )

    customer_ids = sorted(customer_ids)


    selected_customer = st.selectbox(
        "Select Customer ID",
        customer_ids,
        index=0
    )


    customer = df[
        df[customer_col].astype(str) == selected_customer
    ].iloc[0]


    risk_probability = float(
        customer["_risk_probability"]
    )

    risk_level = customer["_risk_level"]


    # Risk badge

    badge_class = {
        "Critical": "badge-critical",
        "High": "badge-high",
        "Medium": "badge-medium",
        "Low": "badge-low"
    }.get(
        risk_level,
        "badge-low"
    )


    st.markdown(f"""
    <div class="profile-card">

        <div class="profile-title">
            Customer {selected_customer}
        </div>

        <div style="margin-top:14px;">
            <span class="{badge_class}">
                {risk_level} Risk
            </span>
        </div>

    </div>
    """, unsafe_allow_html=True)


    # ========================================================
    # PROFILE TABLE
    # ========================================================

    st.markdown(
        '<div class="section-title">Customer Profile</div>',
        unsafe_allow_html=True
    )


    profile_data = []


    profile_data.append(
        ["Customer ID", selected_customer]
    )


    if contract_col:
        profile_data.append(
            ["Contract", customer[contract_col]]
        )


    if tenure_col:
        profile_data.append(
            ["Tenure", customer[tenure_col]]
        )


    if monthly_col:
        profile_data.append(
            ["Monthly Charges", customer[monthly_col]]
        )


    if total_col:
        profile_data.append(
            ["Total Charges", customer[total_col]]
        )


    profile_data.append(
        ["Churn", customer[churn_col]]
    )


    profile_data.append(
        ["Customer Segment", customer["_segment"]]
    )


    profile_data.append(
        ["Risk Level", risk_level]
    )


    profile_df = pd.DataFrame(
        profile_data,
        columns=["Attribute", "Value"]
    )


    st.dataframe(
        profile_df,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # CUSTOMER METRICS
    # ========================================================

    st.markdown(
        '<div class="section-title">Customer Metrics</div>',
        unsafe_allow_html=True
    )


    metric_cols = st.columns(4)


    with metric_cols[0]:

        tenure_value = (
            customer[tenure_col]
            if tenure_col else "—"
        )

        st.metric(
            "Tenure",
            f"{tenure_value}"
        )


    with metric_cols[1]:

        monthly_value = (
            customer[monthly_col]
            if monthly_col else 0
        )

        st.metric(
            "Monthly Charges",
            f"${float(monthly_value):,.2f}"
        )


    with metric_cols[2]:

        total_value = (
            customer[total_col]
            if total_col else 0
        )

        st.metric(
            "Total Charges",
            f"${float(total_value):,.2f}"
        )


    with metric_cols[3]:

        st.metric(
            "Predicted Risk",
            f"{risk_probability * 100:.1f}%"
        )


    # ========================================================
    # RISK GAUGE
    # ========================================================

    st.markdown(
        '<div class="section-title">Customer Churn Risk</div>',
        unsafe_allow_html=True
    )


    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=risk_probability * 100,
            number={
                "suffix": "%"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "bar": {
                    "color": "#146dcc"
                },
                "steps": [
                    {
                        "range": [0, 35],
                        "color": "#e9f7ef"
                    },
                    {
                        "range": [35, 50],
                        "color": "#fff8df"
                    },
                    {
                        "range": [50, 75],
                        "color": "#fff0df"
                    },
                    {
                        "range": [75, 100],
                        "color": "#ffe8e8"
                    }
                ],
                "threshold": {
                    "line": {
                        "color": "#d93025",
                        "width": 4
                    },
                    "value": 35
                }
            }
        )
    )


    gauge.update_layout(
        height=330,
        margin=dict(l=30, r=30, t=40, b=10),
        paper_bgcolor="white"
    )


    st.plotly_chart(
        gauge,
        use_container_width=True
    )


    # ========================================================
    # RECOMMENDATION
    # ========================================================

    if risk_level == "Critical":

        recommendation = (
            "Immediate retention intervention recommended. "
            "Prioritize this customer for proactive outreach, "
            "personalized offers and service recovery."
        )

    elif risk_level == "High":

        recommendation = (
            "High churn risk detected. Consider targeted retention "
            "offers and proactive customer engagement."
        )

    elif risk_level == "Medium":

        recommendation = (
            "Monitor customer behavior and consider preventive "
            "retention communication."
        )

    else:

        recommendation = (
            "Customer currently shows relatively low churn risk. "
            "Maintain normal engagement and monitor future changes."
        )


    st.markdown(f"""
    <div class="insight">

        <div class="insight-title">
            ◆ Recommended Action
        </div>

        <div class="insight-text">
            {recommendation}
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    Customer Churn Intelligence &nbsp;•&nbsp;
    Data Science Portfolio Project &nbsp;•&nbsp;
    EDA + Machine Learning + SHAP + Segmentation
</div>
""", unsafe_allow_html=True)
