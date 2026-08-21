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
# CSS
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.stApp {
    background: #F7F9FC;
}

.block-container {
    max-width: 1450px;
    padding-top: 28px;
    padding-left: 45px;
    padding-right: 45px;
    padding-bottom: 50px;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Remove sidebar */
section[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none;
}

/* Brand */

.brand {
    display: flex;
    align-items: center;
    gap: 13px;
    margin-bottom: 20px;
}

.brand-icon {
    width: 44px;
    height: 44px;
    background: #2563EB;
    color: white;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: bold;
}

.brand-title {
    font-size: 25px;
    font-weight: 800;
    color: #0F172A;
}

.brand-subtitle {
    color: #64748B;
    font-size: 12px;
    margin-top: 2px;
}

/* Navigation */

.nav-box {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 7px;
    margin-bottom: 12px;
}

/* Buttons */

.stButton > button {
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 42px !important;
    border: 1px solid #E2E8F0 !important;
    background: white !important;
    color: #334155 !important;
}

.stButton > button:hover {
    border-color: #2563EB !important;
    color: #2563EB !important;
    background: #EFF6FF !important;
}

/* Quick actions */

.quick-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 14px;
    margin-bottom: 7px;
}

/* Page heading */

.page-eyebrow {
    color: #2563EB;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 6px;
    text-transform: uppercase;
}

.page-title {
    color: #0F172A;
    font-size: 34px;
    font-weight: 800;
    letter-spacing: -1px;
}

.page-subtitle {
    color: #64748B;
    font-size: 13px;
    margin-top: 6px;
    margin-bottom: 20px;
}

/* KPI */

.kpi {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 19px;
    min-height: 120px;
}

.kpi-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.kpi-value {
    color: #0F172A;
    font-size: 29px;
    font-weight: 800;
    margin-top: 12px;
}

.kpi-small {
    color: #94A3B8;
    font-size: 10px;
    margin-top: 4px;
}

/* Sections */

.section-title {
    color: #0F172A;
    font-size: 20px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748B;
    font-size: 12px;
    margin-bottom: 15px;
}

/* Insight */

.insight {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 14px;
    padding: 18px;
    margin-top: 12px;
}

.insight-title {
    color: #1D4ED8;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.insight-text {
    color: #1E3A8A;
    font-size: 13px;
    line-height: 1.6;
    margin-top: 7px;
}

/* Profile */

.profile {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 22px;
    margin-top: 18px;
}

.profile-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.profile-name {
    color: #0F172A;
    font-size: 28px;
    font-weight: 800;
    margin-top: 5px;
}

/* Risk */

.risk-box {
    border-radius: 14px;
    padding: 20px;
    margin-top: 15px;
}

.risk-critical {
    background: #FEF2F2;
    border: 1px solid #FECACA;
}

.risk-high {
    background: #FFF7ED;
    border: 1px solid #FED7AA;
}

.risk-medium {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
}

.risk-low {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
}

.risk-label {
    color: #64748B;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.risk-value {
    color: #0F172A;
    font-size: 30px;
    font-weight: 800;
    margin-top: 5px;
}

/* Footer */

.footer {
    border-top: 1px solid #E2E8F0;
    margin-top: 40px;
    padding-top: 15px;
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

    df = pd.read_csv("telco_churn_powerbi.csv")

    df.columns = df.columns.str.strip()

    # --------------------------------------------------------
    # Customer ID
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Churn Flag
    # --------------------------------------------------------

    if "ChurnFlag" not in df.columns:

        if "Churn" in df.columns:

            df["ChurnFlag"] = (
                df["Churn"]
                .astype(str)
                .str.lower()
                .str.strip()
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

    # --------------------------------------------------------
    # Numeric columns
    # --------------------------------------------------------

    numeric_columns = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "ChurnProbability",
        "ChurnProbabilityPct",
        "CustomerSegment"
    ]

    for col in numeric_columns:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # --------------------------------------------------------
    # Churn probability
    # --------------------------------------------------------

    if "ChurnProbability" not in df.columns:

        if "ChurnProbabilityPct" in df.columns:

            df["ChurnProbability"] = (
                df["ChurnProbabilityPct"] / 100
            )

        else:

            # Use churn history as fallback
            df["ChurnProbability"] = (
                df["ChurnFlag"].astype(float)
            )

    df["ChurnProbability"] = (
        df["ChurnProbability"]
        .fillna(0)
        .clip(0, 1)
    )

    df["ChurnProbabilityPct"] = (
        df["ChurnProbability"] * 100
    )

    # --------------------------------------------------------
    # Risk Level
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Segment
    # --------------------------------------------------------

    if "CustomerSegment" in df.columns:

        segment_values = pd.to_numeric(
            df["CustomerSegment"],
            errors="coerce"
        )

        segment_map = {
            0: "New / Low-Engagement",
            1: "High-Value Loyal",
            2: "Long-Term Low-Spend",
            3: "High-Risk / At-Risk"
        }

        df["Segment Name"] = (
            segment_values
            .map(segment_map)
            .fillna("Other")
        )

    else:

        # Create segments automatically if
        # CustomerSegment doesn't exist

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

    # --------------------------------------------------------
    # Retention recommendation
    # --------------------------------------------------------

    df["RetentionRecommendation"] = np.select(
        [
            df["RiskLevel"] == "Critical",
            df["RiskLevel"] == "High",
            df["RiskLevel"] == "Medium"
        ],
        [
            "Immediate retention outreach and personalized offer.",
            "Proactive retention campaign recommended.",
            "Monitor engagement and provide targeted incentives."
        ],
        default="Maintain relationship and monitor behavior."
    )

    return df


# ============================================================
# LOAD DATA SAFELY
# ============================================================

try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "telco_churn_powerbi.csv was not found. "
        "Upload the CSV file to the same GitHub repository "
        "as app.py."
    )

    st.stop()

except Exception as error:

    st.error(
        "There was a problem loading the dataset."
    )

    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:

    st.session_state.page = "Executive Overview"


if "risk_filter" not in st.session_state:

    st.session_state.risk_filter = False


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

    <div class="brand-icon">
        ◆
    </div>

    <div>

        <div class="brand-title">
            Customer Intelligence
        </div>

        <div class="brand-subtitle">
            AI-Powered Retention Analytics
        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# TOP NAVIGATION
# ============================================================

st.markdown(
    '<div class="nav-box">',
    unsafe_allow_html=True
)

n1, n2, n3, n4, n5 = st.columns(5)


with n1:

    if st.button(
        "▣  Executive Overview",
        use_container_width=True,
        key="executive_nav"
    ):

        st.session_state.page = "Executive Overview"
        st.session_state.risk_filter = False
        st.rerun()


with n2:

    if st.button(
        "◉  Risk Analytics",
        use_container_width=True,
        key="risk_nav"
    ):

        st.session_state.page = "Risk Analytics"
        st.session_state.risk_filter = False
        st.rerun()


with n3:

    if st.button(
        "○  Customer Segments",
        use_container_width=True,
        key="segment_nav"
    ):

        st.session_state.page = "Customer Segments"
        st.session_state.risk_filter = False
        st.rerun()


with n4:

    if st.button(
        "✦  Churn Drivers",
        use_container_width=True,
        key="drivers_nav"
    ):

        st.session_state.page = "Churn Drivers"
        st.session_state.risk_filter = False
        st.rerun()


with n5:

    if st.button(
        "⌕  Customer Explorer",
        use_container_width=True,
        key="explorer_nav"
    ):

        st.session_state.page = "Customer Explorer"
        st.session_state.risk_filter = False
        st.rerun()


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ============================================================
# QUICK ACTIONS
# ============================================================

st.markdown(
    '<div class="quick-label">Quick Actions</div>',
    unsafe_allow_html=True
)

q1, q2, q3 = st.columns([1.7, 1.4, 6])

with q1:

    if st.button(
        "⚠  High-Risk Customers",
        use_container_width=True,
        key="high_risk_button"
    ):

        st.session_state.page = "Customer Explorer"
        st.session_state.risk_filter = True
        st.rerun()


with q2:

    if st.button(
        "↻  Reset",
        use_container_width=True,
        key="reset_button"
    ):

        st.session_state.page = "Executive Overview"
        st.session_state.risk_filter = False
        st.rerun()


st.divider()


# ============================================================
# COMMON METRICS
# ============================================================

total_customers = len(df)

churned = int(
    df["ChurnFlag"].sum()
)

churn_rate = (
    churned / total_customers
    if total_customers > 0
    else 0
)

at_risk = int(
    (
        df["ChurnProbability"] >= 0.35
    ).sum()
)

high_risk = int(
    (
        df["ChurnProbability"] >= 0.50
    ).sum()
)

average_risk = (
    df["ChurnProbability"].mean()
)


# ============================================================
# PAGE HEADER FUNCTION
# ============================================================

def page_header(
    eyebrow,
    title,
    subtitle
):

    st.markdown(
        f"""
        <div>

            <div class="page-eyebrow">
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


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

if st.session_state.page == "Executive Overview":

    page_header(
        "CUSTOMER INTELLIGENCE",
        "Customer Churn Intelligence",
        "Retention command center for proactive customer management."
    )

    # --------------------------------------------------------
    # KPI ROW
    # --------------------------------------------------------

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:

        st.markdown(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    TOTAL CUSTOMERS
                </div>

                <div class="kpi-value">
                    {total_customers:,}
                </div>

                <div class="kpi-small">
                    Customer base
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k2:

        st.markdown(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    CHURN RATE
                </div>

                <div class="kpi-value">
                    {churn_rate:.1%}
                </div>

                <div class="kpi-small">
                    Historical churn
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k3:

        st.markdown(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    AT-RISK
                </div>

                <div class="kpi-value">
                    {at_risk:,}
                </div>

                <div class="kpi-small">
                    Risk ≥ 35%
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k4:

        st.markdown(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    HIGH RISK
                </div>

                <div class="kpi-value">
                    {high_risk:,}
                </div>

                <div class="kpi-small">
                    Risk ≥ 50%
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with k5:

        st.markdown(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    AVG MODEL RISK
                </div>

                <div class="kpi-value">
                    {average_risk:.1%}
                </div>

                <div class="kpi-small">
                    Predicted probability
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # CHARTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Understand where churn risk is concentrated across the customer base.</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        risk_df = (
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

        risk_df.columns = [
            "Risk Level",
            "Customers"
        ]

        fig = px.bar(
            risk_df,
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
            height=400,
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

    with c2:

        if "Contract" in df.columns:

            contract_df = (
                df.groupby("Contract")[
                    "ChurnFlag"
                ]
                .mean()
                .reset_index()
            )

            contract_df["Churn Rate"] = (
                contract_df["ChurnFlag"] * 100
            )

            fig = px.bar(
                contract_df,
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
                height=400,
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

        else:

            st.info(
                "Contract information is not available."
            )

    # --------------------------------------------------------
    # INSIGHT
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="insight">

            <div class="insight-title">
                ✦ Executive Insight
            </div>

            <div class="insight-text">

                The model currently identifies
                <b>{at_risk:,}</b> customers above the
                35% churn-risk threshold.

                These customers represent the primary
                population for proactive retention campaigns.

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RISK ANALYTICS
# ============================================================

elif st.session_state.page == "Risk Analytics":

    page_header(
        "RISK MANAGEMENT",
        "Risk Analytics",
        "Explore predicted churn probability and priority populations."
    )

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

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

        if "Contract" in df.columns:

            contract_values = sorted(
                df["Contract"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        else:

            contract_values = []

        selected_contract = st.multiselect(
            "Contract",
            contract_values,
            default=contract_values
        )

    with f3:

        probability_limit = st.slider(
            "Minimum Churn Probability",
            0.0,
            1.0,
            0.35,
            0.05
        )

    filtered = df[
        df["RiskLevel"].isin(
            selected_risk
        )
        &
        (
            df["ChurnProbability"]
            >= probability_limit
        )
    ].copy()

    if contract_values:

        filtered = filtered[
            filtered["Contract"]
            .astype(str)
            .isin(selected_contract)
        ]

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric(
            "Matching Customers",
            f"{len(filtered):,}"
        )

    with r2:

        risk_average = (
            filtered["ChurnProbability"].mean()
            if len(filtered)
            else 0
        )

        st.metric(
            "Average Risk",
            f"{risk_average:.1%}"
        )

    with r3:

        if (
            "MonthlyCharges" in filtered.columns
            and len(filtered)
        ):

            charge_average = (
                filtered["MonthlyCharges"]
                .mean()
            )

        else:

            charge_average = 0

        st.metric(
            "Average Monthly Charges",
            f"${charge_average:,.2f}"
        )

    # --------------------------------------------------------
    # RISK SCATTER
    # --------------------------------------------------------

    if len(filtered) > 0:

        fig = px.scatter(
            filtered,
            x="tenure",
            y="ChurnProbability",
            color="RiskLevel",
            size="MonthlyCharges"
            if "MonthlyCharges" in filtered.columns
            else None,
            hover_data=[
                "customerID"
            ],
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

    else:

        st.warning(
            "No customers match the selected filters."
        )


# ============================================================
# CUSTOMER SEGMENTS
# ============================================================

elif st.session_state.page == "Customer Segments":

    page_header(
        "CUSTOMER STRATEGY",
        "Customer Segmentation",
        "Understand customer groups based on behavioral and financial characteristics."
    )

    # --------------------------------------------------------
    # SAFE SEGMENT CREATION
    # --------------------------------------------------------

    segment_df = df.copy()

    if "Segment Name" not in segment_df.columns:

        segment_df["Segment Name"] = "Other"

    segment_df["Segment Name"] = (
        segment_df["Segment Name"]
        .fillna("Other")
        .astype(str)
    )

    # --------------------------------------------------------
    # GROUPBY
    # --------------------------------------------------------

    aggregation = {
        "customerID": "count",
        "ChurnFlag": "mean"
    }

    if "tenure" in segment_df.columns:
        aggregation["tenure"] = "mean"

    if "MonthlyCharges" in segment_df.columns:
        aggregation["MonthlyCharges"] = "mean"

    segment_summary = (
        segment_df
        .groupby(
            "Segment Name",
            dropna=False
        )
        .agg(aggregation)
        .reset_index()
    )

    segment_summary = segment_summary.rename(
        columns={
            "customerID": "Customers",
            "ChurnFlag": "Churn Rate",
            "tenure": "Average Tenure",
            "MonthlyCharges": "Average Monthly Charges"
        }
    )

    segment_summary["Churn Rate"] = (
        segment_summary["Churn Rate"] * 100
    )

    # --------------------------------------------------------
    # CHARTS
    # --------------------------------------------------------

    s1, s2 = st.columns(2)

    with s1:

        fig = px.bar(
            segment_summary,
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
            height=420,
            xaxis_title=None
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with s2:

        fig = px.bar(
            segment_summary,
            x="Segment Name",
            y="Churn Rate",
            text="Churn Rate",
            title="Churn Rate by Segment"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
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

    st.dataframe(
        segment_summary.round(2),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CHURN DRIVERS
# ============================================================

elif st.session_state.page == "Churn Drivers":

    page_header(
        "EXPLAINABLE AI",
        "Churn Drivers",
        "Understand which characteristics have the strongest influence on churn."
    )

    try:

        shap_df = pd.read_csv(
            "shap_feature_importance.csv"
        )

        shap_df.columns = (
            shap_df.columns
            .str.strip()
        )

        # Try to identify feature column
        feature_column = None

        for col in [
            "Feature",
            "feature",
            "Feature Name",
            "feature_name"
        ]:

            if col in shap_df.columns:

                feature_column = col
                break

        # Try to identify importance column
        importance_column = None

        for col in [
            "MeanAbsSHAP",
            "mean_abs_shap",
            "Importance",
            "importance"
        ]:

            if col in shap_df.columns:

                importance_column = col
                break

        if (
            feature_column is None
            or
            importance_column is None
        ):

            st.error(
                "SHAP file must contain a feature column "
                "and an importance column."
            )

        else:

            shap_df[importance_column] = pd.to_numeric(
                shap_df[importance_column],
                errors="coerce"
            )

            shap_df = shap_df.dropna(
                subset=[
                    feature_column,
                    importance_column
                ]
            )

            shap_df = shap_df.sort_values(
                importance_column,
                ascending=True
            )

            top_features = shap_df.tail(12)

            fig = px.bar(
                top_features,
                x=importance_column,
                y=feature_column,
                orientation="h",
                title="Top Churn Drivers"
            )

            fig.update_layout(
                template="plotly_white",
                height=550,
                xaxis_title="Feature Importance",
                yaxis_title=None
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # ------------------------------------------------
            # INSIGHT
            # ------------------------------------------------

            strongest = (
                shap_df
                .sort_values(
                    importance_column,
                    ascending=False
                )
                .head(3)[feature_column]
                .tolist()
            )

            strongest_text = ", ".join(
                map(str, strongest)
            )

            st.markdown(
                f"""
                <div class="insight">

                    <div class="insight-title">
                        ✦ Model Interpretation
                    </div>

                    <div class="insight-text">

                        The strongest model drivers are
                        <b>{strongest_text}</b>.

                        These features have the highest
                        overall contribution to the model's
                        churn predictions.

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        st.warning(
            "shap_feature_importance.csv was not found."
        )

        st.info(
            "Upload shap_feature_importance.csv to the "
            "same GitHub repository if you want to display "
            "SHAP-based churn drivers."
        )

    except Exception:

        st.error(
            "Unable to process the SHAP feature importance file."
        )


# ============================================================
# CUSTOMER EXPLORER
# ============================================================

elif st.session_state.page == "Customer Explorer":

    page_header(
        "RETENTION OPERATIONS",
        "Customer Explorer",
        "Inspect individual customer risk and retention recommendations."
    )

    # --------------------------------------------------------
    # FILTER
    # --------------------------------------------------------

    explorer_df = df.copy()

    if st.session_state.risk_filter:

        explorer_df = explorer_df[
            explorer_df["ChurnProbability"] >= 0.35
        ]

        st.info(
            f"Showing {len(explorer_df):,} at-risk customers."
        )

        if st.button(
            "Show All Customers",
            key="show_all"
        ):

            st.session_state.risk_filter = False
            st.rerun()

    # --------------------------------------------------------
    # CUSTOMER SELECTOR
    # --------------------------------------------------------

    customer_ids = sorted(
        explorer_df[
            "customerID"
        ]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    if not customer_ids:

        st.warning(
            "No customers are available."
        )

        st.stop()

    selected_customer = st.selectbox(
        "Select Customer ID",
        customer_ids,
        key="customer_dropdown"
    )

    # --------------------------------------------------------
    # CUSTOMER
    # --------------------------------------------------------

    customer_rows = df[
        df["customerID"]
        .astype(str)
        == str(selected_customer)
    ]

    if customer_rows.empty:

        st.error(
            "Customer not found."
        )

        st.stop()

    customer = customer_rows.iloc[0]

    probability = float(
        customer["ChurnProbability"]
    )

    # --------------------------------------------------------
    # RISK STYLE
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # PROFILE
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="profile">

            <div class="profile-label">
                CUSTOMER PROFILE
            </div>

            <div class="profile-name">
                Customer {selected_customer}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # RISK
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="risk-box {risk_class}">

            <div class="risk-label">
                PREDICTED CHURN RISK
            </div>

            <div class="risk-value">
                {probability:.1%}
            </div>

            <div style="
                color:#64748B;
                font-size:12px;
                margin-top:4px;
            ">
                {risk_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Customer Metrics</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3, m4 = st.columns(4)

    with m1:

        tenure = customer.get(
            "tenure",
            0
        )

        st.metric(
            "Tenure",
            f"{tenure} months"
        )

    with m2:

        monthly = customer.get(
            "MonthlyCharges",
            0
        )

        try:
            monthly = float(monthly)
        except:
            monthly = 0

        st.metric(
            "Monthly Charges",
            f"${monthly:,.2f}"
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

        churn = customer.get(
            "Churn",
            "N/A"
        )

        st.metric(
            "Historical Churn",
            str(churn)
        )

    # --------------------------------------------------------
    # CUSTOMER DETAILS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Customer Details</div>',
        unsafe_allow_html=True
    )

    wanted_columns = [
        "customerID",
        "Contract",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "InternetService",
        "PaymentMethod",
        "Churn",
        "Segment Name",
        "RiskLevel",
        "ChurnProbabilityPct"
    ]

    available_columns = [
        col for col in wanted_columns
        if col in df.columns
    ]

    details = pd.DataFrame({
        "Attribute": available_columns,
        "Value": [
            customer[col]
            for col in available_columns
        ]
    })

    st.dataframe(
        details,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------------
    # RECOMMENDATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Retention Recommendation</div>',
        unsafe_allow_html=True
    )

    recommendation = customer[
        "RetentionRecommendation"
    ]

    st.success(
        recommendation
    )

    # --------------------------------------------------------
    # EXPORT
    # --------------------------------------------------------

    customer_export = pd.DataFrame(
        [customer]
    )

    st.download_button(
        "↓  Download Customer Profile",
        data=customer_export.to_csv(
            index=False
        ),
        file_name=(
            f"{selected_customer}_profile.csv"
        ),
        mime="text/csv"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        Customer Churn Intelligence
        &nbsp; • &nbsp;
        Machine Learning
        &nbsp; • &nbsp;
        Customer Segmentation
        &nbsp; • &nbsp;
        Explainable AI

    </div>
    """,
    unsafe_allow_html=True
)
