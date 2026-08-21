import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background: #F6F8FC;
}

.block-container {
    padding: 2rem 2.5rem 3rem 2.5rem !important;
    max-width: 1500px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1F2937;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

.sidebar-brand {
    color: white;
    font-size: 21px;
    font-weight: 800;
    margin-bottom: 3px;
}

.sidebar-subtitle {
    color: #94A3B8;
    font-size: 11px;
    margin-bottom: 28px;
}

.sidebar-section {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
    margin-top: 18px;
    margin-bottom: 8px;
}

/* Sidebar buttons */

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    background: transparent !important;
    color: #CBD5E1 !important;
    border: 1px solid transparent !important;
    border-radius: 9px !important;
    text-align: left !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    min-height: 42px !important;
    margin-bottom: 5px !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #1E293B !important;
    color: #FFFFFF !important;
    border-color: #334155 !important;
}

section[data-testid="stSidebar"] .stButton > button:focus {
    background: #2563EB !important;
    color: white !important;
    border-color: #2563EB !important;
}

/* ---------- HEADER ---------- */

.header-card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 16px;
    padding: 20px 24px;
    margin-bottom: 25px;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
}

.header-title {
    color: #111827;
    font-size: 27px;
    font-weight: 800;
}

.header-subtitle {
    color: #667085;
    font-size: 13px;
    margin-top: 4px;
}

/* ---------- PAGE TITLE ---------- */

.page-label {
    color: #2563EB;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 5px;
}

.page-title {
    color: #101828;
    font-size: 32px;
    font-weight: 800;
}

.page-description {
    color: #667085;
    font-size: 13px;
    margin-bottom: 25px;
}

/* ---------- KPI ---------- */

.kpi-card {
    background: white;
    border: 1px solid #E4E7EC;
    border-radius: 14px;
    padding: 20px;
    min-height: 105px;
    box-shadow: 0 3px 12px rgba(16, 24, 40, 0.035);
}

.kpi-label {
    color: #667085;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.kpi-value {
    color: #101828;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

/* ---------- SECTION ---------- */

.section-title {
    color: #101828;
    font-size: 19px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 14px;
}

/* ---------- PROFILE ---------- */

.profile-card {
    background: white;
    border: 1px solid #E4E7EC;
    border-radius: 15px;
    padding: 23px;
    margin-top: 18px;
    box-shadow: 0 3px 12px rgba(16, 24, 40, 0.035);
}

.profile-label {
    color: #667085;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.2px;
}

.profile-name {
    color: #101828;
    font-size: 27px;
    font-weight: 800;
    margin-top: 6px;
}

/* ---------- RISK BADGES ---------- */

.risk-low {
    display: inline-block;
    background: #ECFDF3;
    color: #027A48;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
    margin-top: 10px;
}

.risk-medium {
    display: inline-block;
    background: #FFFAEB;
    color: #B54708;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
    margin-top: 10px;
}

.risk-high {
    display: inline-block;
    background: #FFF4ED;
    color: #C4320A;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
    margin-top: 10px;
}

.risk-critical {
    display: inline-block;
    background: #FEF3F2;
    color: #B42318;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
    margin-top: 10px;
}

/* ---------- SELECTBOX ---------- */

div[data-baseweb="select"] > div {
    border-radius: 9px !important;
    border-color: #D0D5DD !important;
    background: white !important;
}

/* ---------- FOOTER ---------- */

.footer {
    margin-top: 45px;
    padding-top: 18px;
    border-top: 1px solid #E4E7EC;
    text-align: center;
    color: #98A2B3;
    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    df = pd.read_csv("telco_churn_powerbi.csv")

    df.columns = df.columns.str.strip()

    # Customer ID
    if "customerID" not in df.columns:

        possible_id = [
            c for c in df.columns
            if c.lower().replace("_", "").replace(" ", "")
            == "customerid"
        ]

        if possible_id:
            df["customerID"] = df[possible_id[0]]

        else:
            df["customerID"] = [
                f"CUST-{i:04d}"
                for i in range(1, len(df) + 1)
            ]

    # Churn flag
    if "ChurnFlag" not in df.columns:

        if "Churn" in df.columns:

            df["ChurnFlag"] = (
                df["Churn"]
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
            df["ChurnFlag"] = 0

    # Churn probability
    if "ChurnProbability" not in df.columns:

        if "ChurnProbabilityPct" in df.columns:

            df["ChurnProbability"] = (
                pd.to_numeric(
                    df["ChurnProbabilityPct"],
                    errors="coerce"
                ) / 100
            )

        else:

            df["ChurnProbability"] = (
                df["ChurnFlag"].astype(float)
            )

    df["ChurnProbability"] = (
        pd.to_numeric(
            df["ChurnProbability"],
            errors="coerce"
        )
        .fillna(0)
        .clip(0, 1)
    )

    # Risk level
    df["RiskLevel"] = np.select(
        [
            df["ChurnProbability"] >= 0.70,
            df["ChurnProbability"] >= 0.50,
            df["ChurnProbability"] >= 0.35
        ],
        [
            "Critical",
            "High",
            "Medium"
        ],
        default="Low"
    )

    # Segment
    if "Segment Name" not in df.columns:

        if "CustomerSegment" in df.columns:

            segment = pd.to_numeric(
                df["CustomerSegment"],
                errors="coerce"
            )

            df["Segment Name"] = segment.map({
                0: "New / Low Engagement",
                1: "High Value Loyal",
                2: "Long Term Low Spend",
                3: "High Risk / At Risk"
            }).fillna("Other")

        else:

            df["Segment Name"] = pd.cut(
                df["ChurnProbability"],
                bins=[
                    -0.01,
                    0.25,
                    0.50,
                    0.70,
                    1.01
                ],
                labels=[
                    "Low Risk",
                    "Medium Risk",
                    "High Risk",
                    "Critical Risk"
                ]
            ).astype(str)

    return df


# ============================================================
# LOAD
# ============================================================

try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "telco_churn_powerbi.csv was not found. "
        "Make sure it is uploaded to the same GitHub repository."
    )

    st.stop()

except Exception as e:

    st.error(f"Error loading dataset: {e}")

    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Overview"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">
            ◆ Customer Intelligence
        </div>

        <div class="sidebar-subtitle">
            AI-Powered Customer Retention
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">DASHBOARD</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "▣   Overview",
        use_container_width=True
    ):
        st.session_state.page = "Overview"
        st.rerun()

    if st.button(
        "◉   Risk Analytics",
        use_container_width=True
    ):
        st.session_state.page = "Risk"
        st.rerun()

    if st.button(
        "○   Customer Segmentation",
        use_container_width=True
    ):
        st.session_state.page = "Segments"
        st.rerun()

    if st.button(
        "✦   Churn Drivers",
        use_container_width=True
    ):
        st.session_state.page = "Drivers"
        st.rerun()

    st.markdown(
        '<div class="sidebar-section">CUSTOMER</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "⌕   Customer Explorer",
        use_container_width=True
    ):
        st.session_state.page = "Customers"
        st.rerun()

    st.markdown("---")

    st.caption(
        f"Customers: {len(df):,}"
    )

    st.caption(
        "Machine Learning • Analytics"
    )


# ============================================================
# TOP HEADER
# ============================================================

st.markdown(
    """
    <div class="header-card">

        <div class="header-title">
            Customer Churn Intelligence
        </div>

        <div class="header-subtitle">
            AI-powered analytics for customer retention,
            segmentation and churn risk management
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# OVERVIEW
# ============================================================

if st.session_state.page == "Overview":

    st.markdown(
        '<div class="page-label">EXECUTIVE OVERVIEW</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Customer Health Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">A high-level view of customer churn, risk and retention opportunities.</div>',
        unsafe_allow_html=True
    )

    total = len(df)

    churned = int(
        df["ChurnFlag"].sum()
    )

    churn_rate = (
        churned / total
        if total > 0
        else 0
    )

    at_risk = int(
        (df["ChurnProbability"] >= 0.35).sum()
    )

    critical = int(
        (df["ChurnProbability"] >= 0.70).sum()
    )

    avg_risk = df[
        "ChurnProbability"
    ].mean()

    k1, k2, k3, k4, k5 = st.columns(5)

    cards = [
        ("TOTAL CUSTOMERS", f"{total:,}"),
        ("CHURN RATE", f"{churn_rate:.1%}"),
        ("AT-RISK CUSTOMERS", f"{at_risk:,}"),
        ("CRITICAL RISK", f"{critical:,}"),
        ("AVERAGE RISK", f"{avg_risk:.1%}")
    ]

    for col, (label, value) in zip(
        [k1, k2, k3, k4, k5],
        cards
    ):

        with col:

            st.markdown(
                f"""
                <div class="kpi-card">

                    <div class="kpi-label">
                        {label}
                    </div>

                    <div class="kpi-value">
                        {value}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">Risk Overview</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:

        risk_data = (
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

        risk_data.columns = [
            "Risk Level",
            "Customers"
        ]

        fig = px.bar(
            risk_data,
            x="Risk Level",
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
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        if "Contract" in df.columns:

            contract = (
                df.groupby("Contract")[
                    "ChurnFlag"
                ]
                .mean()
                .reset_index()
            )

            contract["Churn Rate"] = (
                contract["ChurnFlag"] * 100
            )

            fig = px.bar(
                contract,
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
                height=420,
                margin=dict(
                    l=20,
                    r=20,
                    t=60,
                    b=20
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# ============================================================
# RISK ANALYTICS
# ============================================================

elif st.session_state.page == "Risk":

    st.markdown(
        '<div class="page-label">RISK MANAGEMENT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Identify customers requiring immediate or proactive retention action.</div>',
        unsafe_allow_html=True
    )

    minimum = st.slider(
        "Minimum Churn Probability",
        0.0,
        1.0,
        0.35,
        0.05
    )

    risk_df = df[
        df["ChurnProbability"] >= minimum
    ].copy()

    st.metric(
        "Customers Matching Filter",
        f"{len(risk_df):,}"
    )

    if len(risk_df) > 0:

        x_axis = (
            "tenure"
            if "tenure" in risk_df.columns
            else "ChurnProbability"
        )

        fig = px.scatter(
            risk_df,
            x=x_axis,
            y="ChurnProbability",
            color="RiskLevel",
            hover_data=[
                "customerID"
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

        columns = [
            c for c in [
                "customerID",
                "ChurnProbability",
                "RiskLevel",
                "tenure",
                "MonthlyCharges",
                "Contract"
            ]
            if c in risk_df.columns
        ]

        st.dataframe(
            risk_df[
                columns
            ]
            .sort_values(
                "ChurnProbability",
                ascending=False
            ),
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No customers match the selected risk threshold."
        )


# ============================================================
# SEGMENTS
# ============================================================

elif st.session_state.page == "Segments":

    st.markdown(
        '<div class="page-label">CUSTOMER STRATEGY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Understand customer groups and compare their churn behavior.</div>',
        unsafe_allow_html=True
    )

    # Safety fix for previous KeyError
    if "Segment Name" not in df.columns:
        df["Segment Name"] = "Other"

    df["Segment Name"] = (
        df["Segment Name"]
        .fillna("Other")
        .astype(str)
    )

    summary = (
        df.groupby("Segment Name")
        .agg(
            Customers=(
                "customerID",
                "count"
            ),
            Churn_Rate=(
                "ChurnFlag",
                "mean"
            )
        )
        .reset_index()
    )

    summary["Churn_Rate"] *= 100

    left, right = st.columns(2)

    with left:

        fig = px.bar(
            summary,
            x="Segment Name",
            y="Customers",
            text="Customers",
            title="Customers by Segment"
        )

        fig.update_traces(
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

    with right:

        fig = px.bar(
            summary,
            x="Segment Name",
            y="Churn_Rate",
            text="Churn_Rate",
            title="Churn Rate by Segment"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
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

    st.dataframe(
        summary.round(2),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CHURN DRIVERS
# ============================================================

elif st.session_state.page == "Drivers":

    st.markdown(
        '<div class="page-label">EXPLAINABLE AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Churn Drivers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Understand which factors contribute most strongly to customer churn.</div>',
        unsafe_allow_html=True
    )

    try:

        shap = pd.read_csv(
            "shap_feature_importance.csv"
        )

        shap.columns = shap.columns.str.strip()

        feature_col = next(
            (
                c for c in [
                    "Feature",
                    "feature",
                    "Feature Name",
                    "feature_name"
                ]
                if c in shap.columns
            ),
            None
        )

        importance_col = next(
            (
                c for c in [
                    "MeanAbsSHAP",
                    "mean_abs_shap",
                    "Importance",
                    "importance"
                ]
                if c in shap.columns
            ),
            None
        )

        if feature_col and importance_col:

            shap[importance_col] = pd.to_numeric(
                shap[importance_col],
                errors="coerce"
            )

            shap = shap.dropna(
                subset=[
                    feature_col,
                    importance_col
                ]
            )

            top = (
                shap.nlargest(
                    12,
                    importance_col
                )
                .sort_values(
                    importance_col
                )
            )

            fig = px.bar(
                top,
                x=importance_col,
                y=feature_col,
                orientation="h",
                title="Top Churn Drivers"
            )

            fig.update_layout(
                template="plotly_white",
                height=550
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.warning(
                "Feature importance columns were not detected."
            )

    except FileNotFoundError:

        st.info(
            "Upload shap_feature_importance.csv "
            "to display your model's churn drivers."
        )


# ============================================================
# CUSTOMER EXPLORER
# ============================================================

elif st.session_state.page == "Customers":

    st.markdown(
        '<div class="page-label">RETENTION OPERATIONS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Select a customer to inspect their individual churn profile.</div>',
        unsafe_allow_html=True
    )

    # Customer ID dropdown

    customer_ids = sorted(
        df["customerID"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_id = st.selectbox(
        "Search Customer ID",
        customer_ids
    )

    customer = df[
        df["customerID"].astype(str)
        == selected_id
    ].iloc[0]

    probability = float(
        customer["ChurnProbability"]
    )

    # Risk badge

    if probability >= 0.70:

        risk_text = "Critical Risk"
        risk_class = "risk-critical"

    elif probability >= 0.50:

        risk_text = "High Risk"
        risk_class = "risk-high"

    elif probability >= 0.35:

        risk_text = "Medium Risk"
        risk_class = "risk-medium"

    else:

        risk_text = "Low Risk"
        risk_class = "risk-low"

    st.markdown(
        f"""
        <div class="profile-card">

            <div class="profile-label">
                CUSTOMER PROFILE
            </div>

            <div class="profile-name">
                Customer {selected_id}
            </div>

            <div class="{risk_class}">
                {risk_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # Customer metrics

    st.markdown(
        '<div class="section-title">Customer Metrics</div>',
        unsafe_allow_html=True
    )

    a, b, c, d = st.columns(4)

    tenure = customer.get(
        "tenure",
        0
    )

    monthly = customer.get(
        "MonthlyCharges",
        0
    )

    total_charges = customer.get(
        "TotalCharges",
        0
    )

    try:
        monthly = float(monthly)
    except:
        monthly = 0

    try:
        total_charges = float(total_charges)
    except:
        total_charges = 0

    with a:

        st.metric(
            "Tenure",
            f"{tenure} months"
        )

    with b:

        st.metric(
            "Monthly Charges",
            f"${monthly:,.2f}"
        )

    with c:

        st.metric(
            "Total Charges",
            f"${total_charges:,.2f}"
        )

    with d:

        st.metric(
            "Churn Probability",
            f"{probability:.1%}"
        )

    # Details

    st.markdown(
        '<div class="section-title">Customer Details</div>',
        unsafe_allow_html=True
    )

    details = {}

    for column in [
        "Contract",
        "InternetService",
        "PaymentMethod",
        "Churn",
        "Segment Name"
    ]:

        if column in df.columns:
            details[column] = customer[column]

    if details:

        details_df = pd.DataFrame(
            {
                "Attribute": list(details.keys()),
                "Value": list(details.values())
            }
        )

        st.dataframe(
            details_df,
            use_container_width=True,
            hide_index=True
        )

    # Recommendation

    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )

    if probability >= 0.70:

        recommendation = (
            "Immediate retention outreach recommended. "
            "Consider a personalized offer and direct customer contact."
        )

    elif probability >= 0.50:

        recommendation = (
            "Proactive retention campaign recommended. "
            "Review contract, engagement and service experience."
        )

    elif probability >= 0.35:

        recommendation = (
            "Monitor this customer closely and consider targeted engagement."
        )

    else:

        recommendation = (
            "Customer currently shows relatively low churn risk. "
            "Continue normal engagement."
        )

    st.info(
        recommendation
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Customer Churn Intelligence
        • Machine Learning
        • Customer Segmentation
        • Explainable AI
    </div>
    """,
    unsafe_allow_html=True
)
