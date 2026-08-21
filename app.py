import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F5F7FB;
}

/* Remove default top padding */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1F2937;
}

section[data-testid="stSidebar"] * {
    color: #E5E7EB;
}

/* Sidebar title */
.sidebar-title {
    font-size: 21px;
    font-weight: 700;
    color: white;
    margin-bottom: 4px;
}

.sidebar-subtitle {
    font-size: 12px;
    color: #9CA3AF;
    margin-bottom: 25px;
}

/* Main header */
.main-title {
    font-size: 32px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 2px;
}

.main-subtitle {
    font-size: 14px;
    color: #6B7280;
    margin-bottom: 25px;
}

/* KPI cards */
.kpi-card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 20px 22px;
    min-height: 120px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}

.kpi-label {
    color: #6B7280;
    font-size: 13px;
    font-weight: 500;
    margin-bottom: 10px;
}

.kpi-value {
    color: #111827;
    font-size: 28px;
    font-weight: 700;
}

.kpi-description {
    color: #9CA3AF;
    font-size: 11px;
    margin-top: 6px;
}

/* Section titles */
.section-title {
    font-size: 19px;
    font-weight: 650;
    color: #111827;
    margin-top: 25px;
    margin-bottom: 12px;
}

.section-subtitle {
    font-size: 12px;
    color: #6B7280;
    margin-bottom: 15px;
}

/* Risk cards */
.risk-critical {
    background: #FEF2F2;
    border: 1px solid #FECACA;
    border-radius: 10px;
    padding: 15px;
}

.risk-high {
    background: #FFF7ED;
    border: 1px solid #FED7AA;
    border-radius: 10px;
    padding: 15px;
}

.risk-medium {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    border-radius: 10px;
    padding: 15px;
}

.risk-low {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-radius: 10px;
    padding: 15px;
}

/* Customer profile */
.profile-card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 22px;
    margin-top: 10px;
}

.profile-title {
    font-size: 20px;
    font-weight: 700;
    color: #111827;
}

.profile-label {
    font-size: 11px;
    color: #9CA3AF;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.profile-value {
    font-size: 15px;
    color: #374151;
    font-weight: 600;
}

/* Footer */
.footer {
    text-align: center;
    color: #9CA3AF;
    font-size: 11px;
    padding-top: 35px;
    padding-bottom: 10px;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    data = pd.read_csv("telco_churn_powerbi.csv")

    # Create Segment Name if missing
    if "Segment Name" not in data.columns and "CustomerSegment" in data.columns:

        segment_mapping = {
            0: "New / Low-Engagement",
            1: "High-Value Loyal",
            2: "Long-Term Low-Spend",
            3: "High-Risk / At-Risk"
        }

        data["Segment Name"] = (
            data["CustomerSegment"]
            .map(segment_mapping)
            .fillna("Other")
        )

    return data


df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">Customer Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">AI-Powered Churn Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Navigation")

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

    st.divider()

    st.markdown("### Model")

    st.caption("Algorithm")
    st.markdown("**XGBoost Classifier**")

    st.caption("Operating Threshold")
    st.markdown("**35%**")

    st.caption("ROC-AUC")
    st.markdown("**0.841**")

    st.divider()

    st.caption("Customer Churn Intelligence")
    st.caption("Data Science Portfolio Project")

# =========================================================
# COMMON CALCULATIONS
# =========================================================

total_customers = df["customerID"].nunique()

churned_customers = df.loc[
    df["ChurnFlag"] == 1,
    "customerID"
].nunique()

churn_rate = churned_customers / total_customers

high_risk = df[
    df["RiskLevel"].isin(["High", "Critical"])
]["customerID"].nunique()

avg_probability = df["ChurnProbability"].mean()

at_risk = df[
    df["ChurnProbability"] >= 0.35
]["customerID"].nunique()

# =========================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    st.markdown(
        '<div class="main-title">Customer Churn Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Executive overview of customer retention risk, churn behavior and model predictions.'
        '</div>',
        unsafe_allow_html=True
    )

    # KPI ROW
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">TOTAL CUSTOMERS</div>
                <div class="kpi-value">{total_customers:,}</div>
                <div class="kpi-description">Active customer base</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">CHURN RATE</div>
                <div class="kpi-value">{churn_rate:.1%}</div>
                <div class="kpi-description">Historical churn</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">AT-RISK CUSTOMERS</div>
                <div class="kpi-value">{at_risk:,}</div>
                <div class="kpi-description">Probability ≥ 35%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">HIGH / CRITICAL</div>
                <div class="kpi-value">{high_risk:,}</div>
                <div class="kpi-description">Priority customers</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c5:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">AVG MODEL RISK</div>
                <div class="kpi-value">{avg_probability:.1%}</div>
                <div class="kpi-description">Predicted probability</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # CHARTS

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

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

        risk_counts.columns = ["RiskLevel", "Customers"]

        fig = px.bar(
            risk_counts,
            x="RiskLevel",
            y="Customers",
            text="Customers",
            title="Customer Risk Distribution"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            height=390,
            margin=dict(l=20, r=20, t=55, b=20),
            xaxis_title=None,
            yaxis_title="Customers",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

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
            text=contract_churn["ChurnRate"].round(1),
            title="Churn Rate by Contract"
        )

        fig.update_traces(
            texttemplate="%{text}%",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            height=390,
            margin=dict(l=20, r=20, t=55, b=20),
            xaxis_title=None,
            yaxis_title="Churn Rate (%)",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # INSIGHT BOX

    st.markdown(
        '<div class="section-title">Executive Insight</div>',
        unsafe_allow_html=True
    )

    month_contract = df[
        df["Contract"] == "Month-to-month"
    ]["ChurnFlag"].mean()

    st.info(
        f"Customers on month-to-month contracts show a "
        f"{month_contract:.1%} churn rate. "
        f"The ML system currently flags {at_risk:,} customers "
        f"as requiring proactive retention attention."
    )

# =========================================================
# PAGE 2 — RISK ANALYTICS
# =========================================================

elif page == "Risk Analytics":

    st.markdown(
        '<div class="main-title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Explore model-generated churn probabilities and customer risk tiers.'
        '</div>',
        unsafe_allow_html=True
    )

    # FILTERS

    f1, f2, f3 = st.columns(3)

    with f1:
        selected_risk = st.multiselect(
            "Risk Level",
            ["Critical", "High", "Medium", "Low"],
            default=["Critical", "High"]
        )

    with f2:
        selected_contract = st.multiselect(
            "Contract",
            sorted(df["Contract"].dropna().unique()),
            default=list(df["Contract"].dropna().unique())
        )

    with f3:
        min_probability = st.slider(
            "Minimum Churn Probability",
            0.0,
            1.0,
            0.35,
            0.05
        )

    filtered = df[
        (df["RiskLevel"].isin(selected_risk)) &
        (df["Contract"].isin(selected_contract)) &
        (df["ChurnProbability"] >= min_probability)
    ]

    st.markdown(
        '<div class="section-title">Risk Population</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Customers Matching Filters",
        f"{len(filtered):,}"
    )

    c2.metric(
        "Average Risk",
        f"{filtered['ChurnProbability'].mean():.1%}"
        if len(filtered) else "0%"
    )

    c3.metric(
        "Average Monthly Charges",
        f"${filtered['MonthlyCharges'].mean():,.2f}"
        if len(filtered) else "$0"
    )

    # SCATTER

    fig = px.scatter(
        filtered,
        x="tenure",
        y="ChurnProbability",
        size="MonthlyCharges",
        color="RiskLevel",
        hover_data=[
            "customerID",
            "Contract",
            "MonthlyCharges"
        ],
        title="Customer Risk Map",
        labels={
            "tenure": "Tenure (months)",
            "ChurnProbability": "Churn Probability"
        }
    )

    fig.update_layout(
        template="plotly_white",
        height=480
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "Higher position indicates greater predicted churn probability. "
        "Larger points represent higher monthly charges."
    )

# =========================================================
# PAGE 3 — SEGMENTS
# =========================================================

elif page == "Customer Segments":

    st.markdown(
        '<div class="main-title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'K-Means customer groups based on behavioral and financial characteristics.'
        '</div>',
        unsafe_allow_html=True
    )

    if "Segment Name" not in df.columns:

        mapping = {
            0: "New / Low-Engagement",
            1: "High-Value Loyal",
            2: "Long-Term Low-Spend",
            3: "High-Risk / At-Risk"
        }

        df["Segment Name"] = (
            df["CustomerSegment"]
            .map(mapping)
            .fillna("Other")
        )

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

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            segment_data,
            x="Segment Name",
            y="Customers",
            title="Customer Distribution by Segment"
        )

        fig.update_layout(
            template="plotly_white",
            height=420,
            xaxis_title=None
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.bar(
            segment_data,
            x="Segment Name",
            y="ChurnRate",
            title="Churn Rate by Segment"
        )

        fig.update_layout(
            template="plotly_white",
            height=420,
            xaxis_title=None,
            yaxis_title="Churn Rate (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown(
        '<div class="section-title">Segment Profile</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        segment_data.round(2),
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# PAGE 4 — CHURN DRIVERS
# =========================================================

elif page == "Churn Drivers":

    st.markdown(
        '<div class="main-title">Churn Drivers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Explainable AI analysis using SHAP feature importance.'
        '</div>',
        unsafe_allow_html=True
    )

    try:

        importance = pd.read_csv(
            "shap_feature_importance.csv"
        )

        importance = importance.sort_values(
            "MeanAbsSHAP",
            ascending=True
        )

        top = importance.tail(12)

        fig = px.bar(
            top,
            x="MeanAbsSHAP",
            y="Feature",
            orientation="h",
            title="Top Factors Influencing Churn"
        )

        fig.update_layout(
            template="plotly_white",
            height=600,
            xaxis_title="Mean |SHAP Value|",
            yaxis_title=None
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.info(
            "Higher Mean |SHAP Value| indicates greater overall influence "
            "on the model's churn predictions."
        )

        st.markdown(
            '<div class="section-title">Feature Importance Table</div>',
            unsafe_allow_html=True
        )

        st.dataframe(
            importance.sort_values(
                "MeanAbsSHAP",
                ascending=False
            ).head(15).round(4),
            use_container_width=True,
            hide_index=True
        )

    except Exception:

        st.error(
            "SHAP feature importance data could not be loaded."
        )

# =========================================================
# PAGE 5 — CUSTOMER EXPLORER
# =========================================================

elif page == "Customer Explorer":

    st.markdown(
        '<div class="main-title">Customer Risk Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Inspect individual customer risk and recommended retention actions.'
        '</div>',
        unsafe_allow_html=True
    )

    customer_id = st.selectbox(
        "Select Customer",
        sorted(df["customerID"].dropna().unique())
    )

    customer = df[
        df["customerID"] == customer_id
    ].iloc[0]

    probability = customer["ChurnProbability"]

    if probability >= 0.70:
        risk_class = "risk-critical"
    elif probability >= 0.50:
        risk_class = "risk-high"
    elif probability >= 0.35:
        risk_class = "risk-medium"
    else:
        risk_class = "risk-low"

    st.markdown(
        f"""
        <div class="{risk_class}">
            <div class="profile-label">CUSTOMER RISK</div>
            <div class="profile-title">
                {customer_id}
            </div>
            <br>
            <b>Predicted Churn Probability:</b>
            {probability:.1%}
            &nbsp;&nbsp; | &nbsp;&nbsp;
            <b>Risk Level:</b>
            {customer["RiskLevel"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Customer Profile</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Tenure",
        f"{customer['tenure']} months"
    )

    c2.metric(
        "Monthly Charges",
        f"${customer['MonthlyCharges']:.2f}"
    )

    c3.metric(
        "Contract",
        customer["Contract"]
    )

    c4.metric(
        "Internet Service",
        customer["InternetService"]
    )

    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )

    st.success(
        customer["RetentionRecommendation"]
    )

    # Highest risk customers

    st.markdown(
        '<div class="section-title">Priority Customer List</div>',
        unsafe_allow_html=True
    )

    priority = df[
        df["ChurnProbability"] >= 0.35
    ].sort_values(
        "ChurnProbability",
        ascending=False
    )

    columns = [
        "customerID",
        "Contract",
        "tenure",
        "MonthlyCharges",
        "ChurnProbabilityPct",
        "RiskLevel",
        "RetentionRecommendation"
    ]

    st.dataframe(
        priority[columns].head(50),
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Customer Churn Intelligence • XGBoost • K-Means • SHAP • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
