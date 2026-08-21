import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

/* ================= GLOBAL ================= */

.stApp {
    background: #F6F8FC;
    color: #0F172A;
}

.block-container {
    padding-top: 5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1500px;
}

#MainMenu,
footer,
[data-testid="stDecoration"] {
    visibility: hidden;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A1020 0%, #111827 100%);
    border-right: 1px solid #1E293B;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}

section[data-testid="stSidebar"] * {
    color: #E5E7EB;
}

.brand {
    padding: 8px 5px 25px;
}

.brand-mark {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    border-radius: 11px;
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: white;
    font-size: 18px;
    font-weight: 900;
    margin-right: 9px;
}

.brand-name {
    color: white;
    font-size: 21px;
    font-weight: 850;
    letter-spacing: -0.6px;
}

.brand-sub {
    color: #94A3B8;
    font-size: 11px;
    margin-top: 8px;
}

.nav-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    margin: 14px 0 8px 3px;
}

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 43px;
    text-align: left;
    border: 1px solid transparent;
    border-radius: 10px;
    background: transparent;
    color: #CBD5E1;
    font-weight: 600;
    font-size: 13px;
    padding: 0.55rem 0.8rem;
    margin: 2px 0;
    transition: all .2s ease;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #1B2638;
    border-color: #334155;
    color: white;
    transform: translateX(2px);
}

.side-card {
    margin-top: 20px;
    padding: 15px;
    border: 1px solid #263449;
    background: rgba(255,255,255,.035);
    border-radius: 13px;
}

.side-card-title {
    color: #94A3B8;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 800;
}

.side-model {
    color: white;
    font-size: 14px;
    font-weight: 700;
    margin-top: 8px;
}

.side-row {
    display: flex;
    justify-content: space-between;
    padding-top: 10px;
    font-size: 11px;
    color: #94A3B8;
}

.side-row b {
    color: #E2E8F0;
}

/* ================= HEADER ================= */

.product-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 10px 0 23px;
    border-bottom: 1px solid #E2E8F0;
    margin-bottom: 26px;
}

.eyebrow {
    color: #2563EB;
    font-size: 10px;
    font-weight: 850;
    text-transform: uppercase;
    letter-spacing: 1.7px;
    margin-bottom: 9px;
}

.main-title {
    color: #0F172A;
    font-size: 35px;
    line-height: 1.05;
    font-weight: 850;
    letter-spacing: -1.4px;
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
    font-size: 11px;
    font-weight: 800;
    white-space: nowrap;
}

/* ================= KPI ================= */

.kpi-card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 19px;
    min-height: 132px;
    box-shadow: 0 5px 18px rgba(15,23,42,.04);
    transition: all .2s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 9px 25px rgba(15,23,42,.08);
}

.kpi-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.kpi-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: .9px;
}

.kpi-icon {
    width: 31px;
    height: 31px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #EFF6FF;
    color: #2563EB;
    border-radius: 9px;
    font-weight: 800;
}

.kpi-value {
    color: #0F172A;
    font-size: 28px;
    font-weight: 850;
    letter-spacing: -.8px;
    margin-top: 13px;
}

.kpi-description {
    color: #94A3B8;
    font-size: 10px;
    margin-top: 4px;
}

/* ================= SECTION ================= */

.section-title {
    font-size: 19px;
    font-weight: 850;
    color: #0F172A;
    letter-spacing: -.35px;
    margin-top: 30px;
    margin-bottom: 13px;
}

.section-subtitle {
    color: #64748B;
    font-size: 12px;
    margin-top: -7px;
    margin-bottom: 16px;
}

/* ================= INSIGHT ================= */

.insight-card {
    background: linear-gradient(135deg,#EFF6FF 0%,#F8FAFC 100%);
    border: 1px solid #BFDBFE;
    border-radius: 15px;
    padding: 18px 20px;
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

/* ================= RISK CARDS ================= */

.risk-critical,
.risk-high,
.risk-medium,
.risk-low {
    border-radius: 14px;
    padding: 18px;
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

/* ================= PROFILE ================= */

.profile-card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 22px;
}

.profile-title {
    font-size: 21px;
    font-weight: 850;
    color: #0F172A;
}

.profile-label {
    font-size: 10px;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: .9px;
    font-weight: 800;
}

.profile-value {
    font-size: 15px;
    color: #374151;
    font-weight: 600;
}

/* ================= BUTTONS ================= */

.stButton > button {
    border-radius: 9px;
    font-weight: 700;
}

.stDownloadButton > button {
    border-radius: 9px;
    font-weight: 700;
}

/* ================= INPUTS ================= */

div[data-baseweb="select"] > div {
    border-radius: 9px;
}

input {
    border-radius: 9px !important;
}

/* ================= TABLE ================= */

[data-testid="stDataFrame"] {
    border: 1px solid #E2E8F0;
    border-radius: 12px;
}

/* ================= FOOTER ================= */

.footer {
    border-top: 1px solid #E2E8F0;
    margin-top: 40px;
    padding-top: 17px;
    text-align: center;
    color: #94A3B8;
    font-size: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    data = pd.read_csv("telco_churn_powerbi.csv")

    # Make sure CustomerSegment exists
    if "CustomerSegment" in data.columns:

        mapping = {
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
            .map(mapping)
            .fillna("Other")
        )

    else:

        data["Segment Name"] = "Other"

    return data


df = load_data()


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
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="brand">

        <div>
            <span class="brand-mark">◈</span>
            <span class="brand-name">CHURNIQ</span>
        </div>

        <div class="brand-sub">
            Customer Intelligence Platform
        </div>

    </div>
    """, unsafe_allow_html=True)


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
            st.session_state.pop(
                "risk_quick_filter",
                None
            )

            st.rerun()


    page = st.session_state.page


    # QUICK ACTIONS

    st.markdown(
        '<div class="nav-label" style="margin-top:20px;">Quick Actions</div>',
        unsafe_allow_html=True
    )


    if st.button(
        "⚠   High-Risk Customers",
        use_container_width=True
    ):

        st.session_state.page = "Customer Explorer"

        st.session_state.risk_quick_filter = True

        st.rerun()


    if st.button(
        "↻   Reset Workspace",
        use_container_width=True
    ):

        st.session_state.page = "Executive Overview"

        st.session_state.pop(
            "risk_quick_filter",
            None
        )

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
    <div style="height:30px"></div>

    <div style="
        color:#64748B;
        font-size:10px;
        line-height:1.8;
        letter-spacing:.5px;
    ">

        DATA SCIENCE PORTFOLIO<br>
        CUSTOMER RETENTION ANALYTICS

    </div>
    """, unsafe_allow_html=True)


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


    # KPI CARDS

    k1, k2, k3, k4, k5 = st.columns(5)


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


    # RETENTION OVERVIEW

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
            height=430,
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
            height=430,
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

        selected_contract = st.multiselect(
            "Contract",
            sorted(
                df["Contract"]
                .dropna()
                .unique()
            ),
            default=list(
                df["Contract"]
                .dropna()
                .unique()
            )
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


    # RISK MAP

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


    st.caption(
        "Higher position indicates greater predicted churn probability. "
        "Larger points represent higher monthly charges."
    )


# =========================================================
# PAGE 3 — CUSTOMER SEGMENTS
# =========================================================

elif page == "Customer Segments":


    # GUARANTEE SEGMENT COLUMN EXISTS

    if "CustomerSegment" in df.columns:

        mapping = {
            0: "New / Low-Engagement",
            1: "High-Value Loyal",
            2: "Long-Term Low-Spend",
            3: "High-Risk / At-Risk"
        }

        df["Segment Name"] = (
            pd.to_numeric(
                df["CustomerSegment"],
                errors="coerce"
            )
            .map(mapping)
            .fillna("Other")
        )

    else:

        df["Segment Name"] = "Other"


    # GROUPBY

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


    # CUSTOMER DISTRIBUTION

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


    # CHURN RATE

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


    # SEGMENT PROFILE

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
            "Higher Mean |SHAP Value| indicates greater overall influence "
            "on the model's churn predictions."
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


    except Exception:

        st.error(
            "SHAP feature importance data could not be loaded."
        )


# =========================================================
# PAGE 5 — CUSTOMER EXPLORER
# =========================================================

elif page == "Customer Explorer":


    if "risk_quick_filter" not in st.session_state:

        st.session_state.risk_quick_filter = False


    # QUICK FILTER

    if st.session_state.risk_quick_filter:

        explorer_df = df[
            df["ChurnProbability"] >= 0.35
        ].copy()

        st.info(
            f"Showing {len(explorer_df):,} customers above "
            "the 35% retention threshold."
        )


        if st.button("← Show All Customers"):

            st.session_state.risk_quick_filter = False

            st.rerun()

    else:

        explorer_df = df.copy()


    # CUSTOMER SELECTOR

    customer_ids = sorted(
        explorer_df["customerID"]
        .dropna()
        .unique()
    )


    if len(customer_ids) == 0:

        st.warning(
            "No customers match the current filter."
        )

        st.stop()


    customer_id = st.selectbox(
        "Select Customer",
        customer_ids
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


    # CUSTOMER RISK CARD

    st.markdown(
        f"""
        <div class="{risk_class}">

            <div class="profile-label">
                CUSTOMER RISK PROFILE
            </div>

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


    # PROFILE

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


    # RETENTION RECOMMENDATION

    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )


    st.success(
        customer["RetentionRecommendation"]
    )


    # PRIORITY CUSTOMERS

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


    available_columns = [
        col
        for col in columns
        if col in priority.columns
    ]


    st.dataframe(
        priority[available_columns].head(50),
        use_container_width=True,
        hide_index=True
    )


    # EXPORT BUTTON

    st.download_button(
        "↓  Export Priority Customers",
        data=priority[
            available_columns
        ].to_csv(index=False),
        file_name="priority_customer_list.csv",
        mime="text/csv"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        CHURNIQ • CUSTOMER CHURN INTELLIGENCE
        <br>
        XGBoost • K-Means • SHAP • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)