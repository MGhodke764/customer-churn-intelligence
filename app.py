import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ChurnIQ | Customer Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   GLOBAL
===================================================== */

.stApp {
    background: #F6F8FC;
    color: #0F172A;
}

.block-container {
    max-width: 1500px;
    padding-top: 2.2rem !important;
    padding-bottom: 3rem !important;
    padding-left: 2.5rem !important;
    padding-right: 2.5rem !important;
}

#MainMenu,
footer,
[data-testid="stDecoration"] {
    visibility: hidden;
}


/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0B1220 0%,
        #111827 55%,
        #0F172A 100%
    );
    border-right: 1px solid #1E293B;
}

section[data-testid="stSidebar"] > div {
    padding: 1.2rem 1rem;
}


/* Brand */

.brand {
    padding: 5px 4px 24px 4px;
}

.brand-row {
    display: flex;
    align-items: center;
}

.brand-mark {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;

    background: linear-gradient(
        135deg,
        #2563EB,
        #60A5FA
    );

    color: white;
    font-size: 19px;
    font-weight: 900;

    box-shadow:
        0 8px 20px rgba(37,99,235,.28);
}

.brand-name {
    margin-left: 10px;
    color: #FFFFFF;
    font-size: 20px;
    font-weight: 850;
    letter-spacing: -.6px;
}

.brand-sub {
    color: #94A3B8;
    font-size: 10px;
    margin-top: 9px;
    letter-spacing: .3px;
}


/* Sidebar labels */

.nav-label {
    color: #64748B;
    font-size: 9px;
    font-weight: 850;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 14px 0 8px 3px;
}


/* Sidebar buttons */

section[data-testid="stSidebar"] .stButton {
    margin-bottom: 5px;
}

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 44px;

    border-radius: 11px;

    border: 1px solid #243247;

    background: #151F31;

    color: #CBD5E1;

    text-align: left;

    font-size: 12px;
    font-weight: 700;

    padding: 0.55rem 0.8rem;

    box-shadow: none;

    transition:
        background .2s ease,
        border .2s ease,
        transform .2s ease,
        color .2s ease;
}


/* Hover */

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #1E3A66;
    border-color: #3B82F6;
    color: #FFFFFF;
    transform: translateX(3px);
}


/* Quick action buttons */

section[data-testid="stSidebar"] .stButton > button[kind="secondary"] {
    color: #CBD5E1;
}


/* Sidebar model card */

.side-card {
    margin-top: 24px;

    padding: 15px;

    border-radius: 14px;

    border: 1px solid #263449;

    background:
        linear-gradient(
            145deg,
            rgba(37,99,235,.10),
            rgba(255,255,255,.025)
        );
}

.side-card-title {
    color: #64748B;
    font-size: 9px;
    font-weight: 850;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.side-model {
    color: #F8FAFC;
    font-size: 13px;
    font-weight: 750;
    margin-top: 9px;
}

.side-row {
    display: flex;
    justify-content: space-between;

    padding-top: 10px;

    color: #94A3B8;

    font-size: 10px;
}

.side-row b {
    color: #E2E8F0;
}


/* =====================================================
   HEADER
===================================================== */

.product-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;

    padding: 8px 0 22px;

    border-bottom: 1px solid #E2E8F0;

    margin-bottom: 26px;
}

.eyebrow {
    color: #2563EB;

    font-size: 10px;

    font-weight: 850;

    letter-spacing: 1.7px;

    text-transform: uppercase;

    margin-bottom: 8px;
}

.main-title {
    color: #0F172A;

    font-size: 34px;

    line-height: 1.08;

    font-weight: 850;

    letter-spacing: -1.3px;

    margin: 0;
}

.main-subtitle {
    color: #64748B;

    font-size: 13px;

    margin-top: 9px;
}

.status-pill {
    background: #ECFDF5;

    border: 1px solid #A7F3D0;

    color: #047857;

    border-radius: 999px;

    padding: 8px 13px;

    font-size: 10px;

    font-weight: 850;

    white-space: nowrap;
}


/* =====================================================
   KPI CARDS
===================================================== */

.kpi-card {
    background: #FFFFFF;

    border: 1px solid #E2E8F0;

    border-radius: 15px;

    padding: 18px;

    min-height: 130px;

    box-shadow:
        0 5px 18px rgba(15,23,42,.04);

    transition: .2s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);

    box-shadow:
        0 10px 26px rgba(15,23,42,.08);
}

.kpi-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.kpi-label {
    color: #64748B;

    font-size: 9px;

    font-weight: 850;

    letter-spacing: .9px;
}

.kpi-icon {
    width: 30px;
    height: 30px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #EFF6FF;

    color: #2563EB;

    border-radius: 9px;

    font-weight: 850;
}

.kpi-value {
    color: #0F172A;

    font-size: 27px;

    font-weight: 850;

    letter-spacing: -.8px;

    margin-top: 12px;
}

.kpi-description {
    color: #94A3B8;

    font-size: 10px;

    margin-top: 4px;
}


/* =====================================================
   SECTIONS
===================================================== */

.section-title {
    font-size: 19px;

    font-weight: 850;

    color: #0F172A;

    letter-spacing: -.35px;

    margin-top: 30px;

    margin-bottom: 12px;
}

.section-subtitle {
    color: #64748B;

    font-size: 12px;

    margin-top: -6px;

    margin-bottom: 16px;
}


/* =====================================================
   INSIGHT
===================================================== */

.insight-card {
    background:
        linear-gradient(
            135deg,
            #EFF6FF,
            #F8FAFC
        );

    border: 1px solid #BFDBFE;

    border-radius: 15px;

    padding: 18px 20px;
}

.insight-title {
    color: #1D4ED8;

    font-size: 10px;

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


/* =====================================================
   RISK CARDS
===================================================== */

.risk-critical,
.risk-high,
.risk-medium,
.risk-low {
    border-radius: 14px;

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
    background: #EFF6FF;
    border-color: #BFDBFE;
}


/* =====================================================
   PROFILE
===================================================== */

.profile-label {
    color: #64748B;

    font-size: 9px;

    font-weight: 850;

    letter-spacing: 1.2px;

    text-transform: uppercase;
}

.profile-title {
    color: #0F172A;

    font-size: 25px;

    font-weight: 850;

    margin-top: 6px;
}


/* =====================================================
   STREAMLIT INPUTS
===================================================== */

div[data-baseweb="select"] > div {
    border-radius: 10px !important;

    border-color: #CBD5E1 !important;
}

div[data-baseweb="select"] > div:focus-within {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 1px #2563EB !important;
}

.stSlider {
    padding-top: 4px;
}


/* =====================================================
   NORMAL BUTTONS
===================================================== */

.stButton > button {
    border-radius: 10px;

    font-weight: 700;

    border: 1px solid #CBD5E1;

    background: #FFFFFF;

    color: #1E293B;

    transition: .2s ease;
}

.stButton > button:hover {
    border-color: #2563EB;

    color: #2563EB;

    background: #EFF6FF;
}


/* =====================================================
   DOWNLOAD
===================================================== */

.stDownloadButton > button {
    border-radius: 10px;

    background: #2563EB;

    border: 1px solid #2563EB;

    color: white;

    font-weight: 750;
}

.stDownloadButton > button:hover {
    background: #1D4ED8;

    border-color: #1D4ED8;

    color: white;
}


/* =====================================================
   METRIC
===================================================== */

[data-testid="stMetric"] {
    background: white;

    border: 1px solid #E2E8F0;

    border-radius: 13px;

    padding: 15px;
}


/* =====================================================
   DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {
    border: 1px solid #E2E8F0;

    border-radius: 12px;
}


/* =====================================================
   FOOTER
===================================================== */

.footer {
    border-top: 1px solid #E2E8F0;

    margin-top: 40px;

    padding-top: 17px;

    text-align: center;

    color: #94A3B8;

    font-size: 10px;

    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    data = pd.read_csv("telco_churn_powerbi.csv")

    # Segment names
    if "CustomerSegment" in data.columns:

        segment_mapping = {
            0: "New / Low-Engagement",
            1: "High-Value Loyal",
            2: "Long-Term Low-Spend",
            3: "High-Risk / At-Risk"
        }

        data["Segment Name"] = (
            pd.to_numeric(
                data["CustomerSegment"],
                errors="coerce"
            )
            .map(segment_mapping)
            .fillna("Other")
        )

    else:

        data["Segment Name"] = "Other"

    return data


df = load_data()


# =========================================================
# BASIC VALIDATION
# =========================================================

required_columns = [
    "customerID",
    "ChurnFlag",
    "RiskLevel",
    "ChurnProbability",
    "Contract",
    "tenure",
    "MonthlyCharges"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:

    st.error(
        "Missing columns in telco_churn_powerbi.csv: "
        + ", ".join(missing_columns)
    )

    st.stop()


# =========================================================
# COMMON CALCULATIONS
# =========================================================

total_customers = df["customerID"].nunique()

churned_customers = df.loc[
    df["ChurnFlag"] == 1,
    "customerID"
].nunique()

churn_rate = (
    churned_customers / total_customers
    if total_customers > 0
    else 0
)

high_risk = df[
    df["RiskLevel"].isin(["High", "Critical"])
]["customerID"].nunique()

avg_probability = df["ChurnProbability"].mean()

at_risk = df[
    df["ChurnProbability"] >= 0.35
]["customerID"].nunique()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    # BRAND
    st.markdown("""
    <div class="brand">

        <div class="brand-row">

            <div class="brand-mark">
                ◈
            </div>

            <div class="brand-name">
                CHURNIQ
            </div>

        </div>

        <div class="brand-sub">
            Customer Intelligence Platform
        </div>

    </div>
    """, unsafe_allow_html=True)


    # WORKSPACE
    st.markdown(
        '<div class="nav-label">Workspace</div>',
        unsafe_allow_html=True
    )


    nav_items = [
        ("Executive Overview", "▦"),
        ("Risk Analytics", "◉"),
        ("Customer Segments", "◌"),
        ("Churn Drivers", "✦"),
        ("Customer Explorer", "⌕")
    ]


    if "page" not in st.session_state:
        st.session_state.page = "Executive Overview"


    for page_name, icon in nav_items:

        if st.button(
            f"{icon}   {page_name}",
            key=f"nav_{page_name}",
            use_container_width=True
        ):

            st.session_state.page = page_name

            st.session_state.risk_quick_filter = False

            st.rerun()


    # QUICK ACTIONS
    st.markdown(
        '<div class="nav-label" style="margin-top:22px;">Quick Actions</div>',
        unsafe_allow_html=True
    )


    if st.button(
        "⚠   High-Risk Customers",
        key="high_risk_action",
        use_container_width=True
    ):

        st.session_state.page = "Customer Explorer"

        st.session_state.risk_quick_filter = True

        st.rerun()


    if st.button(
        "↻   Reset Workspace",
        key="reset_workspace",
        use_container_width=True
    ):

        st.session_state.page = "Executive Overview"

        st.session_state.risk_quick_filter = False

        st.rerun()


    # MODEL CARD
    st.markdown("""
    <div class="side-card">

        <div class="side-card-title">
            Model Status
        </div>

        <div class="side-model">
            ● XGBoost Classifier
        </div>

        <div class="side-row">
            <span>ROC-AUC</span>
            <b>0.841</b>
        </div>

        <div class="side-row">
            <span>Threshold</span>
            <b>35%</b>
        </div>

        <div class="side-row">
            <span>Explainability</span>
            <b>SHAP</b>
        </div>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div style="height:28px"></div>

    <div style="
        color:#64748B;
        font-size:9px;
        line-height:1.8;
        letter-spacing:.7px;
    ">
        DATA SCIENCE PORTFOLIO<br>
        CUSTOMER RETENTION ANALYTICS
    </div>
    """, unsafe_allow_html=True)


page = st.session_state.page


# =========================================================
# PAGE HEADER
# =========================================================

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
        "Behavioral segments built from customer engagement and financial characteristics."
    ),

    "Churn Drivers": (
        "MODEL EXPLAINABILITY",
        "Churn Drivers",
        "Understand which customer characteristics influence churn predictions."
    ),

    "Customer Explorer": (
        "CUSTOMER 360",
        "Customer Explorer",
        "Inspect individual customer risk and recommended retention actions."
    )
}


eyebrow, title, subtitle = page_meta[page]


st.markdown(
    f"""
    <div class="product-header">

        <div>

            <div class="eyebrow">
                {eyebrow}
            </div>

            <div class="main-title">
                {title}
            </div>

            <div class="main-subtitle">
                {subtitle}
            </div>

        </div>

        <div class="status-pill">
            ● MODEL ONLINE
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    k1, k2, k3, k4, k5 = st.columns(5)


    # KPI 1
    with k1:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-top">
                    <div class="kpi-label">
                        TOTAL CUSTOMERS
                    </div>

                    <div class="kpi-icon">
                        ◉
                    </div>
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


    # KPI 2
    with k2:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-top">
                    <div class="kpi-label">
                        CHURN RATE
                    </div>

                    <div class="kpi-icon">
                        %
                    </div>
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


    # KPI 3
    with k3:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-top">
                    <div class="kpi-label">
                        AT-RISK CUSTOMERS
                    </div>

                    <div class="kpi-icon">
                        !
                    </div>
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


    # KPI 4
    with k4:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-top">
                    <div class="kpi-label">
                        HIGH / CRITICAL
                    </div>

                    <div class="kpi-icon">
                        ⚠
                    </div>
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


    # KPI 5
    with k5:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-top">
                    <div class="kpi-label">
                        AVG MODEL RISK
                    </div>

                    <div class="kpi-icon">
                        ◇
                    </div>
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


    # SECTION
    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Portfolio-level view of customer risk and contract behavior.</div>',
        unsafe_allow_html=True
    )


    c1, c2 = st.columns(2)


    # RISK DISTRIBUTION
    with c1:

        risk_distribution = (
            df["RiskLevel"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Medium", "Low"]
            )
            .fillna(0)
            .reset_index()
        )

        risk_distribution.columns = [
            "RiskLevel",
            "Customers"
        ]

        fig = px.bar(
            risk_distribution,
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
            height=420,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            ),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # CONTRACT CHURN
    with c2:

        contract_churn = (
            df.groupby("Contract")["ChurnFlag"]
            .mean()
            .mul(100)
            .reset_index()
        )

        contract_churn.columns = [
            "Contract",
            "ChurnRate"
        ]

        fig = px.bar(
            contract_churn,
            x="Contract",
            y="ChurnRate",
            text="ChurnRate",
            title="Churn Rate by Contract"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            height=420,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            ),
            yaxis_title="Churn Rate (%)",
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # EXECUTIVE INSIGHT
    st.markdown(
        '<div class="section-title">Executive Insight</div>',
        unsafe_allow_html=True
    )


    month_contract = df[
        df["Contract"] == "Month-to-month"
    ]["ChurnFlag"].mean()


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
                <b>35% intervention threshold</b> for proactive
                retention attention.

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# PAGE 2 — RISK ANALYTICS
# =========================================================

elif page == "Risk Analytics":

    st.markdown(
        '<div class="section-title">Risk Filters</div>',
        unsafe_allow_html=True
    )


    f1, f2, f3 = st.columns(3)


    with f1:

        selected_risk = st.multiselect(
            "Risk Level",
            ["Critical", "High", "Medium", "Low"],
            default=["Critical", "High"]
        )


    with f2:

        contracts = sorted(
            df["Contract"]
            .dropna()
            .unique()
            .tolist()
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
        df["RiskLevel"].isin(selected_risk)
        &
        df["Contract"].isin(selected_contract)
        &
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
        if len(filtered)
        else "0%"
    )


    c3.metric(
        "Average Monthly Charges",
        f"${filtered['MonthlyCharges'].mean():,.2f}"
        if len(filtered)
        else "$0"
    )


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

        st.warning(
            "No customers match the selected filters."
        )


# =========================================================
# PAGE 3 — CUSTOMER SEGMENTS
# =========================================================

elif page == "Customer Segments":

    segment_data = (
        df.groupby(
            "Segment Name",
            dropna=False
        )
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
            text="Customers",
            title="Customer Distribution by Segment"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            height=430,
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
            text="ChurnRate",
            title="Churn Rate by Segment"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            height=430,
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
        '<div class="section-title">What Drives Customer Churn?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">SHAP-based model explainability showing the strongest churn predictors.</div>',
        unsafe_allow_html=True
    )


    try:

        importance = pd.read_csv(
            "shap_feature_importance.csv"
        )

        required_shap = [
            "Feature",
            "MeanAbsSHAP"
        ]

        if not all(
            col in importance.columns
            for col in required_shap
        ):

            st.error(
                "shap_feature_importance.csv must contain "
                "Feature and MeanAbsSHAP columns."
            )

        else:

            importance = importance.sort_values(
                "MeanAbsSHAP",
                ascending=True
            )

            top = importance.tail(15)


            fig = px.bar(
                top,
                x="MeanAbsSHAP",
                y="Feature",
                orientation="h",
                text="MeanAbsSHAP",
                title="Top 15 Factors Influencing Customer Churn"
            )

            fig.update_traces(
                texttemplate="%{text:.3f}",
                textposition="outside"
            )

            fig.update_layout(
                template="plotly_white",
                height=650,
                xaxis_title="Mean |SHAP Value|",
                yaxis_title=None
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


            st.info(
                "Higher Mean |SHAP Value| indicates greater overall "
                "influence on the model's churn predictions."
            )


            st.markdown(
                '<div class="section-title">Feature Importance Table</div>',
                unsafe_allow_html=True
            )

            st.dataframe(
                importance
                .sort_values(
                    "MeanAbsSHAP",
                    ascending=False
                )
                .head(15)
                .round(4),
                use_container_width=True,
                hide_index=True
            )


    except FileNotFoundError:

        st.error(
            "Could not find shap_feature_importance.csv."
        )

    except Exception as e:

        st.error(
            f"Unable to load SHAP data: {e}"
        )


# =========================================================
# PAGE 5 — CUSTOMER EXPLORER
# =========================================================

elif page == "Customer Explorer":

    if "risk_quick_filter" not in st.session_state:
        st.session_state.risk_quick_filter = False


    # FILTERED CUSTOMER LIST

    if st.session_state.risk_quick_filter:

        explorer_df = df[
            df["ChurnProbability"] >= 0.35
        ].copy()

        st.info(
            f"Showing {len(explorer_df):,} customers "
            "above the 35% retention threshold."
        )

        if st.button(
            "← Show All Customers",
            key="show_all_customers"
        ):

            st.session_state.risk_quick_filter = False

            st.rerun()

    else:

        explorer_df = df.copy()


    # CUSTOMER ID DROPDOWN

    st.markdown(
        '<div class="section-title">Search Customer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Select a Customer ID from the available customer records.</div>',
        unsafe_allow_html=True
    )


    customer_ids = sorted(
        explorer_df["customerID"]
        .dropna()
        .unique()
        .tolist()
    )


    if not customer_ids:

        st.warning(
            "No customers match the current filter."
        )

        st.stop()


    customer_id = st.selectbox(
        "Customer ID",
        customer_ids,
        key="customer_selector"
    )


    customer = df[
        df["customerID"] == customer_id
    ].iloc[0]


    probability = float(
        customer["ChurnProbability"]
    )


    # RISK CLASS

    if probability >= 0.70:

        risk_class = "risk-critical"

    elif probability >= 0.50:

        risk_class = "risk-high"

    elif probability >= 0.35:

        risk_class = "risk-medium"

    else:

        risk_class = "risk-low"


    # CUSTOMER RISK PROFILE

    st.markdown(
        f"""
        <div class="{risk_class}">

            <div class="profile-label">
                CUSTOMER RISK PROFILE
            </div>

            <div class="profile-title">
                Customer {customer_id}
            </div>

            <div style="
                margin-top:12px;
                font-size:14px;
                color:#334155;
            ">

                <b>Predicted Churn Probability:</b>
                {probability:.1%}

                &nbsp;&nbsp;&nbsp;

                <b>Risk Level:</b>
                {customer["RiskLevel"]}

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # CUSTOMER PROFILE

    st.markdown(
        '<div class="section-title">Customer Profile</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "Tenure",
            f"{customer['tenure']} months"
        )


    with c2:

        st.metric(
            "Monthly Charges",
            f"${customer['MonthlyCharges']:.2f}"
        )


    with c3:

        st.metric(
            "Contract",
            str(customer["Contract"])
        )


    with c4:

        internet_service = (
            str(customer["InternetService"])
            if "InternetService" in customer.index
            else "N/A"
        )

        st.metric(
            "Internet Service",
            internet_service
        )


    # RETENTION RECOMMENDATION

    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )


    recommendation = (
        customer["RetentionRecommendation"]
        if "RetentionRecommendation" in customer.index
        else "Review customer engagement and offer a personalized retention plan."
    )


    st.success(
        str(recommendation)
    )


    # PRIORITY LIST

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
        "ChurnProbability",
        "RiskLevel",
        "RetentionRecommendation"
    ]


    available_columns = [
        col
        for col in priority_columns
        if col in priority.columns
    ]


    st.dataframe(
        priority[
            available_columns
        ].head(50),
        use_container_width=True,
        hide_index=True
    )


    # DOWNLOAD

    st.download_button(
        "↓  Export Priority Customers",
        data=priority[
            available_columns
        ].to_csv(index=False),
        file_name="priority_customer_list.csv",
        mime="text/csv",
        key="download_priority"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        <b>CHURNIQ</b> • CUSTOMER CHURN INTELLIGENCE
        <br>
        XGBoost • K-Means • SHAP • Streamlit

    </div>
    """,
    unsafe_allow_html=True
            )
