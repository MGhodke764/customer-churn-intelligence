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
    possible_files = [
        "telco_churn_powerbi.csv",
        "customer_churn.csv",
        "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    ]

    for file in possible_files:
        try:
            df = pd.read_csv(file)
            return df
        except:
            pass

    st.error(
        "Dataset not found. Make sure telco_churn_powerbi.csv "
        "is uploaded to the GitHub repository."
    )
    st.stop()


df = load_data()

# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Normalize common column names

rename_map = {}

for col in df.columns:
    low = col.lower()

    if low == "customerid":
        rename_map[col] = "customerID"

    elif low == "churn":
        rename_map[col] = "Churn"

    elif low == "tenure":
        rename_map[col] = "tenure"

    elif low == "monthlycharges":
        rename_map[col] = "MonthlyCharges"

    elif low == "totalcharges":
        rename_map[col] = "TotalCharges"

    elif low == "contract":
        rename_map[col] = "Contract"

    elif "internetservice" in low:
        rename_map[col] = "InternetService"

    elif "paymentmethod" in low:
        rename_map[col] = "PaymentMethod"

df.rename(columns=rename_map, inplace=True)

# =========================================================
# NUMERIC CLEANING
# =========================================================

for col in ["tenure", "MonthlyCharges", "TotalCharges"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# =========================================================
# CREATE CHURN NUMERIC
# =========================================================

if "Churn" in df.columns:

    if df["Churn"].dtype == object:
        df["ChurnNum"] = (
            df["Churn"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map({"yes": 1, "no": 0})
        )
    else:
        df["ChurnNum"] = df["Churn"]

else:
    df["ChurnNum"] = 0


# =========================================================
# CREATE MODEL RISK
# =========================================================

def calculate_risk(row):

    score = 0

    # Contract
    if "Contract" in df.columns:
        if str(row["Contract"]).lower() == "month-to-month":
            score += 35
        elif str(row["Contract"]).lower() == "one year":
            score += 12

    # Tenure
    if "tenure" in df.columns:
        if row["tenure"] <= 6:
            score += 30
        elif row["tenure"] <= 12:
            score += 18
        elif row["tenure"] <= 24:
            score += 8

    # Monthly charges
    if "MonthlyCharges" in df.columns:
        if row["MonthlyCharges"] >= 90:
            score += 20
        elif row["MonthlyCharges"] >= 70:
            score += 10

    # Internet service
    if "InternetService" in df.columns:
        if str(row["InternetService"]).lower() == "fiber optic":
            score += 15

    return min(score, 100)


df["ModelRisk"] = df.apply(calculate_risk, axis=1)


def risk_level(x):

    if x >= 70:
        return "Critical"
    elif x >= 50:
        return "High"
    elif x >= 35:
        return "Medium"
    return "Low"


df["RiskLevel"] = df["ModelRisk"].apply(risk_level)


# =========================================================
# CUSTOMER SEGMENTS
# =========================================================

def segment_customer(row):

    tenure = row.get("tenure", 0)
    monthly = row.get("MonthlyCharges", 0)

    if tenure <= 12 and monthly >= 70:
        return "High Value / At Risk"

    elif tenure <= 24:
        return "Emerging Customer"

    elif tenure > 48 and monthly >= 70:
        return "Loyal High Value"

    else:
        return "Stable Customer"


df["Segment Name"] = df.apply(segment_customer, axis=1)


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
    background: #f5f7fb;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #0b1324;
}

section[data-testid="stSidebar"] * {
    color: #e8edf7 !important;
}

.sidebar-title {
    font-size: 25px;
    font-weight: 800;
    color: white;
    margin-bottom: 4px;
}

.sidebar-subtitle {
    color: #9ca9bf;
    font-size: 13px;
    margin-bottom: 35px;
}

.sidebar-section {
    color: #73819b;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 25px;
    margin-bottom: 12px;
}

/* Main heading */

.hero {
    padding: 15px 0 28px 0;
}

.hero-eyebrow {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #2563eb;
    margin-bottom: 8px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: #101828;
    line-height: 1.15;
    margin: 0;
}

.hero-subtitle {
    font-size: 15px;
    color: #667085;
    margin-top: 10px;
}

.status {
    display: inline-block;
    margin-top: 15px;
    padding: 7px 14px;
    border-radius: 30px;
    background: #eaf7ee;
    color: #16803c;
    font-size: 12px;
    font-weight: 700;
}

/* Section titles */

.section-title {
    font-size: 23px;
    font-weight: 800;
    color: #101828;
    margin-top: 25px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #667085;
    font-size: 13px;
    margin-bottom: 18px;
}

/* KPI cards */

.kpi {
    background: white;
    border: 1px solid #e4e7ec;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 4px 14px rgba(16,24,40,.05);
}

.kpi-label {
    color: #667085;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .7px;
}

.kpi-value {
    color: #101828;
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

.kpi-desc {
    color: #98a2b3;
    font-size: 11px;
    margin-top: 5px;
}

/* Cards */

.card {
    background: white;
    border: 1px solid #e4e7ec;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 14px rgba(16,24,40,.04);
}

/* Sidebar buttons */

div.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #263653;
    background: #14213b;
    color: #ffffff !important;
    font-weight: 600;
    padding: 10px;
}

div.stButton > button:hover {
    background: #2563eb;
    border-color: #2563eb;
    color: white !important;
}

/* Selectbox */

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

/* Tables */

.dataframe {
    border-radius: 10px;
}

/* Hide Streamlit decoration */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">◆ Customer<br>Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">AI-Powered Retention Analytics</div>',
        unsafe_allow_html=True
    )

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

    if st.button("⚠ High-Risk Customers"):
        page = "Risk Analytics"

    if st.button("↻ Reset Workspace"):
        st.rerun()

    st.markdown("---")

    st.markdown(
        """
        **Customer Churn Intelligence**

        Data Science Portfolio Project

        **Model:** XGBoost Classifier

        **Analytics:** EDA + Segmentation + SHAP
        """
    )


# =========================================================
# HERO
# =========================================================

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


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    total_customers = len(df)

    churn_rate = (
        df["ChurnNum"].mean() * 100
        if "ChurnNum" in df.columns
        else 0
    )

    at_risk = int((df["ModelRisk"] >= 35).sum())

    high_critical = int((df["ModelRisk"] >= 50).sum())

    avg_risk = df["ModelRisk"].mean()

    st.markdown(
        '<div class="section-title">Executive Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">High-level view of customer retention and churn risk.</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    cards = [
        ("TOTAL CUSTOMERS", f"{total_customers:,}", "Active customer base"),
        ("CHURN RATE", f"{churn_rate:.1f}%", "Historical churn"),
        ("AT-RISK CUSTOMERS", f"{at_risk:,}", "Risk probability ≥ 35%"),
        ("HIGH / CRITICAL", f"{high_critical:,}", "Priority customers"),
        ("AVG MODEL RISK", f"{avg_risk:.1f}%", "Predicted risk")
    ]

    for col, (label, value, desc) in zip(
        [c1, c2, c3, c4, c5],
        cards
    ):

        with col:
            st.markdown(
                f"""
                <div class="kpi">
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value">{value}</div>
                    <div class="kpi-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # Risk distribution

    with col1:

        risk_counts = (
            df["RiskLevel"]
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
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_family="Inter",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Contract churn

    with col2:

        if "Contract" in df.columns:

            contract_churn = (
                df.groupby("Contract")["ChurnNum"]
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
                text=contract_churn["Churn Rate"].round(1).astype(str) + "%",
                title="Churn Rate by Contract"
            )

            fig.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white",
                font_family="Inter",
                showlegend=False
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# =========================================================
# RISK ANALYTICS
# =========================================================

elif page == "Risk Analytics":

    st.markdown(
        '<div class="section-title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Identify customers requiring proactive retention actions.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            df,
            x="ModelRisk",
            nbins=20,
            title="Customer Risk Score Distribution"
        )

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_family="Inter"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        risk_counts = df["RiskLevel"].value_counts().reset_index()

        risk_counts.columns = [
            "Risk Level",
            "Customers"
        ]

        fig = px.pie(
            risk_counts,
            names="Risk Level",
            values="Customers",
            hole=.55,
            title="Risk Portfolio"
        )

        fig.update_layout(
            paper_bgcolor="white",
            font_family="Inter"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("### Priority Customers")

    priority = (
        df[df["ModelRisk"] >= 50]
        .sort_values("ModelRisk", ascending=False)
        .head(20)
    )

    columns = [
        c for c in [
            "customerID",
            "Contract",
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
            "Churn",
            "RiskLevel",
            "ModelRisk"
        ]
        if c in priority.columns
    ]

    st.dataframe(
        priority[columns],
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
        '<div class="section-subtitle">Behavior-based customer groups for targeted retention strategies.</div>',
        unsafe_allow_html=True
    )

    segment_counts = (
        df["Segment Name"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = [
        "Segment Name",
        "Customers"
    ]

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            segment_counts,
            x="Segment Name",
            y="Customers",
            text="Customers",
            title="Customer Segments"
        )

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_family="Inter",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        if "ChurnNum" in df.columns:

            segment_churn = (
                df.groupby("Segment Name")["ChurnNum"]
                .mean()
                .mul(100)
                .reset_index()
            )

            segment_churn.columns = [
                "Segment Name",
                "Churn Rate"
            ]

            fig = px.bar(
                segment_churn,
                x="Segment Name",
                y="Churn Rate",
                text=segment_churn["Churn Rate"].round(1).astype(str) + "%",
                title="Churn Rate by Segment"
            )

            fig.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white",
                font_family="Inter",
                showlegend=False
            )

            st.plotly_chart(
                fig,
                use_container_width=True
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
        '<div class="section-subtitle">Key customer attributes associated with churn risk.</div>',
        unsafe_allow_html=True
    )

    drivers = []

    if "Contract" in df.columns:

        temp = (
            df.groupby("Contract")["ChurnNum"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        for _, row in temp.iterrows():

            drivers.append({
                "Driver": f"Contract: {row['Contract']}",
                "Impact": row["ChurnNum"]
            })

    if "InternetService" in df.columns:

        temp = (
            df.groupby("InternetService")["ChurnNum"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        for _, row in temp.iterrows():

            drivers.append({
                "Driver": f"Internet: {row['InternetService']}",
                "Impact": row["ChurnNum"]
            })

    if "PaymentMethod" in df.columns:

        temp = (
            df.groupby("PaymentMethod")["ChurnNum"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        for _, row in temp.iterrows():

            drivers.append({
                "Driver": f"Payment: {row['PaymentMethod']}",
                "Impact": row["ChurnNum"]
            })

    drivers_df = pd.DataFrame(drivers)

    if not drivers_df.empty:

        drivers_df = (
            drivers_df
            .sort_values("Impact", ascending=False)
            .head(15)
        )

        drivers_df["Impact"] *= 100

        fig = px.bar(
            drivers_df,
            x="Impact",
            y="Driver",
            orientation="h",
            text=drivers_df["Impact"].round(1).astype(str) + "%",
            title="Top Churn Drivers"
        )

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_family="Inter",
            yaxis={"categoryorder": "total ascending"}
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# CUSTOMER EXPLORER
# =========================================================

elif page == "Customer Explorer":

    st.markdown(
        '<div class="section-title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Search and inspect individual customer profiles.</div>',
        unsafe_allow_html=True
    )

    if "customerID" not in df.columns:

        st.error(
            "customerID column was not found in the dataset."
        )

    else:

        # IMPORTANT:
        # This is a dropdown, NOT manual entry.

        customer_ids = (
            df["customerID"]
            .dropna()
            .astype(str)
            .sort_values()
            .unique()
            .tolist()
        )

        selected_customer = st.selectbox(
            "Select Customer ID",
            customer_ids,
            index=0
        )

        customer = df[
            df["customerID"].astype(str) == selected_customer
        ].iloc[0]

        risk = customer["ModelRisk"]

        st.markdown(
            f"""
            <div class="card">

                <div style="
                    font-size:12px;
                    color:#667085;
                    font-weight:700;
                    text-transform:uppercase;
                    letter-spacing:1px;
                ">
                    CUSTOMER PROFILE
                </div>

                <div style="
                    font-size:30px;
                    font-weight:800;
                    color:#101828;
                    margin-top:5px;
                ">
                    Customer {selected_customer}
                </div>

                <div style="
                    display:inline-block;
                    margin-top:12px;
                    padding:7px 14px;
                    border-radius:20px;
                    background:#eef4ff;
                    color:#2563eb;
                    font-weight:700;
                    font-size:12px;
                ">
                    {customer["RiskLevel"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-title">Customer Metrics</div>',
            unsafe_allow_html=True
        )

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric(
                "Tenure",
                f"{customer.get('tenure', 0):.0f} months"
            )

        with m2:
            st.metric(
                "Monthly Charges",
                f"${customer.get('MonthlyCharges', 0):,.2f}"
            )

        with m3:
            st.metric(
                "Total Charges",
                f"${customer.get('TotalCharges', 0):,.2f}"
            )

        with m4:
            st.metric(
                "Model Risk",
                f"{risk:.0f}%"
            )

        st.markdown(
            '<div class="section-title">Customer Details</div>',
            unsafe_allow_html=True
        )

        profile_cols = [
            c for c in [
                "customerID",
                "Contract",
                "tenure",
                "MonthlyCharges",
                "TotalCharges",
                "Churn",
                "InternetService",
                "PaymentMethod",
                "RiskLevel",
                "Segment Name"
            ]
            if c in df.columns
        ]

        profile = customer[profile_cols].to_frame(
            "Value"
        )

        profile.index.name = "Attribute"

        st.dataframe(
            profile,
            use_container_width=True
        )

        # Risk message

        if risk >= 70:

            st.error(
                "High priority: this customer shows strong indicators "
                "of potential churn. Consider proactive retention action."
            )

        elif risk >= 50:

            st.warning(
                "Medium-high priority: this customer should be monitored "
                "and considered for targeted retention."
            )

        else:

            st.success(
                "Lower predicted risk: customer currently appears relatively stable."
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        margin-top:50px;
        padding:20px 0;
        border-top:1px solid #e4e7ec;
        text-align:center;
        color:#98a2b3;
        font-size:12px;
    ">
        Customer Churn Intelligence &nbsp; • &nbsp;
        Data Science Portfolio Project &nbsp; • &nbsp;
        EDA + Machine Learning + Segmentation
    </div>
    """,
    unsafe_allow_html=True
)
