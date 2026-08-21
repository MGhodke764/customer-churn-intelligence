import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

/* ---------- GLOBAL ---------- */

.stApp {
    background: #f5f7fb;
    color: #172033;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1324 0%, #111d33 100%);
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

.sidebar-brand {
    padding: 10px 8px 25px 8px;
}

.sidebar-brand-title {
    color: white;
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -0.6px;
}

.sidebar-brand-sub {
    color: #9eabc2;
    font-size: 13px;
    margin-top: 7px;
}

.sidebar-section {
    color: #7f8da8;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* ---------- HEADINGS ---------- */

.main-title {
    font-size: 42px;
    font-weight: 850;
    letter-spacing: -1.5px;
    color: #101828;
    margin-bottom: 4px;
}

.main-subtitle {
    color: #667085;
    font-size: 15px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 25px;
    font-weight: 800;
    color: #101828;
    margin-top: 30px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #667085;
    font-size: 14px;
    margin-bottom: 18px;
}

/* ---------- HERO ---------- */

.hero {
    background: linear-gradient(135deg, #111c35 0%, #172b52 100%);
    border-radius: 22px;
    padding: 32px 36px;
    margin-bottom: 28px;
    box-shadow: 0 12px 35px rgba(16, 24, 40, 0.15);
}

.hero-eyebrow {
    color: #7dd3fc;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.hero-title {
    color: white;
    font-size: 36px;
    font-weight: 850;
    letter-spacing: -1px;
}

.hero-text {
    color: #b9c5d8;
    font-size: 14px;
    max-width: 800px;
    margin-top: 8px;
}

.online-pill {
    display: inline-block;
    background: rgba(34, 197, 94, 0.14);
    color: #4ade80;
    padding: 7px 13px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    margin-top: 18px;
}

/* ---------- KPI CARDS ---------- */

.kpi-card {
    background: white;
    border: 1px solid #e6eaf0;
    border-radius: 17px;
    padding: 21px;
    min-height: 125px;
    box-shadow: 0 5px 18px rgba(16, 24, 40, 0.05);
}

.kpi-label {
    color: #667085;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.7px;
    text-transform: uppercase;
}

.kpi-value {
    color: #101828;
    font-size: 30px;
    font-weight: 850;
    margin-top: 8px;
}

.kpi-note {
    color: #98a2b3;
    font-size: 12px;
    margin-top: 4px;
}

/* ---------- CONTENT CARDS ---------- */

.card {
    background: white;
    border: 1px solid #e6eaf0;
    border-radius: 17px;
    padding: 22px;
    box-shadow: 0 5px 18px rgba(16, 24, 40, 0.04);
}

.insight-card {
    background: linear-gradient(135deg, #eef6ff, #f7fbff);
    border: 1px solid #d8e9ff;
    border-radius: 17px;
    padding: 22px;
    margin-top: 20px;
}

.insight-title {
    font-size: 16px;
    font-weight: 800;
    color: #1459a6;
    margin-bottom: 7px;
}

.insight-text {
    font-size: 14px;
    color: #475467;
    line-height: 1.6;
}

/* ---------- STATUS ---------- */

.status-critical {
    display: inline-block;
    background: #fff0f0;
    color: #c62828;
    border-radius: 20px;
    padding: 7px 13px;
    font-weight: 800;
    font-size: 12px;
}

.status-high {
    display: inline-block;
    background: #fff5e8;
    color: #b45309;
    border-radius: 20px;
    padding: 7px 13px;
    font-weight: 800;
    font-size: 12px;
}

.status-medium {
    display: inline-block;
    background: #fffbe6;
    color: #9a6700;
    border-radius: 20px;
    padding: 7px 13px;
    font-weight: 800;
    font-size: 12px;
}

.status-low {
    display: inline-block;
    background: #ecfdf3;
    color: #15803d;
    border-radius: 20px;
    padding: 7px 13px;
    font-weight: 800;
    font-size: 12px;
}

/* ---------- TABLE ---------- */

.dataframe {
    border-radius: 12px;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    border-radius: 10px;
    border: 1px solid #d0d5dd;
    font-weight: 700;
    min-height: 42px;
}

.stButton > button:hover {
    border-color: #1677ff;
    color: #1677ff;
}

/* ---------- SELECTBOX ---------- */

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

/* ---------- FOOTER ---------- */

.footer {
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid #e4e7ec;
    text-align: center;
    color: #98a2b3;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():

    possible_files = [
        "telco_churn_powerbi.csv",
        "customer_churn.csv",
        "WA_Fn-UseC_-Telco-Customer-Churn.csv",
        "telco_churn.csv",
        "data.csv"
    ]

    for file in possible_files:
        try:
            df = pd.read_csv(file)
            if len(df) > 0:
                return df
        except:
            pass

    return pd.DataFrame()


df = load_data()

if df.empty:
    st.error(
        "Dataset not found. Make sure `telco_churn_powerbi.csv` "
        "is uploaded to the same GitHub repository as app.py."
    )
    st.stop()


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)

# Remove duplicate columns
df = df.loc[:, ~df.columns.duplicated()]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def find_col(names):

    lower_map = {str(c).lower().strip(): c for c in df.columns}

    for name in names:
        if name.lower() in lower_map:
            return lower_map[name.lower()]

    return None


def numeric_col(names):

    col = find_col(names)

    if col is None:
        return None

    converted = pd.to_numeric(df[col], errors="coerce")

    if converted.notna().sum() > 0:
        return converted

    return None


# ============================================================
# IDENTIFY IMPORTANT COLUMNS
# ============================================================

customer_id_col = find_col([
    "customerID",
    "customerId",
    "CustomerID",
    "Customer Id",
    "customer_id"
])

churn_col = find_col([
    "Churn",
    "churn",
    "Exited",
    "Churn Status"
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
    "AvgMonthlySpend",
    "avg_monthly_spend"
])

total_col = find_col([
    "TotalCharges",
    "Total Charges",
    "TotalChargesAmount"
])

internet_col = find_col([
    "InternetService",
    "Internet Service"
])

payment_col = find_col([
    "PaymentMethod",
    "Payment Method"
])


# ============================================================
# STANDARDIZE NUMERIC VALUES
# ============================================================

if tenure_col:
    df["_tenure"] = pd.to_numeric(df[tenure_col], errors="coerce").fillna(0)
else:
    df["_tenure"] = 0


if monthly_col:
    df["_monthly"] = pd.to_numeric(
        df[monthly_col], errors="coerce"
    ).fillna(0)
else:
    df["_monthly"] = 0


if total_col:
    df["_total"] = pd.to_numeric(
        df[total_col], errors="coerce"
    ).fillna(0)
else:
    df["_total"] = df["_monthly"] * df["_tenure"]


# ============================================================
# CHURN STANDARDIZATION
# ============================================================

if churn_col:

    churn_values = (
        df[churn_col]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["_churn"] = churn_values.map({
        "yes": 1,
        "y": 1,
        "true": 1,
        "1": 1,
        "churned": 1,
        "no": 0,
        "n": 0,
        "false": 0,
        "0": 0,
        "stayed": 0
    }).fillna(0)

else:
    df["_churn"] = 0


# ============================================================
# RISK SCORE
# ============================================================

# Build a robust risk score without assuming unavailable columns.

risk = np.zeros(len(df))


# Month-to-month contracts increase risk
if contract_col:

    contract_text = (
        df[contract_col]
        .astype(str)
        .str.lower()
    )

    risk += np.where(
        contract_text.str.contains("month"),
        0.30,
        0
    )


# Short tenure increases risk
risk += np.where(
    df["_tenure"] < 12,
    0.20,
    0
)

risk += np.where(
    df["_tenure"] < 6,
    0.15,
    0
)


# High monthly charges
monthly_threshold = df["_monthly"].quantile(0.75)

risk += np.where(
    df["_monthly"] > monthly_threshold,
    0.15,
    0
)


# Fiber optic
if internet_col:

    internet_text = (
        df[internet_col]
        .astype(str)
        .str.lower()
    )

    risk += np.where(
        internet_text.str.contains("fiber"),
        0.10,
        0
    )


# Electronic check
if payment_col:

    payment_text = (
        df[payment_col]
        .astype(str)
        .str.lower()
    )

    risk += np.where(
        payment_text.str.contains("electronic"),
        0.10,
        0
    )


# Historical churn
risk += df["_churn"] * 0.25

df["_risk_score"] = np.clip(risk, 0, 1)


# ============================================================
# RISK LEVEL
# ============================================================

def risk_label(x):

    if x >= 0.70:
        return "Critical"
    elif x >= 0.50:
        return "High"
    elif x >= 0.35:
        return "Medium"
    return "Low"


df["_risk_level"] = df["_risk_score"].apply(risk_label)


# ============================================================
# CUSTOMER SEGMENT
# ============================================================

def segment_customer(row):

    tenure = row["_tenure"]
    monthly = row["_monthly"]
    risk_score = row["_risk_score"]

    if risk_score >= 0.70:
        return "At-Risk"

    if tenure < 12 and monthly >= df["_monthly"].median():
        return "New & Valuable"

    if tenure >= 36 and risk_score < 0.35:
        return "Loyal"

    if monthly < df["_monthly"].median():
        return "Budget"

    return "Regular"


df["_segment"] = df.apply(segment_customer, axis=1)


# ============================================================
# SHAP IMPORTANCE
# Based on the user's supplied SHAP results
# ============================================================

shap_data = pd.DataFrame({
    "Feature": [
        "Two-year Contract",
        "Tenure",
        "Support Risk",
        "One-year Contract",
        "Fiber Optic",
        "Avg Monthly Spend",
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


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-title">◆ Customer Intelligence</div>
        <div class="sidebar-brand-sub">
            AI-Powered Retention Analytics
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section">WORKSPACE</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
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
        '<div class="sidebar-section">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    if st.button("⚠ High-Risk Customers", use_container_width=True):
        st.session_state["quick_action"] = "high_risk"
        page = "Risk Analytics"

    if st.button("↻ Reset Workspace", use_container_width=True):
        st.session_state.clear()
        st.rerun()

    st.markdown("---")

    st.markdown("""
    <div style="color:#ffffff;font-weight:800;font-size:13px;">
        Customer Churn Intelligence
    </div>

    <div style="color:#98a2b3;font-size:12px;margin-top:8px;">
        Data Science Portfolio Project
    </div>

    <div style="color:#98a2b3;font-size:12px;margin-top:12px;">
        Model: XGBoost Classifier
    </div>

    <div style="color:#98a2b3;font-size:12px;margin-top:5px;">
        Analytics: EDA + Segmentation + SHAP
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# COMMON METRICS
# ============================================================

total_customers = len(df)

churn_rate = df["_churn"].mean() * 100

at_risk = int((df["_risk_score"] >= 0.35).sum())

high_critical = int(
    df["_risk_level"].isin(["High", "Critical"]).sum()
)

avg_risk = df["_risk_score"].mean() * 100


# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    st.markdown(
        '<div class="main-title">Customer Churn Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Executive command center for customer retention, churn behavior and risk analysis.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">
        <div class="hero-eyebrow">CUSTOMER ANALYTICS PLATFORM</div>
        <div class="hero-title">Retention Command Center</div>
        <div class="hero-text">
            Monitor customer churn, identify high-risk accounts,
            understand churn drivers and prioritize retention actions.
        </div>
        <div class="online-pill">● ANALYTICS ONLINE</div>
    </div>
    """, unsafe_allow_html=True)

    # KPIs

    cols = st.columns(5)

    metrics = [
        ("TOTAL CUSTOMERS", f"{total_customers:,}", "Active customer base"),
        ("CHURN RATE", f"{churn_rate:.1f}%", "Historical churn"),
        ("AT-RISK CUSTOMERS", f"{at_risk:,}", "Risk score ≥ 35%"),
        ("HIGH / CRITICAL", f"{high_critical:,}", "Priority customers"),
        ("AVG MODEL RISK", f"{avg_risk:.1f}%", "Estimated risk")
    ]

    for col, (label, value, note) in zip(cols, metrics):

        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value">{value}</div>
                    <div class="kpi-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Customer distribution and contract-level churn patterns.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

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
            title="Customer Risk Distribution"
        )

        fig.update_layout(
            template="plotly_white",
            height=400,
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        if contract_col:

            contract_churn = (
                df.groupby(contract_col)["_churn"]
                .mean()
                .mul(100)
                .reset_index()
            )

            contract_churn.columns = [
                "Contract",
                "Churn Rate"
            ]

            fig = px.bar(
                contract_churn,
                x="Contract",
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
                showlegend=False
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.info("Contract information is not available.")

    # Insight

    if contract_col:

        month_contract = df[
            df[contract_col]
            .astype(str)
            .str.lower()
            .str.contains("month")
        ]

        if len(month_contract) > 0:
            month_rate = month_contract["_churn"].mean() * 100

            st.markdown(
                f"""
                <div class="insight-card">
                    <div class="insight-title">
                        ◆ Executive Insight
                    </div>
                    <div class="insight-text">
                        Month-to-month customers show a churn rate of
                        <b>{month_rate:.1f}%</b>.
                        These customers should be prioritized for proactive
                        retention campaigns and contract conversion offers.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# PAGE 2 — RISK ANALYTICS
# ============================================================

elif page == "Risk Analytics":

    st.markdown(
        '<div class="main-title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Identify customers requiring immediate retention attention.'
        '</div>',
        unsafe_allow_html=True
    )

    # Quick action filter

    risk_filter = st.selectbox(
        "Risk Level",
        ["All", "Critical", "High", "Medium", "Low"]
    )

    risk_df = df.copy()

    if risk_filter != "All":
        risk_df = risk_df[
            risk_df["_risk_level"] == risk_filter
        ]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Customers in View",
            f"{len(risk_df):,}"
        )

    with c2:
        st.metric(
            "Average Risk",
            f"{risk_df['_risk_score'].mean()*100:.1f}%"
        )

    with c3:
        st.metric(
            "Historical Churn",
            f"{risk_df['_churn'].mean()*100:.1f}%"
        )

    st.markdown(
        '<div class="section-title">Risk Distribution</div>',
        unsafe_allow_html=True
    )

    fig = px.histogram(
        df,
        x="_risk_score",
        nbins=20,
        title="Customer Risk Score Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=400,
        xaxis_title="Risk Score",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # High risk customers

    st.markdown(
        '<div class="section-title">Priority Customers</div>',
        unsafe_allow_html=True
    )

    display_cols = []

    if customer_id_col:
        display_cols.append(customer_id_col)

    if contract_col:
        display_cols.append(contract_col)

    if tenure_col:
        display_cols.append(tenure_col)

    if monthly_col:
        display_cols.append(monthly_col)

    if churn_col:
        display_cols.append(churn_col)

    display_cols += [
        "_risk_score",
        "_risk_level",
        "_segment"
    ]

    display_cols = [
        c for c in display_cols
        if c in risk_df.columns
    ]

    priority = (
        risk_df[display_cols]
        .sort_values(
            "_risk_score",
            ascending=False
        )
        .head(25)
        .copy()
    )

    priority["_risk_score"] = (
        priority["_risk_score"] * 100
    ).round(1)

    priority = priority.rename(
        columns={
            "_risk_score": "Risk %",
            "_risk_level": "Risk Level",
            "_segment": "Segment"
        }
    )

    st.dataframe(
        priority,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 3 — CUSTOMER SEGMENTS
# ============================================================

elif page == "Customer Segments":

    st.markdown(
        '<div class="main-title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Behavioral customer groups designed to support targeted retention strategies.'
        '</div>',
        unsafe_allow_html=True
    )

    segment_summary = (
        df.groupby("_segment")
        .agg(
            Customers=("_segment", "size"),
            Avg_Tenure=("_tenure", "mean"),
            Avg_Monthly=("_monthly", "mean"),
            Avg_Risk=("_risk_score", "mean"),
            Churn_Rate=("_churn", "mean")
        )
        .reset_index()
    )

    segment_summary["Avg_Risk"] *= 100
    segment_summary["Churn_Rate"] *= 100

    segment_summary.columns = [
        "Segment",
        "Customers",
        "Avg Tenure",
        "Avg Monthly Spend",
        "Avg Risk %",
        "Churn Rate %"
    ]

    c1, c2 = st.columns(2)

    with c1:

        fig = px.pie(
            segment_summary,
            names="Segment",
            values="Customers",
            hole=0.55,
            title="Customer Segment Distribution"
        )

        fig.update_layout(
            template="plotly_white",
            height=430
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.bar(
            segment_summary,
            x="Segment",
            y="Churn Rate %",
            text="Churn Rate %",
            title="Churn Rate by Segment"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            height=430
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
# PAGE 4 — CHURN DRIVERS
# ============================================================

elif page == "Churn Drivers":

    st.markdown(
        '<div class="main-title">Churn Drivers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Key customer attributes associated with model-predicted churn risk.'
        '</div>',
        unsafe_allow_html=True
    )

    fig = px.bar(
        shap_data.sort_values("Importance"),
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance",
        title="Top Factors Influencing Customer Churn"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=650,
        xaxis_title="Mean Absolute SHAP Impact",
        yaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        '<div class="section-title">Key Findings</div>',
        unsafe_allow_html=True
    )

    top1 = shap_data.iloc[0]["Feature"]
    top2 = shap_data.iloc[1]["Feature"]
    top3 = shap_data.iloc[2]["Feature"]

    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-title">
                ◆ Model Interpretation
            </div>

            <div class="insight-text">
                The strongest model drivers are
                <b>{top1}</b>,
                <b>{top2}</b>, and
                <b>{top3}</b>.
                These variables should receive the greatest attention
                when designing customer retention strategies.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">SHAP Importance Table</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        shap_data.round(4),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 5 — CUSTOMER EXPLORER
# ============================================================

elif page == "Customer Explorer":

    st.markdown(
        '<div class="main-title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Search and inspect individual customer profiles.'
        '</div>',
        unsafe_allow_html=True
    )

    if customer_id_col:

        customer_ids = (
            df[customer_id_col]
            .dropna()
            .astype(str)
            .drop_duplicates()
            .sort_values()
            .tolist()
        )

        selected_id = st.selectbox(
            "Select Customer ID",
            customer_ids,
            index=0,
            placeholder="Search customer..."
        )

        customer_rows = df[
            df[customer_id_col]
            .astype(str) == str(selected_id)
        ]

        if len(customer_rows) > 0:

            customer = customer_rows.iloc[0]

            risk_level = customer["_risk_level"]

            if risk_level == "Critical":
                badge = "status-critical"
            elif risk_level == "High":
                badge = "status-high"
            elif risk_level == "Medium":
                badge = "status-medium"
            else:
                badge = "status-low"

            st.markdown(
                f"""
                <div class="card">
                    <div style="
                        color:#667085;
                        font-size:12px;
                        font-weight:800;
                        text-transform:uppercase;
                        letter-spacing:1px;">
                        CUSTOMER PROFILE
                    </div>

                    <div style="
                        font-size:30px;
                        font-weight:850;
                        color:#101828;
                        margin-top:6px;">
                        Customer {selected_id}
                    </div>

                    <div class="{badge}" style="margin-top:12px;">
                        {risk_level} Risk
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="section-title">Customer Profile</div>',
                unsafe_allow_html=True
            )

            profile = {}

            for label, col in [
                ("Customer ID", customer_id_col),
                ("Contract", contract_col),
                ("Tenure", tenure_col),
                ("Monthly Charges", monthly_col),
                ("Total Charges", total_col),
                ("Churn", churn_col)
            ]:

                if col and col in customer.index:
                    profile[label] = customer[col]

            profile["Risk Score"] = (
                f"{customer['_risk_score']*100:.1f}%"
            )

            profile["Risk Level"] = customer["_risk_level"]

            profile["Customer Segment"] = customer["_segment"]

            profile_df = pd.DataFrame(
                profile.items(),
                columns=["Attribute", "Value"]
            )

            st.dataframe(
                profile_df,
                use_container_width=True,
                hide_index=True
            )

            st.markdown(
                '<div class="section-title">Customer Metrics</div>',
                unsafe_allow_html=True
            )

            m1, m2, m3, m4 = st.columns(4)

            with m1:
                st.metric(
                    "Tenure",
                    f"{customer['_tenure']:.0f} months"
                )

            with m2:
                st.metric(
                    "Monthly Charges",
                    f"${customer['_monthly']:,.2f}"
                )

            with m3:
                st.metric(
                    "Total Charges",
                    f"${customer['_total']:,.2f}"
                )

            with m4:
                st.metric(
                    "Risk Score",
                    f"{customer['_risk_score']*100:.1f}%"
                )

            # Retention recommendation

            if risk_level in ["Critical", "High"]:

                recommendation = (
                    "Prioritize this customer for immediate retention outreach. "
                    "Consider personalized offers, contract incentives and proactive support."
                )

            elif risk_level == "Medium":

                recommendation = (
                    "Monitor this customer closely and use targeted engagement "
                    "campaigns to reduce future churn risk."
                )

            else:

                recommendation = (
                    "Customer currently shows relatively low churn risk. "
                    "Continue engagement and loyalty initiatives."
                )

            st.markdown(
                f"""
                <div class="insight-card">
                    <div class="insight-title">
                        ◆ Retention Recommendation
                    </div>
                    <div class="insight-text">
                        {recommendation}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
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
    Customer Churn Intelligence &nbsp;•&nbsp;
    Data Science Portfolio Project &nbsp;•&nbsp;
    EDA + Machine Learning + SHAP + Segmentation
</div>
""", unsafe_allow_html=True)
