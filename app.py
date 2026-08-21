import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown("""
<style>

/* =========================================================
   GLOBAL
   ========================================================= */

:root {
    --blue: #2563EB;
    --blue-dark: #1D4ED8;
    --navy: #0F172A;
    --text: #172033;
    --muted: #64748B;
    --light: #F8FAFC;
    --line: #E2E8F0;
    --white: #FFFFFF;
    --green: #059669;
    --red: #DC2626;
    --orange: #EA580C;
}

.stApp {
    background: #F7F9FC;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stDecoration"] {
    display: none;
}


/* =========================================================
   BRAND
   ========================================================= */

.brand-wrapper {
    display: flex;
    align-items: center;
    gap: 13px;
    margin-bottom: 18px;
}

.brand-icon {
    width: 44px;
    height: 44px;
    border-radius: 13px;

    background: linear-gradient(
        135deg,
        #2563EB,
        #3B82F6
    );

    display: flex;
    align-items: center;
    justify-content: center;

    color: white;
    font-size: 20px;
    font-weight: 800;

    box-shadow:
        0 6px 18px rgba(37, 99, 235, 0.20);
}

.brand-name {
    font-size: 25px;
    font-weight: 850;
    letter-spacing: -0.7px;
    color: #0F172A;
}

.brand-subtitle {
    font-size: 12px;
    color: #64748B;
    margin-top: 2px;
}


/* =========================================================
   NAVIGATION
   ========================================================= */

.nav-container {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;

    padding: 7px;

    box-shadow:
        0 4px 16px rgba(15, 23, 42, 0.035);

    margin-bottom: 15px;
}

.nav-container .stButton > button {
    min-height: 44px;

    border-radius: 10px;

    border: 1px solid transparent;

    background: transparent;

    color: #475569;

    font-size: 13px;
    font-weight: 700;

    transition:
        background 0.2s ease,
        color 0.2s ease,
        transform 0.2s ease;
}

.nav-container .stButton > button:hover {
    background: #EFF6FF;
    color: #2563EB;
    border-color: #DBEAFE;
    transform: translateY(-1px);
}


/* =========================================================
   QUICK ACTIONS
   ========================================================= */

.quick-label {
    font-size: 10px;
    font-weight: 850;

    color: #64748B;

    text-transform: uppercase;
    letter-spacing: 1.7px;

    margin-top: 10px;
    margin-bottom: 8px;
}

.quick-button .stButton > button {
    min-height: 38px;

    border-radius: 9px;

    background: white;

    color: #334155;

    border: 1px solid #E2E8F0;

    font-size: 12px;
    font-weight: 700;
}

.quick-button .stButton > button:hover {
    color: #2563EB;
    border-color: #93C5FD;
    background: #F8FBFF;
}


/* =========================================================
   PAGE HEADER
   ========================================================= */

.page-header {
    padding-top: 18px;
    padding-bottom: 22px;

    border-bottom: 1px solid #E2E8F0;

    margin-bottom: 25px;
}

.eyebrow {
    color: #2563EB;

    font-size: 10px;
    font-weight: 850;

    text-transform: uppercase;
    letter-spacing: 1.5px;

    margin-bottom: 6px;
}

.page-title {
    color: #0F172A;

    font-size: 34px;
    line-height: 1.1;

    font-weight: 850;

    letter-spacing: -1.2px;

    margin: 0;
}

.page-subtitle {
    color: #64748B;

    font-size: 13px;

    margin-top: 8px;
}

.status-pill {
    background: #ECFDF5;

    border: 1px solid #A7F3D0;

    color: #047857;

    border-radius: 999px;

    padding: 8px 13px;

    font-size: 11px;

    font-weight: 800;

    white-space: nowrap;
}


/* =========================================================
   KPI CARDS
   ========================================================= */

.kpi-card {
    background: white;

    border: 1px solid #E2E8F0;

    border-radius: 15px;

    padding: 18px 19px;

    min-height: 130px;

    box-shadow:
        0 4px 15px rgba(15, 23, 42, 0.035);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);

    box-shadow:
        0 8px 22px rgba(15, 23, 42, 0.07);
}

.kpi-label {
    color: #64748B;

    font-size: 10px;

    font-weight: 850;

    letter-spacing: 0.9px;
}

.kpi-value {
    color: #0F172A;

    font-size: 29px;

    font-weight: 850;

    letter-spacing: -0.8px;

    margin-top: 12px;
}

.kpi-description {
    color: #94A3B8;

    font-size: 10px;

    margin-top: 4px;
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {
    color: #0F172A;

    font-size: 19px;

    font-weight: 850;

    letter-spacing: -0.35px;

    margin-top: 30px;
    margin-bottom: 12px;
}

.section-subtitle {
    color: #64748B;

    font-size: 12px;

    margin-top: -6px;

    margin-bottom: 15px;
}


/* =========================================================
   INSIGHT
   ========================================================= */

.insight-card {
    background:
        linear-gradient(
            135deg,
            #EFF6FF 0%,
            #F8FAFC 100%
        );

    border: 1px solid #BFDBFE;

    border-radius: 15px;

    padding: 18px 20px;

    margin-top: 12px;
}

.insight-title {
    color: #1D4ED8;

    font-size: 11px;

    text-transform: uppercase;

    letter-spacing: 1px;

    font-weight: 850;
}

.insight-text {
    color: #1E3A8A;

    font-size: 13px;

    line-height: 1.6;

    margin-top: 7px;
}


/* =========================================================
   RISK CARDS
   ========================================================= */

.risk-card {
    border-radius: 15px;

    padding: 20px;

    border: 1px solid;
}

.risk-critical {
    background: #FEF2F2;
    border-color: #FECACA;
}

.risk-high {
    background: #FFF7ED;
    border-color: #FED7AA;
}

.risk-medium {
    background: #FFFBEB;
    border-color: #FDE68A;
}

.risk-low {
    background: #F0FDF4;
    border-color: #BBF7D0;
}

.risk-label {
    font-size: 10px;

    font-weight: 850;

    text-transform: uppercase;

    letter-spacing: 1px;

    color: #64748B;
}

.risk-customer {
    font-size: 26px;

    font-weight: 850;

    color: #0F172A;

    margin-top: 4px;
}


/* =========================================================
   CUSTOMER PROFILE
   ========================================================= */

.profile-card {
    background: white;

    border: 1px solid #E2E8F0;

    border-radius: 15px;

    padding: 22px;

    margin-top: 15px;

    box-shadow:
        0 4px 15px rgba(15, 23, 42, 0.035);
}

.profile-title {
    color: #0F172A;

    font-size: 25px;

    font-weight: 850;

    letter-spacing: -0.6px;
}

.profile-label {
    font-size: 10px;

    color: #64748B;

    text-transform: uppercase;

    letter-spacing: 1px;

    font-weight: 850;
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {
    border-radius: 9px;

    font-weight: 700;

    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
}


/* =========================================================
   SELECTBOX
   ========================================================= */

div[data-baseweb="select"] > div {
    border-radius: 10px !important;

    border-color: #CBD5E1 !important;

    background: white !important;
}


/* =========================================================
   DATAFRAME
   ========================================================= */

[data-testid="stDataFrame"] {
    border: 1px solid #E2E8F0;

    border-radius: 12px;

    overflow: hidden;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    border-top: 1px solid #E2E8F0;

    margin-top: 45px;

    padding-top: 17px;

    text-align: center;

    color: #94A3B8;

    font-size: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv("telco_churn_powerbi.csv")

    # --------------------------------------------------------
    # Clean column names
    # --------------------------------------------------------

    data.columns = (
        data.columns
        .str.strip()
    )

    # --------------------------------------------------------
    # Customer ID
    # --------------------------------------------------------

    if "customerID" not in data.columns:

        possible_id = [
            c for c in data.columns
            if c.lower() in [
                "customerid",
                "customer_id",
                "customer id"
            ]
        ]

        if possible_id:
            data["customerID"] = data[possible_id[0]]

    # --------------------------------------------------------
    # ChurnFlag
    # --------------------------------------------------------

    if "ChurnFlag" not in data.columns:

        if "Churn" in data.columns:

            data["ChurnFlag"] = (
                data["Churn"]
                .astype(str)
                .str.strip()
                .str.lower()
                .map({
                    "yes": 1,
                    "no": 0,
                    "1": 1,
                    "0": 0
                })
                .fillna(0)
            )

        else:

            data["ChurnFlag"] = 0

    # --------------------------------------------------------
    # Numeric columns
    # --------------------------------------------------------

    for column in [
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "ChurnProbability",
        "ChurnProbabilityPct",
        "CustomerSegment"
    ]:

        if column in data.columns:

            data[column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    # --------------------------------------------------------
    # Churn Probability
    # --------------------------------------------------------

    if "ChurnProbability" not in data.columns:

        if "ChurnProbabilityPct" in data.columns:

            data["ChurnProbability"] = (
                data["ChurnProbabilityPct"] / 100
            )

        else:

            data["ChurnProbability"] = data["ChurnFlag"].astype(float)

    # Keep probability between 0 and 1

    data["ChurnProbability"] = (
        data["ChurnProbability"]
        .fillna(0)
        .clip(0, 1)
    )

    # --------------------------------------------------------
    # Probability Percentage
    # --------------------------------------------------------

    data["ChurnProbabilityPct"] = (
        data["ChurnProbability"] * 100
    )

    # --------------------------------------------------------
    # Risk Level
    # --------------------------------------------------------

    if "RiskLevel" not in data.columns:

        data["RiskLevel"] = np.select(
            [
                data["ChurnProbability"] >= 0.70,
                data["ChurnProbability"] >= 0.50,
                data["ChurnProbability"] >= 0.35
            ],
            [
                "Critical",
                "High",
                "Medium"
            ],
            default="Low"
        )

    # --------------------------------------------------------
    # Segment Names
    # --------------------------------------------------------

    segment_mapping = {
        0: "New / Low-Engagement",
        1: "High-Value Loyal",
        2: "Long-Term Low-Spend",
        3: "High-Risk / At-Risk"
    }

    if "CustomerSegment" in data.columns:

        numeric_segment = pd.to_numeric(
            data["CustomerSegment"],
            errors="coerce"
        )

        data["Segment Name"] = (
            numeric_segment
            .map(segment_mapping)
            .fillna("Other")
        )

    elif "Segment Name" not in data.columns:

        data["Segment Name"] = "Other"

    # --------------------------------------------------------
    # Retention Recommendation
    # --------------------------------------------------------

    if "RetentionRecommendation" not in data.columns:

        data["RetentionRecommendation"] = np.select(
            [
                data["RiskLevel"] == "Critical",
                data["RiskLevel"] == "High",
                data["RiskLevel"] == "Medium"
            ],
            [
                "Immediate retention outreach and personalized offer",
                "Proactive retention campaign recommended",
                "Monitor engagement and provide targeted incentives"
            ],
            default="Maintain relationship and monitor behavior"
        )

    return data


# ============================================================
# LOAD DATA
# ============================================================

try:

    df = load_data()

except Exception as e:

    st.error(
        "Unable to load telco_churn_powerbi.csv. "
        "Make sure the CSV file is in the same GitHub repository "
        "as app.py."
    )

    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:

    st.session_state.page = "Executive Overview"


if "risk_quick_filter" not in st.session_state:

    st.session_state.risk_quick_filter = False


# ============================================================
# TOP BRAND
# ============================================================

st.markdown("""
<div class="brand-wrapper">

    <div class="brand-icon">
        ◆
    </div>

    <div>
        <div class="brand-name">
            Customer Intelligence
        </div>

        <div class="brand-subtitle">
            AI-Powered Retention Analytics
        </div>
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown(
    '<div class="nav-container">',
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

navigation = [
    ("Executive Overview", "▣"),
    ("Risk Analytics", "◉"),
    ("Customer Segments", "○"),
    ("Churn Drivers", "✦"),
    ("Customer Explorer", "⌕")
]

with nav1:

    if st.button(
        "▣  Executive Overview",
        key="nav_executive",
        use_container_width=True
    ):

        st.session_state.page = "Executive Overview"
        st.rerun()


with nav2:

    if st.button(
        "◉  Risk Analytics",
        key="nav_risk",
        use_container_width=True
    ):

        st.session_state.page = "Risk Analytics"
        st.rerun()


with nav3:

    if st.button(
        "○  Customer Segments",
        key="nav_segments",
        use_container_width=True
    ):

        st.session_state.page = "Customer Segments"
        st.rerun()


with nav4:

    if st.button(
        "✦  Churn Drivers",
        key="nav_drivers",
        use_container_width=True
    ):

        st.session_state.page = "Churn Drivers"
        st.rerun()


with nav5:

    if st.button(
        "⌕  Customer Explorer",
        key="nav_explorer",
        use_container_width=True
    ):

        st.session_state.page = "Customer Explorer"
        st.rerun()


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


page = st.session_state.page


# ============================================================
# QUICK ACTIONS
# ============================================================

st.markdown(
    '<div class="quick-label">Quick Actions</div>',
    unsafe_allow_html=True
)

q1, q2, q3 = st.columns([1.5, 1.2, 5])

with q1:

    if st.button(
        "⚠  High-Risk Customers",
        key="quick_risk",
        use_container_width=True
    ):

        st.session_state.page = "Customer Explorer"

        st.session_state.risk_quick_filter = True

        st.rerun()


with q2:

    if st.button(
        "↻  Reset Workspace",
        key="quick_reset",
        use_container_width=True
    ):

        st.session_state.page = "Executive Overview"

        st.session_state.risk_quick_filter = False

        st.rerun()


st.markdown(
    "<div style='height:8px'></div>",
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# COMMON CALCULATIONS
# ============================================================

total_customers = (
    df["customerID"]
    .nunique()
    if "customerID" in df.columns
    else len(df)
)

churned_customers = (
    df.loc[
        df["ChurnFlag"] == 1,
        "customerID"
    ].nunique()
    if "customerID" in df.columns
    else int(df["ChurnFlag"].sum())
)

churn_rate = (
    churned_customers / total_customers
    if total_customers > 0
    else 0
)

high_risk = (
    df[
        df["RiskLevel"].isin(
            ["High", "Critical"]
        )
    ]["customerID"].nunique()
    if "customerID" in df.columns
    else len(
        df[
            df["RiskLevel"].isin(
                ["High", "Critical"]
            )
        ]
    )
)

avg_probability = df[
    "ChurnProbability"
].mean()

at_risk = (
    df[
        df["ChurnProbability"] >= 0.35
    ]["customerID"].nunique()
    if "customerID" in df.columns
    else len(
        df[
            df["ChurnProbability"] >= 0.35
        ]
    )
)


# ============================================================
# PAGE HEADER
# ============================================================

page_meta = {

    "Executive Overview": (
        "CUSTOMER INTELLIGENCE",
        "Customer Churn Intelligence",
        "Retention command center for proactive customer management."
    ),

    "Risk Analytics": (
        "RISK MANAGEMENT",
        "Risk Analytics",
        "Explore predicted churn probability, risk tiers and priority populations."
    ),

    "Customer Segments": (
        "CUSTOMER STRATEGY",
        "Customer Segmentation",
        "Understand customer groups based on behavior and financial characteristics."
    ),

    "Churn Drivers": (
        "EXPLAINABLE AI",
        "Churn Drivers",
        "Understand which customer characteristics have the strongest model impact."
    ),

    "Customer Explorer": (
        "RETENTION OPERATIONS",
        "Customer Explorer",
        "Inspect individual customer risk, profile attributes and retention actions."
    )
}


eyebrow, title, subtitle = page_meta[page]


h1, h2 = st.columns([5, 1])

with h1:

    st.markdown(
        f"""
        <div class="page-header">

            <div class="eyebrow">
                {eyebrow}
            </div>

            <div class="page-title">
                {title}
            </div>

            <div class="page-subtitle">
                {subtitle}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with h2:

    st.markdown(
        """
        <div style="text-align:right; padding-top:18px;">
            <div class="status-pill">
                ● MODEL ACTIVE
                &nbsp;&nbsp;
                XGBoost · 0.841 AUC
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    TOTAL CUSTOMERS
                </div>

                <div class="kpi-value">
                    {total_customers:,}
                </div>

                <div class="kpi-description">
                    Active customer base
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    CHURN RATE
                </div>

                <div class="kpi-value">
                    {churn_rate:.1%}
                </div>

                <div class="kpi-description">
                    Historical churn
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    AT-RISK CUSTOMERS
                </div>

                <div class="kpi-value">
                    {at_risk:,}
                </div>

                <div class="kpi-description">
                    Probability ≥ 35%
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    HIGH / CRITICAL
                </div>

                <div class="kpi-value">
                    {high_risk:,}
                </div>

                <div class="kpi-description">
                    Priority customers
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c5:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    AVG MODEL RISK
                </div>

                <div class="kpi-value">
                    {avg_probability:.1%}
                </div>

                <div class="kpi-description">
                    Predicted probability
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # CHART SECTION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Customer population and contract-level churn behavior.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    with col1:

        risk_counts = (
            df["RiskLevel"]
            .value_counts()
            .reindex(
                [
                    "Critical",
                    "High",
                    "Medium",
                    "Low"
                ],
                fill_value=0
            )
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
            text="Customers",
            title="Customer Risk Distribution"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            height=390,
            margin=dict(
                l=20,
                r=20,
                t=55,
                b=20
            ),
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
            margin=dict(
                l=20,
                r=20,
                t=55,
                b=20
            ),
            xaxis_title=None,
            yaxis_title="Churn Rate (%)",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # INSIGHT
    # --------------------------------------------------------

    month_contract = (
        df[
            df["Contract"] == "Month-to-month"
        ]["ChurnFlag"].mean()
        if "Contract" in df.columns
        else 0
    )

    st.markdown(
        f"""
        <div class="insight-card">

            <div class="insight-title">
                ✦ Executive Insight
            </div>

            <div class="insight-text">

                Customers on month-to-month contracts show a
                <b>{month_contract:.1%}</b> churn rate.

                The ML system currently flags
                <b>{at_risk:,}</b> customers above the
                35% intervention threshold for proactive
                retention attention.

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PAGE 2 — RISK ANALYTICS
# ============================================================

elif page == "Risk Analytics":

    f1, f2, f3 = st.columns(3)


    with f1:

        selected_risk = st.multiselect(
            "Risk Level",
            [
                "Critical",
                "High",
                "Medium",
                "Low"
            ],
            default=[
                "Critical",
                "High"
            ]
        )


    with f2:

        contracts = sorted(
            df["Contract"]
            .dropna()
            .astype(str)
            .unique()
        )

        selected_contract = st.multiselect(
            "Contract",
            contracts,
            default=contracts
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
        (df["RiskLevel"].isin(selected_risk))
        &
        (df["Contract"].isin(selected_contract))
        &
        (df["ChurnProbability"] >= min_probability)
    ].copy()


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
        (
            f"{filtered['ChurnProbability'].mean():.1%}"
            if len(filtered)
            else "0%"
        )
    )


    c3.metric(
        "Average Monthly Charges",
        (
            f"${filtered['MonthlyCharges'].mean():,.2f}"
            if len(filtered)
            else "$0"
        )
    )


    # --------------------------------------------------------
    # RISK MAP
    # --------------------------------------------------------

    if len(filtered) > 0:

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
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No customers match the selected filters."
        )


# ============================================================
# PAGE 3 — CUSTOMER SEGMENTS
# ============================================================

elif page == "Customer Segments":

    # --------------------------------------------------------
    # GUARANTEE SEGMENT COLUMN
    # --------------------------------------------------------

    if "CustomerSegment" in df.columns:

        segment_mapping = {
            0: "New / Low-Engagement",
            1: "High-Value Loyal",
            2: "Long-Term Low-Spend",
            3: "High-Risk / At-Risk"
        }

        numeric_segment = pd.to_numeric(
            df["CustomerSegment"],
            errors="coerce"
        )

        df["Segment Name"] = (
            numeric_segment
            .map(segment_mapping)
            .fillna("Other")
        )

    elif "Segment Name" not in df.columns:

        df["Segment Name"] = "Other"


    # --------------------------------------------------------
    # SAFE GROUPBY
    # --------------------------------------------------------

    segment_data = (
        df[
            [
                "Segment Name",
                "customerID",
                "tenure",
                "MonthlyCharges",
                "ChurnFlag"
            ]
        ]
        .copy()
        .groupby(
            "Segment Name",
            dropna=False
        )
        .agg(
            Customers=("customerID", "count"),
            AvgTenure=("tenure", "mean"),
            AvgMonthlyCharges=(
                "MonthlyCharges",
                "mean"
            ),
            ChurnRate=(
                "ChurnFlag",
                "mean"
            )
        )
        .reset_index()
    )


    segment_data["ChurnRate"] = (
        segment_data["ChurnRate"] * 100
    )


    # --------------------------------------------------------
    # CHARTS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        fig = px.bar(
            segment_data,
            x="Segment Name",
            y="Customers",
            text="Customers",
            title="Customer Distribution by Segment"
        )

        fig.update_traces(
            textposition="outside"
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
            text=segment_data["ChurnRate"].round(1),
            title="Churn Rate by Segment"
        )

        fig.update_traces(
            texttemplate="%{text}%",
            textposition="outside"
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


    # --------------------------------------------------------
    # TABLE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Segment Profile</div>',
        unsafe_allow_html=True
    )

    display_segments = segment_data.copy()

    display_segments[
        "AvgTenure"
    ] = display_segments[
        "AvgTenure"
    ].round(1)

    display_segments[
        "AvgMonthlyCharges"
    ] = display_segments[
        "AvgMonthlyCharges"
    ].round(2)

    display_segments[
        "ChurnRate"
    ] = display_segments[
        "ChurnRate"
    ].round(1)

    st.dataframe(
        display_segments,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 4 — CHURN DRIVERS
# ============================================================

elif page == "Churn Drivers":

    st.markdown(
        '<div class="section-subtitle">Model features ranked by their overall contribution to churn predictions.</div>',
        unsafe_allow_html=True
    )

    try:

        importance = pd.read_csv(
            "shap_feature_importance.csv"
        )

        importance.columns = (
            importance.columns
            .str.strip()
        )

        if (
            "Feature" not in importance.columns
            or
            "MeanAbsSHAP" not in importance.columns
        ):

            st.error(
                "The SHAP file must contain "
                "'Feature' and 'MeanAbsSHAP' columns."
            )

        else:

            importance["MeanAbsSHAP"] = pd.to_numeric(
                importance["MeanAbsSHAP"],
                errors="coerce"
            )

            importance = (
                importance
                .dropna(
                    subset=[
                        "Feature",
                        "MeanAbsSHAP"
                    ]
                )
                .sort_values(
                    "MeanAbsSHAP",
                    ascending=True
                )
            )


            top = importance.tail(12)


            # ------------------------------------------------
            # CHART
            # ------------------------------------------------

            fig = px.bar(
                top,
                x="MeanAbsSHAP",
                y="Feature",
                orientation="h",
                text="MeanAbsSHAP",
                title="Top Factors Influencing Churn"
            )

            fig.update_traces(
                texttemplate="%{text:.3f}",
                textposition="outside"
            )

            fig.update_layout(
                template="plotly_white",
                height=560,
                xaxis_title="Mean |SHAP Value|",
                yaxis_title=None,
                margin=dict(
                    l=20,
                    r=50,
                    t=60,
                    b=30
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


            # ------------------------------------------------
            # INSIGHT
            # ------------------------------------------------

            top_features = (
                importance
                .sort_values(
                    "MeanAbsSHAP",
                    ascending=False
                )
                .head(3)["Feature"]
                .tolist()
            )


            feature_text = ", ".join(
                top_features
            )


            st.markdown(
                f"""
                <div class="insight-card">

                    <div class="insight-title">
                        ✦ Model Interpretation
                    </div>

                    <div class="insight-text">

                        The strongest model drivers are
                        <b>{feature_text}</b>.

                        These variables have the greatest
                        overall influence on the model's
                        churn predictions and should receive
                        attention when designing customer
                        retention strategies.

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            # ------------------------------------------------
            # TABLE
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">Feature Importance</div>',
                unsafe_allow_html=True
            )


            feature_table = (
                importance
                .sort_values(
                    "MeanAbsSHAP",
                    ascending=False
                )
                .head(15)
                .copy()
            )


            feature_table[
                "MeanAbsSHAP"
            ] = feature_table[
                "MeanAbsSHAP"
            ].round(4)


            st.dataframe(
                feature_table,
                use_container_width=True,
                hide_index=True
            )


    except FileNotFoundError:

        st.warning(
            "shap_feature_importance.csv was not found. "
            "Upload it to the same GitHub repository as app.py."
        )

    except Exception as e:

        st.error(
            "Unable to load the SHAP feature importance data."
        )


# ============================================================
# PAGE 5 — CUSTOMER EXPLORER
# ============================================================

elif page == "Customer Explorer":

    # --------------------------------------------------------
    # QUICK FILTER
    # --------------------------------------------------------

    if st.session_state.risk_quick_filter:

        explorer_df = df[
            df["ChurnProbability"] >= 0.35
        ].copy()

        st.info(
            f"Showing {len(explorer_df):,} customers "
            "above the 35% retention threshold."
        )

        if st.button(
            "Show All Customers",
            key="show_all_customers"
        ):

            st.session_state.risk_quick_filter = False

            st.rerun()

    else:

        explorer_df = df.copy()


    # --------------------------------------------------------
    # CUSTOMER SELECTOR
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Search Customer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Select a customer from the dropdown to inspect their complete profile.</div>',
        unsafe_allow_html=True
    )


    customer_ids = sorted(
        explorer_df[
            "customerID"
        ]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )


    if len(customer_ids) == 0:

        st.warning(
            "No customer IDs are available."
        )

        st.stop()


    customer_id = st.selectbox(
        "Select Customer ID",
        customer_ids,
        index=0,
        key="customer_selector"
    )


    # --------------------------------------------------------
    # FIND CUSTOMER
    # --------------------------------------------------------

    matching = df[
        df["customerID"].astype(str)
        == str(customer_id)
    ]


    if len(matching) == 0:

        st.error(
            "Customer could not be found."
        )

        st.stop()


    customer = matching.iloc[0]


    probability = float(
        customer["ChurnProbability"]
    )


    # --------------------------------------------------------
    # RISK CLASS
    # --------------------------------------------------------

    if probability >= 0.70:

        risk_class = "risk-critical"

        risk_label = "Critical Risk"

    elif probability >= 0.50:

        risk_class = "risk-high"

        risk_label = "High Risk"

    elif probability >= 0.35:

        risk_class = "risk-medium"

        risk_label = "Medium Risk"

    else:

        risk_class = "risk-low"

        risk_label = "Low Risk"


    # --------------------------------------------------------
    # CUSTOMER HEADER
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="profile-card">

            <div class="profile-label">
                CUSTOMER PROFILE
            </div>

            <div class="profile-title">
                Customer {customer_id}
            </div>

            <div style="margin-top:12px;">

                <span style="
                    display:inline-block;
                    padding:7px 12px;
                    border-radius:999px;
                    background:#EFF6FF;
                    color:#2563EB;
                    font-size:11px;
                    font-weight:800;
                ">
                    {risk_label}
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # CUSTOMER RISK
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="{risk_class}" style="margin-top:15px;">

            <div class="risk-label">
                PREDICTED CHURN RISK
            </div>

            <div class="risk-customer">
                {probability:.1%}
            </div>

            <div style="
                margin-top:5px;
                color:#64748B;
                font-size:12px;
            ">
                Risk Level:
                <b>{customer["RiskLevel"]}</b>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # CUSTOMER METRICS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Customer Metrics</div>',
        unsafe_allow_html=True
    )


    m1, m2, m3, m4 = st.columns(4)


    with m1:

        tenure_value = customer.get(
            "tenure",
            0
        )

        st.metric(
            "Tenure",
            f"{tenure_value} months"
        )


    with m2:

        monthly = customer.get(
            "MonthlyCharges",
            0
        )

        st.metric(
            "Monthly Charges",
            f"${float(monthly):,.2f}"
        )


    with m3:

        total = customer.get(
            "TotalCharges",
            0
        )

        try:

            total = float(total)

        except:

            total = 0


        st.metric(
            "Total Charges",
            f"${total:,.2f}"
        )


    with m4:

        churn_value = customer.get(
            "Churn",
            "Unknown"
        )

        st.metric(
            "Historical Churn",
            str(churn_value)
        )


    # --------------------------------------------------------
    # CUSTOMER DETAILS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Customer Details</div>',
        unsafe_allow_html=True
    )


    details = {}


    desired_columns = [
        "customerID",
        "Contract",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "InternetService",
        "PaymentMethod",
        "Churn",
        "CustomerSegment",
        "Segment Name",
        "RiskLevel",
        "ChurnProbabilityPct"
    ]


    for column in desired_columns:

        if column in df.columns:

            value = customer[column]

            if column == "ChurnProbabilityPct":

                value = f"{float(value):.1f}%"

            details[column] = value


    details_df = pd.DataFrame(
        list(details.items()),
        columns=[
            "Attribute",
            "Value"
        ]
    )


    st.dataframe(
        details_df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # RETENTION RECOMMENDATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )


    recommendation = customer.get(
        "RetentionRecommendation",
        "Monitor customer behavior and maintain engagement."
    )


    st.success(
        recommendation
    )


    # --------------------------------------------------------
    # PRIORITY CUSTOMERS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Priority Customer List</div>',
        unsafe_allow_html=True
    )


    priority = (
        df[
            df["ChurnProbability"] >= 0.35
        ]
        .sort_values(
            "ChurnProbability",
            ascending=False
        )
        .copy()
    )


    priority_columns = [
        "customerID",
        "Contract",
        "tenure",
        "MonthlyCharges",
        "ChurnProbabilityPct",
        "RiskLevel",
        "RetentionRecommendation"
    ]


    priority_columns = [
        c for c in priority_columns
        if c in priority.columns
    ]


    st.dataframe(
        priority[
            priority_columns
        ].head(50),
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    st.download_button(
        "↓  Export Priority Customers",
        data=priority[
            priority_columns
        ].to_csv(index=False),
        file_name="priority_customer_list.csv",
        mime="text/csv",
        use_container_width=False
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        Customer Churn Intelligence
        &nbsp;•&nbsp;
        XGBoost
        &nbsp;•&nbsp;
        K-Means
        &nbsp;•&nbsp;
        SHAP
        &nbsp;•&nbsp;
        Streamlit

    </div>
    """,
    unsafe_allow_html=True
)
