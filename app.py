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
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #F6F8FC;
}

.block-container {
    max-width: 1500px;
    padding-top: 2.5rem !important;
    padding-bottom: 3rem !important;
}

#MainMenu,
footer,
[data-testid="stDecoration"] {
    visibility: hidden;
}


/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1220 0%, #111827 100%);
    border-right: 1px solid #1E293B;
}

section[data-testid="stSidebar"] > div {
    padding: 1rem 0.8rem;
}

section[data-testid="stSidebar"] * {
    color: #E5E7EB;
}


/* BRAND */

.brand-box {
    padding: 8px 8px 24px 8px;
}

.brand-row {
    display: flex;
    align-items: center;
}

.brand-mark {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white !important;
    font-size: 19px;
    font-weight: 900;
    margin-right: 10px;
}

.brand-name {
    color: white !important;
    font-size: 21px;
    font-weight: 850;
    letter-spacing: -0.5px;
}

.brand-sub {
    color: #94A3B8 !important;
    font-size: 10px;
    margin-top: 8px;
    margin-left: 2px;
}


/* NAVIGATION TITLE */

.nav-title {
    color: #64748B !important;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin: 12px 5px 8px 5px;
}


/* NAV BUTTONS */

section[data-testid="stSidebar"] .stButton {
    margin-bottom: 5px;
}

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: 11px;
    border: 1px solid transparent;
    background: transparent;
    color: #CBD5E1 !important;
    font-size: 13px;
    font-weight: 650;
    text-align: left;
    padding: 0.55rem 0.8rem;
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #1E293B;
    border-color: #334155;
    color: #FFFFFF !important;
    transform: translateX(2px);
}


/* QUICK ACTIONS */

.quick-card {
    margin-top: 18px;
    padding-top: 5px;
}


/* MODEL CARD */

.model-card {
    margin-top: 22px;
    padding: 16px;
    border-radius: 14px;
    border: 1px solid #263449;
    background: rgba(255,255,255,0.04);
}

.model-title {
    color: #94A3B8 !important;
    font-size: 9px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.2px;
}

.model-name {
    color: white !important;
    font-size: 14px;
    font-weight: 750;
    margin-top: 8px;
}

.model-row {
    display: flex;
    justify-content: space-between;
    margin-top: 11px;
    font-size: 11px;
    color: #94A3B8 !important;
}

.model-row b {
    color: #E2E8F0 !important;
}


/* ================= MAIN HEADER ================= */

.header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 22px;
    margin-bottom: 25px;
    border-bottom: 1px solid #E2E8F0;
}

.eyebrow {
    color: #2563EB;
    font-size: 10px;
    font-weight: 850;
    text-transform: uppercase;
    letter-spacing: 1.7px;
    margin-bottom: 8px;
}

.page-title {
    color: #0F172A;
    font-size: 34px;
    font-weight: 850;
    letter-spacing: -1.2px;
    line-height: 1.1;
}

.page-subtitle {
    color: #64748B;
    font-size: 13px;
    margin-top: 8px;
}

.online {
    background: #ECFDF5;
    color: #047857 !important;
    border: 1px solid #A7F3D0;
    border-radius: 50px;
    padding: 8px 13px;
    font-size: 10px;
    font-weight: 800;
}


/* ================= KPI ================= */

.kpi {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 18px;
    min-height: 125px;
    box-shadow: 0 4px 18px rgba(15,23,42,0.04);
}

.kpi-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: .8px;
}

.kpi-value {
    color: #0F172A;
    font-size: 27px;
    font-weight: 850;
    margin-top: 13px;
}

.kpi-desc {
    color: #94A3B8;
    font-size: 10px;
    margin-top: 4px;
}


/* ================= SECTIONS ================= */

.section-title {
    color: #0F172A;
    font-size: 19px;
    font-weight: 850;
    margin-top: 30px;
    margin-bottom: 8px;
}

.section-subtitle {
    color: #64748B;
    font-size: 12px;
    margin-bottom: 15px;
}


/* ================= INSIGHT ================= */

.insight {
    background: linear-gradient(135deg, #EFF6FF, #F8FAFC);
    border: 1px solid #BFDBFE;
    border-radius: 15px;
    padding: 18px 20px;
}

.insight-title {
    color: #1D4ED8;
    font-size: 11px;
    font-weight: 850;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.insight-text {
    color: #1E3A8A;
    font-size: 13px;
    line-height: 1.6;
    margin-top: 7px;
}


/* ================= RISK ================= */

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

.profile-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.profile-name {
    color: #0F172A;
    font-size: 25px;
    font-weight: 850;
    margin-top: 5px;
}

.profile-risk {
    font-size: 13px;
    font-weight: 800;
    margin-top: 8px;
}


/* ================= INPUTS ================= */

div[data-baseweb="select"] > div {
    border-radius: 10px;
    border-color: #CBD5E1;
}

.stSelectbox label,
.stMultiSelect label,
.stSlider label {
    font-weight: 700 !important;
    color: #334155 !important;
}


/* ================= BUTTONS ================= */

.stButton > button {
    border-radius: 10px;
    font-weight: 700;
}


/* ================= FOOTER ================= */

.footer {
    border-top: 1px solid #E2E8F0;
    margin-top: 40px;
    padding-top: 18px;
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

    df = pd.read_csv("telco_churn_powerbi.csv")

    if "CustomerSegment" in df.columns:

        segment_map = {
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
            .map(segment_map)
            .fillna("Other")
        )

    else:

        df["Segment Name"] = "Other"

    return df


df = load_data()


# =========================================================
# CALCULATIONS
# =========================================================

total_customers = df["customerID"].nunique()

churned = df.loc[
    df["ChurnFlag"] == 1,
    "customerID"
].nunique()

churn_rate = churned / total_customers if total_customers else 0

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
    <div class="brand-box">

        <div class="brand-row">

            <div class="brand-mark">◈</div>

            <div class="brand-name">
                CHURNIQ
            </div>

        </div>

        <div class="brand-sub">
            Customer Intelligence Platform
        </div>

    </div>
    """, unsafe_allow_html=True)


    st.markdown(
        '<div class="nav-title">Workspace</div>',
        unsafe_allow_html=True
    )


    navigation = [
        ("Executive Overview", "▦"),
        ("Risk Analytics", "◉"),
        ("Customer Segments", "◌"),
        ("Churn Drivers", "✦"),
        ("Customer Explorer", "⌕")
    ]


    if "page" not in st.session_state:
        st.session_state.page = "Executive Overview"


    for name, icon in navigation:

        if st.button(
            f"{icon}   {name}",
            key="nav_" + name,
            use_container_width=True
        ):

            st.session_state.page = name
            st.session_state.risk_filter = False
            st.rerun()


    st.markdown(
        '<div class="nav-title" style="margin-top:20px;">Quick Actions</div>',
        unsafe_allow_html=True
    )


    if st.button(
        "⚠   High-Risk Customers",
        key="quick_risk",
        use_container_width=True
    ):

        st.session_state.page = "Customer Explorer"
        st.session_state.risk_filter = True
        st.rerun()


    if st.button(
        "↻   Reset Workspace",
        key="reset",
        use_container_width=True
    ):

        st.session_state.page = "Executive Overview"
        st.session_state.risk_filter = False
        st.rerun()


    st.markdown("""
    <div class="model-card">

        <div class="model-title">
            Model Status
        </div>

        <div class="model-name">
            ● XGBoost Classifier
        </div>

        <div class="model-row">
            <span>ROC-AUC</span>
            <b>0.841</b>
        </div>

        <div class="model-row">
            <span>Threshold</span>
            <b>35%</b>
        </div>

        <div class="model-row">
            <span>Explainability</span>
            <b>SHAP</b>
        </div>

    </div>
    """, unsafe_allow_html=True)


page = st.session_state.page


# =========================================================
# HEADER
# =========================================================

page_info = {

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


eyebrow, title, subtitle = page_info[page]


st.markdown(
    f"""
    <div class="header">

        <div>

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

        <div class="online">
            ● MODEL ONLINE
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">TOTAL CUSTOMERS</div>
                <div class="kpi-value">{total_customers:,}</div>
                <div class="kpi-desc">Active customer base</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">CHURN RATE</div>
                <div class="kpi-value">{churn_rate:.1%}</div>
                <div class="kpi-desc">Historical churn</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">AT-RISK CUSTOMERS</div>
                <div class="kpi-value">{at_risk:,}</div>
                <div class="kpi-desc">Probability ≥ 35%</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">HIGH / CRITICAL</div>
                <div class="kpi-value">{high_risk:,}</div>
                <div class="kpi-desc">Priority customers</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with c5:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">AVG MODEL RISK</div>
                <div class="kpi-value">{avg_probability:.1%}</div>
                <div class="kpi-desc">Predicted probability</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Portfolio-level view of customer risk and contract behavior.</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)


    with col1:

        risk = (
            df["RiskLevel"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Medium", "Low"]
            )
            .fillna(0)
            .reset_index()
        )

        risk.columns = ["RiskLevel", "Customers"]


        fig = px.bar(
            risk,
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
            margin=dict(l=20, r=20, t=60, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:

        contract = (
            df.groupby("Contract")["ChurnFlag"]
            .mean()
            .mul(100)
            .reset_index()
        )

        contract.columns = [
            "Contract",
            "ChurnRate"
        ]


        fig = px.bar(
            contract,
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
            margin=dict(l=20, r=20, t=60, b=20),
            yaxis_title="Churn Rate (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    month_churn = df[
        df["Contract"] == "Month-to-month"
    ]["ChurnFlag"].mean()


    st.markdown(
        '<div class="section-title">Executive Insight</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="insight">

            <div class="insight-title">
                ✦ Retention Insight
            </div>

            <div class="insight-text">
                Month-to-month customers show a
                <b>{month_churn:.1%}</b> churn rate.
                The model currently identifies
                <b>{at_risk:,}</b> customers above the
                <b>35% intervention threshold</b>.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# RISK ANALYTICS
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

        minimum = st.slider(
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
        (df["ChurnProbability"] >= minimum)
    ]


    a, b, c = st.columns(3)

    a.metric(
        "Customers",
        f"{len(filtered):,}"
    )

    b.metric(
        "Average Risk",
        f"{filtered['ChurnProbability'].mean():.1%}"
        if len(filtered)
        else "0%"
    )

    c.metric(
        "Avg Monthly Charges",
        f"${filtered['MonthlyCharges'].mean():,.2f}"
        if len(filtered)
        else "$0"
    )


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
        title="Customer Risk Map"
    )

    fig.update_layout(
        template="plotly_white",
        height=520
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# CUSTOMER SEGMENTS
# =========================================================

elif page == "Customer Segments":

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
# CHURN DRIVERS
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
            "Higher Mean |SHAP Value| indicates greater overall influence on churn predictions."
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


    except Exception as e:

        st.error(
            "Could not load shap_feature_importance.csv"
        )


# =========================================================
# CUSTOMER EXPLORER
# =========================================================

elif page == "Customer Explorer":

    if "risk_filter" not in st.session_state:
        st.session_state.risk_filter = False


    if st.session_state.risk_filter:

        explorer_df = df[
            df["ChurnProbability"] >= 0.35
        ].copy()

        st.info(
            f"Showing {len(explorer_df):,} customers above the 35% retention threshold."
        )

        if st.button(
            "← Show All Customers",
            key="show_all"
        ):

            st.session_state.risk_filter = False
            st.rerun()

    else:

        explorer_df = df.copy()


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


    st.markdown(
        '<div class="section-title">Search Customer</div>',
        unsafe_allow_html=True
    )


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
        <div class="risk-card {risk_class}">

            <div class="profile-label">
                CUSTOMER PROFILE
            </div>

            <div class="profile-name">
                Customer {customer_id}
            </div>

            <div class="profile-risk">
                {customer["RiskLevel"]} Risk
                &nbsp; • &nbsp;
                {probability:.1%} predicted churn
            </div>

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
        str(customer["Contract"])
    )

    c4.metric(
        "Internet Service",
        str(customer["InternetService"])
    )


    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )


    recommendation = customer.get(
        "RetentionRecommendation",
        "Review customer engagement and offer a personalized retention plan."
    )


    st.success(
        str(recommendation)
    )


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


    available = [
        column
        for column in columns
        if column in priority.columns
    ]


    st.dataframe(
        priority[available].head(50),
        use_container_width=True,
        hide_index=True
    )


    st.download_button(
        "↓ Export Priority Customers",
        priority[available].to_csv(
            index=False
        ),
        "priority_customer_list.csv",
        "text/csv"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    CHURNIQ • CUSTOMER CHURN INTELLIGENCE
    <br>
    XGBoost • K-Means • SHAP • Streamlit

</div>
""", unsafe_allow_html=True)