import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="◆",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #F7F9FC;
}

.block-container {
    max-width: 1450px;
    padding: 2rem 3rem 3rem 3rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

section[data-testid="stSidebar"] {
    display: none;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 22px;
}

.brand-icon {
    background: #2563EB;
    color: white;
    width: 44px;
    height: 44px;
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
    font-size: 12px;
    color: #64748B;
}

.nav-card {
    background: white;
    border: 1px solid #E2E8F0;
    padding: 8px;
    border-radius: 14px;
    margin-bottom: 25px;
}

.stButton > button {
    border-radius: 10px !important;
    border: 1px solid #E2E8F0 !important;
    background: white !important;
    color: #334155 !important;
    font-weight: 700 !important;
    min-height: 42px !important;
}

.stButton > button:hover {
    background: #EFF6FF !important;
    color: #2563EB !important;
    border-color: #2563EB !important;
}

.eyebrow {
    color: #2563EB;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 5px;
}

.title {
    color: #0F172A;
    font-size: 34px;
    font-weight: 800;
}

.subtitle {
    color: #64748B;
    font-size: 13px;
    margin-top: 5px;
    margin-bottom: 25px;
}

.kpi {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
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
    margin-top: 10px;
}

.section {
    color: #0F172A;
    font-size: 20px;
    font-weight: 800;
    margin-top: 32px;
    margin-bottom: 12px;
}

.profile {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 22px;
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
    margin-top: 6px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv("telco_churn_powerbi.csv")

    data.columns = data.columns.str.strip()

    # Customer ID
    if "customerID" not in data.columns:

        possible_id = [
            c for c in data.columns
            if c.lower().replace("_", "").replace(" ", "")
            == "customerid"
        ]

        if possible_id:
            data["customerID"] = data[possible_id[0]]

        else:
            data["customerID"] = [
                f"CUST-{i:04d}"
                for i in range(1, len(data) + 1)
            ]

    # Churn flag
    if "ChurnFlag" not in data.columns:

        if "Churn" in data.columns:

            data["ChurnFlag"] = (
                data["Churn"]
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
            data["ChurnFlag"] = 0

    # Churn probability
    if "ChurnProbability" not in data.columns:

        if "ChurnProbabilityPct" in data.columns:

            data["ChurnProbability"] = (
                pd.to_numeric(
                    data["ChurnProbabilityPct"],
                    errors="coerce"
                ) / 100
            )

        else:

            data["ChurnProbability"] = (
                data["ChurnFlag"].astype(float)
            )

    data["ChurnProbability"] = (
        pd.to_numeric(
            data["ChurnProbability"],
            errors="coerce"
        )
        .fillna(0)
        .clip(0, 1)
    )

    # Risk
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

    # Segment
    if "Segment Name" not in data.columns:

        if "CustomerSegment" in data.columns:

            segment = pd.to_numeric(
                data["CustomerSegment"],
                errors="coerce"
            )

            data["Segment Name"] = segment.map({
                0: "New / Low-Engagement",
                1: "High-Value Loyal",
                2: "Long-Term Low-Spend",
                3: "High-Risk / At-Risk"
            }).fillna("Other")

        else:

            data["Segment Name"] = pd.cut(
                data["ChurnProbability"],
                bins=[-0.01, 0.25, 0.50, 0.70, 1.01],
                labels=[
                    "Low Risk",
                    "Medium Risk",
                    "High Risk",
                    "Critical Risk"
                ]
            ).astype(str)

    return data


# ============================================================
# LOAD
# ============================================================

try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "Could not find telco_churn_powerbi.csv. "
        "Make sure the CSV is in the same GitHub repository."
    )

    st.stop()

except Exception as e:

    st.error(f"Could not load the dataset: {e}")

    st.stop()


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

    <div class="brand-icon">◆</div>

    <div>
        <div class="brand-title">
            Customer Intelligence
        </div>

        <div class="brand-subtitle">
            AI-Powered Customer Retention Analytics
        </div>
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown(
    '<div class="nav-card">',
    unsafe_allow_html=True
)

c1, c2, c3, c4, c5 = st.columns(5)

if "page" not in st.session_state:
    st.session_state.page = "Overview"

with c1:
    if st.button("▣  Overview", use_container_width=True):
        st.session_state.page = "Overview"
        st.rerun()

with c2:
    if st.button("◉  Risk Analytics", use_container_width=True):
        st.session_state.page = "Risk"
        st.rerun()

with c3:
    if st.button("○  Segments", use_container_width=True):
        st.session_state.page = "Segments"
        st.rerun()

with c4:
    if st.button("✦  Churn Drivers", use_container_width=True):
        st.session_state.page = "Drivers"
        st.rerun()

with c5:
    if st.button("⌕  Customer Explorer", use_container_width=True):
        st.session_state.page = "Customers"
        st.rerun()

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ============================================================
# OVERVIEW
# ============================================================

if st.session_state.page == "Overview":

    st.markdown(
        '<div class="eyebrow">CUSTOMER INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Customer Churn Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Monitor customer health, identify churn risk, and prioritize retention opportunities.</div>',
        unsafe_allow_html=True
    )

    total = len(df)

    churned = int(df["ChurnFlag"].sum())

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

    average_risk = df[
        "ChurnProbability"
    ].mean()

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">TOTAL CUSTOMERS</div>
                <div class="kpi-value">{total:,}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k2:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">CHURN RATE</div>
                <div class="kpi-value">{churn_rate:.1%}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k3:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">AT-RISK CUSTOMERS</div>
                <div class="kpi-value">{at_risk:,}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k4:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">CRITICAL RISK</div>
                <div class="kpi-value">{critical:,}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k5:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">AVERAGE MODEL RISK</div>
                <div class="kpi-value">{average_risk:.1%}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section">Risk Overview</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:

        risk_counts = (
            df["RiskLevel"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Medium", "Low"],
                fill_value=0
            )
            .reset_index()
        )

        risk_counts.columns = [
            "Risk Level",
            "Customers"
        ]

        fig = px.bar(
            risk_counts,
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
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        if "Contract" in df.columns:

            contract = (
                df.groupby("Contract")["ChurnFlag"]
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
                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.info(
                "Contract column is not available in the dataset."
            )


# ============================================================
# RISK
# ============================================================

elif st.session_state.page == "Risk":

    st.markdown(
        '<div class="eyebrow">RISK MANAGEMENT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Risk Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Explore predicted churn probability across the customer base.</div>',
        unsafe_allow_html=True
    )

    minimum_risk = st.slider(
        "Minimum Churn Probability",
        0.0,
        1.0,
        0.35,
        0.05
    )

    risk_df = df[
        df["ChurnProbability"] >= minimum_risk
    ].copy()

    st.metric(
        "Customers Matching Filter",
        f"{len(risk_df):,}"
    )

    if len(risk_df) > 0:

        x_column = (
            "tenure"
            if "tenure" in risk_df.columns
            else "ChurnProbability"
        )

        fig = px.scatter(
            risk_df,
            x=x_column,
            y="ChurnProbability",
            color="RiskLevel",
            hover_data=["customerID"],
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

        display_columns = [
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
                display_columns
            ].sort_values(
                "ChurnProbability",
                ascending=False
            ),
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No customers match this risk threshold."
        )


# ============================================================
# SEGMENTS
# ============================================================

elif st.session_state.page == "Segments":

    st.markdown(
        '<div class="eyebrow">CUSTOMER STRATEGY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Analyze customer groups and compare their churn behavior.</div>',
        unsafe_allow_html=True
    )

    # IMPORTANT:
    # This prevents the previous Segment Name KeyError.

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
            Customers=("customerID", "count"),
            Churn_Rate=("ChurnFlag", "mean")
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

        fig.update_layout(
            template="plotly_white",
            height=430
        )

        fig.update_traces(
            textposition="outside"
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
        '<div class="eyebrow">EXPLAINABLE AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Churn Drivers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Identify the variables most associated with customer churn.</div>',
        unsafe_allow_html=True
    )

    # Use SHAP file if available

    try:

        shap = pd.read_csv(
            "shap_feature_importance.csv"
        )

        shap.columns = shap.columns.str.strip()

        feature_col = None
        importance_col = None

        for c in [
            "Feature",
            "feature",
            "Feature Name",
            "feature_name"
        ]:
            if c in shap.columns:
                feature_col = c
                break

        for c in [
            "MeanAbsSHAP",
            "mean_abs_shap",
            "Importance",
            "importance"
        ]:
            if c in shap.columns:
                importance_col = c
                break

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

            top = shap.sort_values(
                importance_col
            ).tail(12)

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
                "SHAP file columns were not recognized."
            )

    except FileNotFoundError:

        st.info(
            "Add shap_feature_importance.csv to display "
            "your model's feature importance."
        )


# ============================================================
# CUSTOMER EXPLORER
# ============================================================

elif st.session_state.page == "Customers":

    st.markdown(
        '<div class="eyebrow">RETENTION OPERATIONS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Select a customer to inspect their individual churn profile.</div>',
        unsafe_allow_html=True
    )

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

    if probability >= 0.70:
        risk = "Critical Risk"
    elif probability >= 0.50:
        risk = "High Risk"
    elif probability >= 0.35:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    st.markdown(
        f"""
        <div class="profile">

            <div class="profile-label">
                CUSTOMER PROFILE
            </div>

            <div class="profile-name">
                Customer {selected_id}
            </div>

            <div style="
                margin-top:10px;
                color:#2563EB;
                font-weight:800;
                font-size:14px;
            ">
                {risk}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section">Customer Metrics</div>',
        unsafe_allow_html=True
    )

    a, b, c, d = st.columns(4)

    with a:

        tenure = customer.get(
            "tenure",
            0
        )

        st.metric(
            "Tenure",
            f"{tenure} months"
        )

    with b:

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

    with c:

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

    with d:

        st.metric(
            "Churn Probability",
            f"{probability:.1%}"
        )

    st.markdown(
        '<div class="section">Customer Details</div>',
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

    st.markdown(
        '<div class="section">Retention Recommendation</div>',
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
            "Monitor this customer closely and consider "
            "targeted engagement."
        )

    else:

        recommendation = (
            "Customer currently shows relatively low churn risk. "
            "Continue normal engagement."
        )

    st.success(
        recommendation
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div style="
        margin-top:45px;
        padding-top:15px;
        border-top:1px solid #E2E8F0;
        text-align:center;
        color:#94A3B8;
        font-size:11px;
    ">
        Customer Churn Intelligence
        • Machine Learning
        • Customer Segmentation
        • Explainable AI
    </div>
    """,
    unsafe_allow_html=True
)
