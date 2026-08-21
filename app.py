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
    initial_sidebar_state="collapsed"
)

# ============================================================
# PROFESSIONAL UI CSS
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Inter, -apple-system, BlinkMacSystemFont,
    "Segoe UI", sans-serif;
}

.stApp {
    background: #F5F7FB;
}

/* Main container */
.block-container {
    max-width: 1450px;
    padding: 28px 45px 50px 45px !important;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stDecoration"] {
    display: none;
}

/* ============================================================
   HEADER
   ============================================================ */

.header-box {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 18px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
}

.header-title {
    font-size: 27px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 3px;
}

.header-subtitle {
    font-size: 13px;
    color: #6B7280;
}

/* ============================================================
   NAVIGATION
   ============================================================ */

div.stButton > button {
    width: 100%;
    min-height: 45px;
    border-radius: 11px;
    border: 1px solid #DDE3EC;
    background: #FFFFFF;
    color: #344054;
    font-weight: 700;
    font-size: 13px;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    border-color: #2563EB;
    color: #2563EB;
    background: #EFF6FF;
}

div.stButton > button:focus {
    border-color: #2563EB;
    color: #FFFFFF;
    background: #2563EB;
}

/* ============================================================
   PAGE TITLE
   ============================================================ */

.page-label {
    color: #2563EB;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-top: 25px;
    margin-bottom: 5px;
}

.page-title {
    color: #101828;
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 4px;
}

.page-description {
    color: #667085;
    font-size: 13px;
    margin-bottom: 25px;
}

/* ============================================================
   KPI CARDS
   ============================================================ */

.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E4E7EC;
    border-radius: 15px;
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
    margin-top: 9px;
}

/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: #101828;
    font-size: 19px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 14px;
}

/* ============================================================
   CUSTOMER PROFILE
   ============================================================ */

.profile-card {
    background: #FFFFFF;
    border: 1px solid #E4E7EC;
    border-radius: 16px;
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
    margin-top: 7px;
}

/* ============================================================
   RISK BADGES
   ============================================================ */

.risk-low {
    display: inline-block;
    margin-top: 10px;
    padding: 6px 12px;
    border-radius: 20px;
    background: #ECFDF3;
    color: #027A48;
    font-size: 12px;
    font-weight: 800;
}

.risk-medium {
    display: inline-block;
    margin-top: 10px;
    padding: 6px 12px;
    border-radius: 20px;
    background: #FFFAEB;
    color: #B54708;
    font-size: 12px;
    font-weight: 800;
}

.risk-high {
    display: inline-block;
    margin-top: 10px;
    padding: 6px 12px;
    border-radius: 20px;
    background: #FFF4ED;
    color: #C4320A;
    font-size: 12px;
    font-weight: 800;
}

.risk-critical {
    display: inline-block;
    margin-top: 10px;
    padding: 6px 12px;
    border-radius: 20px;
    background: #FEF3F2;
    color: #B42318;
    font-size: 12px;
    font-weight: 800;
}

/* ============================================================
   SELECT BOX
   ============================================================ */

div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: #D0D5DD !important;
    background: #FFFFFF !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: #2563EB !important;
}

/* ============================================================
   INFO BOX
   ============================================================ */

.info-box {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 12px;
    padding: 15px 18px;
    color: #1E40AF;
    font-size: 13px;
    margin-top: 15px;
}

/* ============================================================
   FOOTER
   ============================================================ */

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

    # -------------------------------
    # Customer ID
    # -------------------------------

    if "customerID" not in df.columns:

        possible = [
            c for c in df.columns
            if c.lower().replace("_", "").replace(" ", "")
            == "customerid"
        ]

        if possible:
            df["customerID"] = df[possible[0]]

        else:
            df["customerID"] = [
                f"CUST-{i:04d}"
                for i in range(1, len(df) + 1)
            ]

    # -------------------------------
    # Churn flag
    # -------------------------------

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

    # -------------------------------
    # Churn probability
    # -------------------------------

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

    # -------------------------------
    # Risk level
    # -------------------------------

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

    # -------------------------------
    # Segment
    # -------------------------------

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
# DATA
# ============================================================

try:

    df = load_data()

except Exception as e:

    st.error(
        "Dataset could not be loaded. "
        "Make sure telco_churn_powerbi.csv is in the GitHub repository."
    )

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="header-box">

        <div class="header-title">
            ◆ Customer Intelligence
        </div>

        <div class="header-subtitle">
            AI-Powered Customer Retention Analytics
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# NAVIGATION BUTTONS
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Overview"

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button(
        "▣  Overview",
        use_container_width=True
    ):
        st.session_state.page = "Overview"
        st.rerun()

with n2:
    if st.button(
        "◉  Risk Analytics",
        use_container_width=True
    ):
        st.session_state.page = "Risk"
        st.rerun()

with n3:
    if st.button(
        "○  Segments",
        use_container_width=True
    ):
        st.session_state.page = "Segments"
        st.rerun()

with n4:
    if st.button(
        "✦  Churn Drivers",
        use_container_width=True
    ):
        st.session_state.page = "Drivers"
        st.rerun()

with n5:
    if st.button(
        "⌕  Customer Explorer",
        use_container_width=True
    ):
        st.session_state.page = "Customers"
        st.rerun()


# ============================================================
# OVERVIEW
# ============================================================

if st.session_state.page == "Overview":

    st.markdown(
        '<div class="page-label">CUSTOMER INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Customer Churn Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Monitor customer health, identify churn risk, and prioritize retention opportunities.</div>',
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

        risk = (
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

        risk.columns = [
            "Risk Level",
            "Customers"
        ]

        fig = px.bar(
            risk,
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
            height=420
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
                height=420
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
        '<div class="page-description">Explore predicted churn probability across your customer base.</div>',
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

        x = (
            "tenure"
            if "tenure" in risk_df.columns
            else "ChurnProbability"
        )

        fig = px.scatter(
            risk_df,
            x=x,
            y="ChurnProbability",
            color="RiskLevel",
            hover_data=["customerID"],
            title="Customer Risk Map"
        )

        fig.update_layout(
            template="plotly_white",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
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
        '<div class="page-description">Compare customer groups and understand their churn behavior.</div>',
        unsafe_allow_html=True
    )

    summary = (
        df.groupby("Segment Name")
        .agg(
            Customers=("customerID", "count"),
            Churn_Rate=("ChurnFlag", "mean")
        )
        .reset_index()
    )

    summary["Churn_Rate"] *= 100

    a, b = st.columns(2)

    with a:

        fig = px.bar(
            summary,
            x="Segment Name",
            y="Customers",
            text="Customers",
            title="Customers by Segment"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with b:

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
            height=420
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
        '<div class="page-description">Understand the factors associated with customer churn.</div>',
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

            top = shap.nlargest(
                12,
                importance_col
            ).sort_values(
                importance_col
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
                "Feature importance columns could not be detected."
            )

    except FileNotFoundError:

        st.info(
            "Upload shap_feature_importance.csv to show model drivers."
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

    # Customer dropdown

    customer_ids = sorted(
        df["customerID"]
        .astype(str)
        .dropna()
        .unique()
        .tolist()
    )

    selected_id = st.selectbox(
        "Search Customer ID",
        customer_ids,
        index=0
    )

    customer = df[
        df["customerID"].astype(str)
        == selected_id
    ].iloc[0]

    probability = float(
        customer["ChurnProbability"]
    )

    # Risk

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

    # Profile

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

    # Metrics

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
            "Review contract, engagement, and service experience."
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
        &nbsp;•&nbsp;
        Machine Learning
        &nbsp;•&nbsp;
        Customer Segmentation
        &nbsp;•&nbsp;
        Explainable AI
    </div>
    """,
    unsafe_allow_html=True
)
