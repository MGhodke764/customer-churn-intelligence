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
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #F5F7FB;
    color: #172033;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hide Streamlit default elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stDecoration"] {
    display: none;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background: #0B1220;
}

section[data-testid="stSidebar"] * {
    color: #E5E7EB;
}

.brand-box {
    padding: 10px 5px 25px 5px;
}

.brand-title {
    font-size: 22px;
    font-weight: 800;
    color: white;
}

.brand-subtitle {
    font-size: 11px;
    color: #94A3B8;
    margin-top: 5px;
}

/* Sidebar buttons */

section[data-testid="stSidebar"] .stButton button {
    width: 100%;
    background: transparent;
    color: #CBD5E1;
    border: 1px solid transparent;
    border-radius: 10px;
    text-align: left;
    font-weight: 600;
    min-height: 42px;
}

section[data-testid="stSidebar"] .stButton button:hover {
    background: #1E293B;
    color: white;
    border-color: #334155;
}

/* ================= HEADER ================= */

.page-eyebrow {
    color: #2563EB;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.page-title {
    font-size: 36px;
    font-weight: 800;
    color: #0F172A;
    margin-top: 5px;
}

.page-subtitle {
    color: #64748B;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 25px;
}

/* ================= CARDS ================= */

.card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.04);
}

.card-title {
    font-size: 12px;
    font-weight: 800;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.card-value {
    font-size: 28px;
    font-weight: 800;
    color: #0F172A;
    margin-top: 8px;
}

.card-description {
    color: #94A3B8;
    font-size: 11px;
    margin-top: 5px;
}

/* ================= SECTION ================= */

.section-title {
    font-size: 21px;
    font-weight: 800;
    color: #0F172A;
    margin-top: 30px;
    margin-bottom: 12px;
}

.section-subtitle {
    color: #64748B;
    font-size: 13px;
    margin-bottom: 15px;
}

/* ================= INSIGHT ================= */

.insight-box {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 14px;
    padding: 20px;
}

.insight-heading {
    color: #1D4ED8;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 8px;
}

.insight-body {
    color: #1E3A8A;
    font-size: 13px;
    line-height: 1.7;
}

/* ================= RISK ================= */

.risk-critical {
    background: #FEF2F2;
    border: 1px solid #FECACA;
    color: #B91C1C;
}

.risk-high {
    background: #FFF7ED;
    border: 1px solid #FED7AA;
    color: #C2410C;
}

.risk-medium {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    color: #A16207;
}

.risk-low {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    color: #15803D;
}

.risk-box {
    border-radius: 14px;
    padding: 22px;
}

.risk-name {
    font-size: 25px;
    font-weight: 800;
    color: #0F172A;
}

.risk-label {
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ================= MODEL ================= */

.model-box {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
}

.model-text {
    color: #475569;
    font-size: 13px;
    line-height: 1.7;
}

/* ================= SIDEBAR MODEL ================= */

.sidebar-model {
    background: #111827;
    border: 1px solid #263449;
    border-radius: 12px;
    padding: 15px;
    margin-top: 20px;
}

.sidebar-model-title {
    color: #94A3B8;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.sidebar-model-name {
    color: white;
    font-size: 14px;
    font-weight: 700;
    margin-top: 8px;
}

.sidebar-row {
    display: flex;
    justify-content: space-between;
    margin-top: 9px;
    color: #94A3B8;
    font-size: 11px;
}

.sidebar-row strong {
    color: #E2E8F0;
}

/* ================= BUTTON ================= */

.stButton button {
    border-radius: 9px;
    font-weight: 700;
}

/* ================= FOOTER ================= */

.footer {
    margin-top: 45px;
    padding-top: 20px;
    border-top: 1px solid #E2E8F0;
    text-align: center;
    color: #94A3B8;
    font-size: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv("telco_churn_powerbi.csv")

    # Segment mapping
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


# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

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


# ============================================================
# COMMON CALCULATIONS
# ============================================================

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


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="brand-box">

        <div class="brand-title">
            ◆ CHURNIQ
        </div>

        <div class="brand-subtitle">
            Customer Intelligence Platform
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">WORKSPACE</div>',
        unsafe_allow_html=True
    )

    if "page" not in st.session_state:
        st.session_state.page = "Executive Overview"

    navigation = [
        ("Executive Overview", "▦"),
        ("Risk Analytics", "◉"),
        ("Customer Segments", "◌"),
        ("Churn Drivers", "✦"),
        ("Customer Explorer", "⌕")
    ]

    for name, icon in navigation:

        if st.button(
            f"{icon}   {name}",
            key="nav_" + name,
            use_container_width=True
        ):

            st.session_state.page = name
            st.session_state.risk_filter = False
            st.rerun()

    # QUICK ACTIONS

    st.markdown(
        '<div class="card-title" style="margin-top:25px;">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "⚠   High-Risk Customers",
        key="high_risk_action",
        use_container_width=True
    ):

        st.session_state.page = "Customer Explorer"
        st.session_state.risk_filter = True
        st.rerun()

    if st.button(
        "↻   Reset Workspace",
        key="reset_action",
        use_container_width=True
    ):

        st.session_state.page = "Executive Overview"
        st.session_state.risk_filter = False
        st.rerun()

    # MODEL STATUS

    st.markdown("""
    <div class="sidebar-model">

        <div class="sidebar-model-title">
            MODEL STATUS
        </div>

        <div class="sidebar-model-name">
            ● XGBoost Classifier
        </div>

        <div class="sidebar-row">
            <span>ROC-AUC</span>
            <strong>0.841</strong>
        </div>

        <div class="sidebar-row">
            <span>Threshold</span>
            <strong>35%</strong>
        </div>

        <div class="sidebar-row">
            <span>Explainability</span>
            <strong>SHAP</strong>
        </div>

    </div>
    """, unsafe_allow_html=True)


page = st.session_state.page


# ============================================================
# PAGE INFORMATION
# ============================================================

page_info = {

    "Executive Overview": (
        "CUSTOMER INTELLIGENCE",
        "Customer Churn Intelligence",
        "Retention command center for proactive customer management."
    ),

    "Risk Analytics": (
        "RISK MANAGEMENT",
        "Risk Analytics",
        "Explore predicted churn probability and priority populations."
    ),

    "Customer Segments": (
        "CUSTOMER STRATEGY",
        "Customer Segmentation",
        "Understand behavioral customer segments."
    ),

    "Churn Drivers": (
        "MODEL EXPLAINABILITY",
        "Churn Drivers",
        "Understand the strongest factors influencing churn."
    ),

    "Customer Explorer": (
        "CUSTOMER 360",
        "Customer Explorer",
        "Inspect individual customer risk and retention recommendations."
    )
}

eyebrow, title, subtitle = page_info[page]


# ============================================================
# HEADER
# ============================================================

st.markdown(
    f"""
    <div class="page-eyebrow">
        {eyebrow}
    </div>

    <div class="page-title">
        {title}
    </div>

    <div class="page-subtitle">
        {subtitle}
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    Total Customers
                </div>

                <div class="card-value">
                    {total_customers:,}
                </div>

                <div class="card-description">
                    Customer base
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k2:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    Churn Rate
                </div>

                <div class="card-value">
                    {churn_rate:.1%}
                </div>

                <div class="card-description">
                    Historical churn
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k3:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    At-Risk Customers
                </div>

                <div class="card-value">
                    {at_risk:,}
                </div>

                <div class="card-description">
                    Probability ≥ 35%
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k4:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    High / Critical
                </div>

                <div class="card-value">
                    {high_risk:,}
                </div>

                <div class="card-description">
                    Priority customers
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k5:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    Average Model Risk
                </div>

                <div class="card-value">
                    {avg_probability:.1%}
                </div>

                <div class="card-description">
                    Predicted probability
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # Charts

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        risk_data = (
            df["RiskLevel"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Medium", "Low"]
            )
            .fillna(0)
            .reset_index()
        )

        risk_data.columns = [
            "RiskLevel",
            "Customers"
        ]

        fig = px.bar(
            risk_data,
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
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        contract_data = (
            df.groupby("Contract")["ChurnFlag"]
            .mean()
            .mul(100)
            .reset_index()
        )

        contract_data.columns = [
            "Contract",
            "ChurnRate"
        ]

        fig = px.bar(
            contract_data,
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
            yaxis_title="Churn Rate (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # MODEL INTERPRETATION
    # IMPORTANT:
    # This uses st.info instead of raw HTML divs.
    # Therefore the HTML/code cannot appear on screen.

    st.markdown(
        '<div class="section-title">Model Interpretation</div>',
        unsafe_allow_html=True
    )

    st.info(
        "The strongest retention risk signals are associated with "
        "contract type, customer tenure, monthly charges, and payment "
        "method. These variables should receive priority when designing "
        "customer retention strategies."
    )


# ============================================================
# PAGE 2 — RISK ANALYTICS
# ============================================================

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
    ]

    m1, m2, m3 = st.columns(3)

    m1.metric(
        "Customers",
        f"{len(filtered):,}"
    )

    m2.metric(
        "Average Risk",
        f"{filtered['ChurnProbability'].mean():.1%}"
        if len(filtered)
        else "0%"
    )

    m3.metric(
        "Avg Monthly Charges",
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

    else:

        st.warning(
            "No customers match the selected filters."
        )


# ============================================================
# PAGE 3 — CUSTOMER SEGMENTS
# ============================================================

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

    c1, c2 = st.columns(2)

    with c1:

        fig = px.bar(
            segment_data,
            x="Segment Name",
            y="Customers",
            text="Customers",
            title="Customer Distribution by Segment"
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
            segment_data,
            x="Segment Name",
            y="ChurnRate",
            text="ChurnRate",
            title="Churn Rate by Segment"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%"
        )

        fig.update_layout(
            template="plotly_white",
            height=430,
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


# ============================================================
# PAGE 4 — CHURN DRIVERS
# ============================================================

elif page == "Churn Drivers":

    st.markdown(
        '<div class="section-title">What Drives Customer Churn?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Model explainability showing the strongest churn predictors.'
        '</div>',
        unsafe_allow_html=True
    )

    try:

        importance = pd.read_csv(
            "shap_feature_importance.csv"
        )

        if (
            "Feature" not in importance.columns
            or
            "MeanAbsSHAP" not in importance.columns
        ):

            st.error(
                "The SHAP file must contain Feature and MeanAbsSHAP columns."
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
                texttemplate="%{text:.3f}"
            )

            fig.update_layout(
                template="plotly_white",
                height=650
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.info(
                "Higher Mean |SHAP Value| indicates greater overall "
                "influence on the model's churn predictions."
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

        st.warning(
            "shap_feature_importance.csv was not found."
        )


# ============================================================
# PAGE 5 — CUSTOMER EXPLORER
# ============================================================

elif page == "Customer Explorer":

    if "risk_filter" not in st.session_state:
        st.session_state.risk_filter = False

    # ========================================================
    # CUSTOMER FILTER
    # ========================================================

    if st.session_state.risk_filter:

        explorer_df = df[
            df["ChurnProbability"] >= 0.35
        ].copy()

        st.warning(
            f"Showing {len(explorer_df):,} customers "
            "with churn probability ≥ 35%."
        )

        if st.button(
            "← Show All Customers",
            key="show_all_customers"
        ):

            st.session_state.risk_filter = False
            st.rerun()

    else:

        explorer_df = df.copy()

    # ========================================================
    # CUSTOMER ID DROPDOWN
    # ========================================================

    customer_ids = sorted(
        explorer_df["customerID"]
        .dropna()
        .astype(str)
        .unique()
    )

    if not customer_ids:

        st.warning(
            "No customers available."
        )

        st.stop()

    st.markdown(
        '<div class="section-title">Search Customer</div>',
        unsafe_allow_html=True
    )

    customer_id = st.selectbox(
        "Select Customer ID",
        customer_ids,
        index=0
    )

    customer = df[
        df["customerID"].astype(str) == customer_id
    ].iloc[0]

    probability = float(
        customer["ChurnProbability"]
    )

    # ========================================================
    # RISK CLASS
    # ========================================================

    if probability >= 0.70:

        risk_class = "risk-critical"
        risk_text = "Critical Risk"

    elif probability >= 0.50:

        risk_class = "risk-high"
        risk_text = "High Risk"

    elif probability >= 0.35:

        risk_class = "risk-medium"
        risk_text = "Medium Risk"

    else:

        risk_class = "risk-low"
        risk_text = "Low Risk"

    # ========================================================
    # CUSTOMER PROFILE
    # ========================================================

    st.markdown(
        '<div class="section-title">Customer Profile</div>',
        unsafe_allow_html=True
    )

    # IMPORTANT:
    # No HTML is used for the customer name/risk text.
    # This prevents the previous raw-code problem.

    profile_col1, profile_col2 = st.columns([3, 1])

    with profile_col1:

        st.markdown(
            f"### Customer {customer_id}"
        )

        st.caption(
            "Individual customer risk profile"
        )

    with profile_col2:

        st.markdown(
            f"""
            <div class="risk-box {risk_class}">
                <div class="risk-label">
                    Risk Status
                </div>
                <div style="
                    font-size:18px;
                    font-weight:800;
                    margin-top:5px;
                ">
                    {risk_text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ========================================================
    # CUSTOMER METRICS
    # ========================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Churn Probability",
        f"{probability:.1%}"
    )

    c2.metric(
        "Tenure",
        f"{customer['tenure']} months"
    )

    c3.metric(
        "Monthly Charges",
        f"${float(customer['MonthlyCharges']):.2f}"
    )

    c4.metric(
        "Contract",
        str(customer["Contract"])
    )

    # ========================================================
    # ADDITIONAL CUSTOMER INFO
    # ========================================================

    st.markdown(
        '<div class="section-title">Customer Details</div>',
        unsafe_allow_html=True
    )

    detail_columns = [
        "InternetService",
        "PaymentMethod",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "TechSupport",
        "OnlineSecurity"
    ]

    available_details = [
        col for col in detail_columns
        if col in df.columns
    ]

    if available_details:

        detail_data = {}

        for col in available_details:

            value = customer[col]

            if pd.isna(value):
                value = "N/A"

            detail_data[col] = str(value)

        detail_cols = st.columns(
            min(4, len(detail_data))
        )

        for i, (key, value) in enumerate(
            detail_data.items()
        ):

            with detail_cols[
                i % len(detail_cols)
            ]:

                st.metric(
                    key,
                    value
                )

    # ========================================================
    # RETENTION RECOMMENDATION
    # ========================================================

    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )

    if "RetentionRecommendation" in df.columns:

        recommendation = customer[
            "RetentionRecommendation"
        ]

        if pd.isna(recommendation):

            recommendation = (
                "Customers classified as High or Critical Risk "
                "should be prioritized for proactive retention "
                "campaigns, personalized offers and customer "
                "support follow-ups."
            )

    else:

        recommendation = (
            "Customers classified as High or Critical Risk "
            "should be prioritized for proactive retention "
            "campaigns, personalized offers and customer "
            "support follow-ups."
        )

    st.success(
        str(recommendation)
    )

    # ========================================================
    # PRIORITY CUSTOMER LIST
    # ========================================================

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
        "RiskLevel"
    ]

    if "RetentionRecommendation" in priority.columns:

        priority_columns.append(
            "RetentionRecommendation"
        )

    available_priority = [
        col for col in priority_columns
        if col in priority.columns
    ]

    st.dataframe(
        priority[
            available_priority
        ].head(50),
        use_container_width=True,
        hide_index=True
    )

    # ========================================================
    # DOWNLOAD
    # ========================================================

    st.download_button(
        "↓ Export Priority Customers",
        data=priority[
            available_priority
        ].to_csv(index=False),
        file_name="priority_customer_list.csv",
        mime="text/csv"
    )


# ============================================================
# MODEL INTERPRETATION
# ============================================================

if page in [
    "Churn Drivers",
    "Customer Explorer"
]:

    st.markdown(
        '<div class="section-title">Model Interpretation</div>',
        unsafe_allow_html=True
    )

    st.info(
        "The strongest retention risk signals are associated with "
        "contract type, customer tenure, monthly charges, and "
        "payment method. These variables should receive priority "
        "when designing customer retention strategies."
    )


# ============================================================
# FOOTER
# ============================================================

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
