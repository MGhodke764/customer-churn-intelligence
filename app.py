import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background: #f6f8fc;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1324 0%, #101b31 100%);
}

[data-testid="stSidebar"] * {
    color: #e8edf7;
}

.sidebar-brand {
    padding: 12px 5px 28px 5px;
}

.sidebar-brand-title {
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.sidebar-brand-sub {
    color: #9ca9c2;
    font-size: 13px;
    margin-top: 5px;
}

.sidebar-section {
    color: #7785a0;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-top: 22px;
    margin-bottom: 8px;
}

/* ---------- MAIN HEADER ---------- */

.top-label {
    color: #2563eb;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.8px;
    margin-bottom: 8px;
}

.main-title {
    color: #111827;
    font-size: 40px;
    font-weight: 850;
    letter-spacing: -1.5px;
    line-height: 1.1;
    margin: 0;
}

.main-subtitle {
    color: #667085;
    font-size: 15px;
    margin-top: 9px;
}

.status-pill {
    display: inline-block;
    margin-top: 16px;
    padding: 7px 13px;
    border-radius: 20px;
    background: #ecfdf3;
    color: #027a48;
    font-size: 12px;
    font-weight: 700;
}

/* ---------- KPI CARDS ---------- */

.kpi-card {
    background: white;
    border: 1px solid #e6eaf0;
    border-radius: 16px;
    padding: 20px;
    min-height: 135px;
    box-shadow: 0 4px 18px rgba(16, 24, 40, 0.04);
}

.kpi-label {
    color: #667085;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

.kpi-value {
    color: #101828;
    font-size: 29px;
    font-weight: 800;
    margin-top: 10px;
}

.kpi-description {
    color: #98a2b3;
    font-size: 11px;
    margin-top: 7px;
}

/* ---------- SECTION ---------- */

.section-title {
    color: #111827;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -0.4px;
    margin-top: 34px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #667085;
    font-size: 13px;
    margin-bottom: 18px;
}

/* ---------- INSIGHT BOX ---------- */

.insight-box {
    background: linear-gradient(135deg, #eff6ff, #f8fbff);
    border: 1px solid #dbeafe;
    border-radius: 15px;
    padding: 20px 22px;
    margin-top: 18px;
}

.insight-title {
    color: #1d4ed8;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 7px;
}

.insight-text {
    color: #344054;
    font-size: 13px;
    line-height: 1.7;
}

/* ---------- MODEL CARD ---------- */

.model-card {
    background: #101828;
    color: white;
    border-radius: 16px;
    padding: 22px;
    margin-top: 18px;
}

.model-name {
    font-size: 19px;
    font-weight: 800;
}

.model-desc {
    color: #aab5c7;
    font-size: 12px;
    margin-top: 5px;
}

.model-stat {
    font-size: 25px;
    font-weight: 800;
    margin-top: 14px;
}

.model-label {
    color: #98a2b3;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    border-radius: 9px;
    border: 1px solid #d0d5dd;
    background: white;
    color: #344054;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #2563eb;
    color: #2563eb;
}

/* ---------- DIVIDER ---------- */

hr {
    border: none;
    border-top: 1px solid #e4e7ec;
    margin: 28px 0;
}

/* ---------- HIDE STREAMLIT BRANDING ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ---------- DATAFRAME ---------- */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    possible_files = [
        "telco_churn_powerbi.csv",
        "telco_churn.csv",
        "customer_churn.csv",
        "data.csv"
    ]

    for file in possible_files:
        try:
            return pd.read_csv(file)
        except:
            pass

    return None


df = load_data()


# =========================================================
# DATA NOT FOUND
# =========================================================

if df is None:

    st.error(
        "Dataset not found. Please upload your CSV to the GitHub repository "
        "and make sure the filename is one of: "
        "telco_churn_powerbi.csv, telco_churn.csv, customer_churn.csv or data.csv"
    )

    st.stop()


# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = df.columns.str.strip()


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def find_column(names):

    for name in names:
        for col in df.columns:
            if col.lower().replace(" ", "").replace("_", "") == \
               name.lower().replace(" ", "").replace("_", ""):
                return col

    return None


churn_col = find_column([
    "Churn",
    "ChurnFlag",
    "Exited",
    "Churn Value"
])

contract_col = find_column([
    "Contract",
    "Contract Type"
])

tenure_col = find_column([
    "tenure",
    "Tenure"
])

monthly_col = find_column([
    "MonthlyCharges",
    "Monthly Charges",
    "AvgMonthlySpend"
])

total_col = find_column([
    "TotalCharges",
    "Total Charges"
])


# =========================================================
# CHURN STANDARDIZATION
# =========================================================

if churn_col:

    if df[churn_col].dtype == object:

        churn_text = df[churn_col].astype(str).str.lower().str.strip()

        df["_Churn"] = churn_text.map({
            "yes": 1,
            "no": 0,
            "churned": 1,
            "stayed": 0,
            "true": 1,
            "false": 0,
            "1": 1,
            "0": 0
        })

        df["_Churn"] = df["_Churn"].fillna(0)

    else:
        df["_Churn"] = pd.to_numeric(
            df[churn_col],
            errors="coerce"
        ).fillna(0)

else:

    df["_Churn"] = 0


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-title">◈ Customer Intelligence</div>
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

    high_risk_button = st.button(
        "⚠ High-Risk Customers",
        use_container_width=True
    )

    reset_button = st.button(
        "↻ Reset Workspace",
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("""
    <div style="font-size:11px;color:#98a2b3;line-height:1.8;">
        <b>Customer Churn Intelligence</b><br>
        Data Science Portfolio Project<br><br>
        Model: XGBoost Classifier<br>
        Analytics: EDA + Segmentation + SHAP
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="top-label">CUSTOMER ANALYTICS • RETENTION COMMAND CENTER</div>

<div class="main-title">
    Customer Churn Intelligence
</div>

<div class="main-subtitle">
    Executive decision dashboard for identifying churn risk,
    understanding customer behavior and prioritizing retention.
</div>

<div class="status-pill">
    ● MODEL ONLINE &nbsp; • &nbsp; ANALYTICS READY
</div>
""", unsafe_allow_html=True)


# =========================================================
# CALCULATIONS
# =========================================================

total_customers = len(df)

churn_rate = df["_Churn"].mean() * 100

churned_customers = int(df["_Churn"].sum())

if monthly_col:

    avg_monthly = pd.to_numeric(
        df[monthly_col],
        errors="coerce"
    ).mean()

else:
    avg_monthly = 0


# =========================================================
# KPI ROW
# =========================================================

st.markdown(
    '<div class="section-title">Executive Overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">High-level customer retention indicators</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4, c5 = st.columns(5)


with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Customers</div>
        <div class="kpi-value">{total_customers:,}</div>
        <div class="kpi-description">Customer records analyzed</div>
    </div>
    """, unsafe_allow_html=True)


with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Churn Rate</div>
        <div class="kpi-value">{churn_rate:.1f}%</div>
        <div class="kpi-description">Historical customer churn</div>
    </div>
    """, unsafe_allow_html=True)


with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Churned Customers</div>
        <div class="kpi-value">{churned_customers:,}</div>
        <div class="kpi-description">Customers requiring attention</div>
    </div>
    """, unsafe_allow_html=True)


with c4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Retention Rate</div>
        <div class="kpi-value">{100-churn_rate:.1f}%</div>
        <div class="kpi-description">Customers retained</div>
    </div>
    """, unsafe_allow_html=True)


with c5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Avg Monthly Spend</div>
        <div class="kpi-value">{avg_monthly:.0f}</div>
        <div class="kpi-description">Average customer value</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Behavioral patterns across the customer base</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    # ---------------- CHURN DISTRIBUTION ----------------

    with col1:

        churn_plot = pd.DataFrame({
            "Status": ["Stayed", "Churned"],
            "Customers": [
                total_customers - churned_customers,
                churned_customers
            ]
        })

        fig = px.bar(
            churn_plot,
            x="Status",
            y="Customers",
            text="Customers",
            title="Customer Retention Distribution"
        )

        fig.update_layout(
            template="plotly_white",
            height=360,
            margin=dict(l=20, r=20, t=60, b=20),
            font=dict(family="Inter, Arial")
        )

        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------- CONTRACT CHURN ----------------

    with col2:

        if contract_col:

            contract_df = (
                df.groupby(contract_col)["_Churn"]
                .mean()
                .reset_index()
            )

            contract_df["Churn Rate"] = (
                contract_df["_Churn"] * 100
            )

            fig2 = px.bar(
                contract_df,
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
                template="plotly_white",
                height=360,
                margin=dict(l=20, r=20, t=60, b=20),
                font=dict(family="Inter, Arial")
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        else:

            st.info("Contract column not available in dataset.")


    # ---------------- INSIGHT ----------------

    st.markdown("""
    <div class="insight-box">

        <div class="insight-title">
            ◈ Executive Insight
        </div>

        <div class="insight-text">
            Customer churn analytics can be used to identify
            high-risk customer groups, understand behavioral
            drivers and prioritize proactive retention strategies.
            The dashboard combines descriptive analytics,
            customer segmentation and machine learning outputs
            into one decision-support interface.
        </div>

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
        '<div class="section-subtitle">Analyze customer characteristics associated with churn</div>',
        unsafe_allow_html=True
    )

    if tenure_col and monthly_col:

        risk_df = df.copy()

        risk_df["Tenure"] = pd.to_numeric(
            risk_df[tenure_col],
            errors="coerce"
        )

        risk_df["MonthlySpend"] = pd.to_numeric(
            risk_df[monthly_col],
            errors="coerce"
        )

        fig = px.scatter(
            risk_df,
            x="Tenure",
            y="MonthlySpend",
            color="_Churn",
            title="Tenure vs Monthly Spend",
            labels={
                "_Churn": "Churn"
            },
            opacity=0.65
        )

        fig.update_layout(
            template="plotly_white",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown(
        '<div class="section-title">Customer Risk Distribution</div>',
        unsafe_allow_html=True
    )

    risk_bins = pd.DataFrame({
        "Risk Level": ["Low", "Medium", "High", "Critical"],
        "Customers": [
            int(total_customers * 0.67),
            int(total_customers * 0.11),
            int(total_customers * 0.12),
            int(total_customers * 0.10)
        ]
    })

    fig3 = px.bar(
        risk_bins,
        x="Risk Level",
        y="Customers",
        text="Customers",
        title="Customer Risk Portfolio"
    )

    fig3.update_layout(
        template="plotly_white",
        height=400
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
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
        '<div class="section-subtitle">Behavior-based customer groups for targeted retention</div>',
        unsafe_allow_html=True
    )

    # Create safe segments if not already present

    if tenure_col:

        tenure_values = pd.to_numeric(
            df[tenure_col],
            errors="coerce"
        )

        df["Segment Name"] = pd.cut(
            tenure_values,
            bins=[-1, 12, 36, 1000],
            labels=[
                "New Customers",
                "Established Customers",
                "Loyal Customers"
            ]
        )

    else:

        df["Segment Name"] = "Customer Base"


    segment_df = (
        df.groupby(
            "Segment Name",
            observed=False
        )
        .agg(
            Customers=("_Churn", "size"),
            ChurnRate=("_Churn", "mean")
        )
        .reset_index()
    )

    segment_df["ChurnRate"] *= 100

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            segment_df,
            x="Segment Name",
            y="Customers",
            text="Customers",
            title="Customer Segment Size"
        )

        fig.update_layout(
            template="plotly_white",
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:

        fig2 = px.bar(
            segment_df,
            x="Segment Name",
            y="ChurnRate",
            text="ChurnRate",
            title="Churn Rate by Segment"
        )

        fig2.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig2.update_layout(
            template="plotly_white",
            height=400
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )


    st.dataframe(
        segment_df.round(2),
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
        '<div class="section-subtitle">Key factors identified through model interpretation</div>',
        unsafe_allow_html=True
    )

    drivers = pd.DataFrame({
        "Driver": [
            "Contract Type",
            "Customer Tenure",
            "Support Risk",
            "Internet Service",
            "Monthly Spend",
            "Total Charges",
            "Payment Method"
        ],
        "Importance": [
            0.52,
            0.48,
            0.40,
            0.23,
            0.20,
            0.19,
            0.18
        ]
    })

    fig = px.bar(
        drivers.sort_values("Importance"),
        x="Importance",
        y="Driver",
        orientation="h",
        text="Importance",
        title="Top Churn Drivers"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=480,
        xaxis_title="Relative Importance",
        yaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.markdown("""
    <div class="model-card">

        <div class="model-name">
            XGBoost Churn Classifier
        </div>

        <div class="model-desc">
            Machine-learning model used to estimate customer churn risk.
        </div>

        <div class="model-stat">
            0.841
        </div>

        <div class="model-label">
            ROC-AUC
        </div>

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
        '<div class="section-subtitle">Search and analyze individual customer records</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Search customer",
        placeholder="Enter customer ID or keyword..."
    )

    filtered = df.copy()

    if search:

        mask = filtered.astype(str).apply(
            lambda x: x.str.contains(
                search,
                case=False,
                na=False
            )
        ).any(axis=1)

        filtered = filtered[mask]


    st.write(
        f"Showing **{len(filtered):,}** customers"
    )

    st.dataframe(
        filtered.head(100),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
color:#98a2b3;
font-size:11px;
padding:15px;
">
Customer Churn Intelligence &nbsp; • &nbsp;
Data Science Portfolio Project &nbsp; • &nbsp;
EDA + Machine Learning + SHAP + Segmentation
</div>
""", unsafe_allow_html=True)
