import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

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
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b1425;
}

section[data-testid="stSidebar"] > div {
    background: #0b1425;
}

.sidebar-brand {
    padding: 18px 4px 28px 4px;
}

.sidebar-title {
    color: white;
    font-size: 24px;
    font-weight: 800;
    line-height: 1.2;
}

.sidebar-subtitle {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 8px;
}

.sidebar-section {
    color: #64748b;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Main header */
.page-eyebrow {
    color: #2563eb;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.page-title {
    color: #0f172a;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 5px;
}

.page-subtitle {
    color: #64748b;
    font-size: 15px;
    margin-bottom: 24px;
}

/* Cards */
.kpi-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 20px;
    min-height: 135px;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
}

.kpi-label {
    color: #64748b;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.kpi-value {
    color: #0f172a;
    font-size: 30px;
    font-weight: 800;
    margin-top: 10px;
}

.kpi-description {
    color: #94a3b8;
    font-size: 11px;
    margin-top: 5px;
}

/* Section headings */
.section-title {
    color: #0f172a;
    font-size: 24px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 18px;
}

/* Insight card */
.insight-card {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 16px;
    padding: 22px;
    margin-top: 18px;
}

.insight-title {
    color: #1d4ed8;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 8px;
}

.insight-text {
    color: #334155;
    font-size: 13px;
    line-height: 1.7;
}

/* Risk badges */
.risk-critical {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: #fee2e2;
    color: #b91c1c;
    font-size: 12px;
    font-weight: 800;
}

.risk-high {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: #ffedd5;
    color: #c2410c;
    font-size: 12px;
    font-weight: 800;
}

.risk-medium {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: #fef3c7;
    color: #a16207;
    font-size: 12px;
    font-weight: 800;
}

.risk-low {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: #dcfce7;
    color: #15803d;
    font-size: 12px;
    font-weight: 800;
}

/* Customer profile */
.profile-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
}

.profile-title {
    color: #0f172a;
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 12px;
}

/* Model card */
.model-card {
    background: #0f1b32;
    border-radius: 18px;
    padding: 24px;
    color: white;
}

.model-title {
    color: white;
    font-size: 18px;
    font-weight: 800;
}

.model-text {
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.6;
}

.model-number {
    color: white;
    font-size: 30px;
    font-weight: 800;
}

/* Footer */
.footer {
    border-top: 1px solid #e2e8f0;
    margin-top: 50px;
    padding-top: 20px;
    text-align: center;
    color: #94a3b8;
    font-size: 11px;
}

/* Streamlit buttons */
.stButton > button {
    border-radius: 10px;
    border: 1px solid #dbe3ef;
    font-weight: 600;
    min-height: 42px;
}

.stButton > button:hover {
    border-color: #2563eb;
    color: #2563eb;
}

/* Select box */
div[data-baseweb="select"] > div {
    border-radius: 10px;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 12px;
}

/* Mobile */
@media (max-width: 900px) {
    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    possible_files = [
        "telco_churn_powerbi.csv",
        "telco_churn.csv",
        "customer_churn.csv",
        "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    ]

    for file in possible_files:
        try:
            df = pd.read_csv(file)
            return df
        except:
            continue

    return None


df = load_data()

if df is None:
    st.error(
        "Dataset not found. Please upload telco_churn_powerbi.csv "
        "to the same GitHub repository as app.py."
    )
    st.stop()


# ============================================================
# CLEAN DATA
# ============================================================

df.columns = df.columns.str.strip()

# Standardize common column names

rename_map = {}

for col in df.columns:

    low = col.lower().replace(" ", "").replace("_", "")

    if low == "customerid":
        rename_map[col] = "customerID"

    elif low == "monthlycharges":
        rename_map[col] = "MonthlyCharges"

    elif low == "totalcharges":
        rename_map[col] = "TotalCharges"

    elif low == "tenure":
        rename_map[col] = "tenure"

    elif low == "churn":
        rename_map[col] = "Churn"

    elif low == "contract":
        rename_map[col] = "Contract"

    elif low == "paymentmethod":
        rename_map[col] = "PaymentMethod"

    elif low == "internetservice":
        rename_map[col] = "InternetService"

    elif low == "phoneservice":
        rename_map[col] = "PhoneService"

    elif low == "seniorcitizen":
        rename_map[col] = "SeniorCitizen"

df = df.rename(columns=rename_map)


# Numeric conversion

for col in ["MonthlyCharges", "TotalCharges", "tenure", "SeniorCitizen"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")


# Remove completely empty rows

df = df.dropna(how="all").reset_index(drop=True)


# ============================================================
# CUSTOMER ID
# ============================================================

if "customerID" not in df.columns:

    df["customerID"] = [
        f"CUST-{i+1:04d}"
        for i in range(len(df))
    ]


# ============================================================
# CHURN NORMALIZATION
# ============================================================

if "Churn" in df.columns:

    df["Churn"] = (
        df["Churn"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["ChurnFlag"] = df["Churn"].map({
        "yes": 1,
        "no": 0,
        "1": 1,
        "0": 0,
        "true": 1,
        "false": 0
    })

else:

    df["Churn"] = "No"
    df["ChurnFlag"] = 0


df["ChurnFlag"] = df["ChurnFlag"].fillna(0).astype(int)


# ============================================================
# RISK SCORE
# ============================================================

def calculate_risk(data):

    risk = np.zeros(len(data))

    # Month-to-month contracts
    if "Contract" in data.columns:
        contract = data["Contract"].astype(str).str.lower()

        risk += np.where(
            contract.str.contains("month"),
            0.30,
            0
        )

        risk += np.where(
            contract.str.contains("one year"),
            0.08,
            0
        )

    # Short tenure
    if "tenure" in data.columns:

        tenure = pd.to_numeric(
            data["tenure"],
            errors="coerce"
        ).fillna(0)

        risk += np.where(tenure <= 6, 0.25, 0)
        risk += np.where((tenure > 6) & (tenure <= 12), 0.12, 0)

    # High monthly charges
    if "MonthlyCharges" in data.columns:

        monthly = pd.to_numeric(
            data["MonthlyCharges"],
            errors="coerce"
        ).fillna(0)

        q75 = monthly.quantile(0.75)

        risk += np.where(
            monthly >= q75,
            0.15,
            0
        )

    # Electronic check
    if "PaymentMethod" in data.columns:

        payment = data["PaymentMethod"].astype(str).str.lower()

        risk += np.where(
            payment.str.contains("electronic"),
            0.15,
            0
        )

    # Internet service
    if "InternetService" in data.columns:

        internet = data["InternetService"].astype(str).str.lower()

        risk += np.where(
            internet.str.contains("fiber"),
            0.10,
            0
        )

    return np.clip(risk, 0, 1)


df["RiskScore"] = calculate_risk(df)


# ============================================================
# RISK LEVEL
# ============================================================

def risk_label(score):

    if score >= 0.65:
        return "Critical"

    elif score >= 0.45:
        return "High"

    elif score >= 0.25:
        return "Medium"

    return "Low"


df["RiskLevel"] = df["RiskScore"].apply(risk_label)


# ============================================================
# CUSTOMER SEGMENTS
# ============================================================

def create_segments(data):

    numeric_cols = []

    for col in [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]:

        if col in data.columns:
            numeric_cols.append(col)

    if len(numeric_cols) < 2:

        data["Segment Name"] = "General"

        return data

    temp = data[numeric_cols].copy()

    temp = temp.fillna(
        temp.median(numeric_only=True)
    )

    scaler = StandardScaler()

    scaled = scaler.fit_transform(temp)

    n_clusters = min(4, len(data))

    if n_clusters < 2:

        data["Segment Name"] = "General"

        return data

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(scaled)

    data["Cluster"] = labels

    # Give meaningful names based on cluster averages

    summary = (
        data
        .groupby("Cluster", as_index=False)
        [numeric_cols]
        .mean(numeric_only=True)
    )

    summary["Score"] = (
        summary["MonthlyCharges"].rank(pct=True)
        + (1 - summary["tenure"].rank(pct=True))
    )

    summary = summary.sort_values("Score")

    names = [
        "Loyal Customers",
        "Growth Customers",
        "Value Customers",
        "At-Risk Customers"
    ]

    mapping = {}

    for i, cluster in enumerate(summary["Cluster"]):

        mapping[
            cluster
        ] = names[min(i, len(names)-1)]

    data["Segment Name"] = data["Cluster"].map(mapping)

    data["Segment Name"] = data["Segment Name"].fillna(
        "General"
    )

    return data


df = create_segments(df)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:

    st.session_state.page = "Executive Overview"


def go_to(page):

    st.session_state.page = page


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-title">◆ Customer<br>Intelligence</div>
        <div class="sidebar-subtitle">
            AI-Powered Retention Analytics
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section">WORKSPACE</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "▣  Executive Overview",
        use_container_width=True
    ):
        go_to("Executive Overview")

    if st.button(
        "◉  Risk Analytics",
        use_container_width=True
    ):
        go_to("Risk Analytics")

    if st.button(
        "○  Customer Segments",
        use_container_width=True
    ):
        go_to("Customer Segments")

    if st.button(
        "✦  Churn Drivers",
        use_container_width=True
    ):
        go_to("Churn Drivers")

    if st.button(
        "⌕  Customer Explorer",
        use_container_width=True
    ):
        go_to("Customer Explorer")

    st.markdown(
        '<div class="sidebar-section">QUICK ACTIONS</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "⚠  High-Risk Customers",
        use_container_width=True
    ):
        go_to("Risk Analytics")

    if st.button(
        "↻  Reset Workspace",
        use_container_width=True
    ):
        st.session_state.page = "Executive Overview"
        st.rerun()

    st.markdown("---")

    st.markdown("""
    <div style="
        color:#e2e8f0;
        font-size:13px;
        font-weight:700;">
        Customer Churn Intelligence
    </div>

    <div style="
        color:#94a3b8;
        font-size:11px;
        margin-top:8px;
        line-height:1.8;">
        Data Science Portfolio Project<br><br>
        Model: Churn Risk Analytics<br>
        Analytics: EDA + Segmentation + Drivers
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def page_header(title, subtitle, eyebrow="CUSTOMER ANALYTICS PLATFORM"):

    st.markdown(
        f"""
        <div class="page-eyebrow">{eyebrow}</div>
        <div class="page-title">{title}</div>
        <div class="page-subtitle">{subtitle}</div>
        """,
        unsafe_allow_html=True
    )


def kpi(label, value, description):

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def risk_badge(level):

    css = {
        "Critical": "risk-critical",
        "High": "risk-high",
        "Medium": "risk-medium",
        "Low": "risk-low"
    }.get(level, "risk-low")

    return f'<span class="{css}">{level} Risk</span>'


def numeric_series(column):

    if column not in df.columns:

        return pd.Series(
            np.zeros(len(df))
        )

    return pd.to_numeric(
        df[column],
        errors="coerce"
    ).fillna(0)


# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if st.session_state.page == "Executive Overview":

    page_header(
        "Customer Churn Intelligence",
        "Executive command center for proactive customer retention and churn risk management."
    )

    total_customers = len(df)

    churn_rate = (
        df["ChurnFlag"].mean() * 100
        if len(df) > 0
        else 0
    )

    at_risk = int(
        (df["RiskScore"] >= 0.35).sum()
    )

    high_critical = int(
        df["RiskLevel"].isin(
            ["High", "Critical"]
        ).sum()
    )

    avg_risk = (
        df["RiskScore"].mean() * 100
        if len(df) > 0
        else 0
    )

    cols = st.columns(5)

    with cols[0]:
        kpi(
            "Total Customers",
            f"{total_customers:,}",
            "Customer base"
        )

    with cols[1]:
        kpi(
            "Churn Rate",
            f"{churn_rate:.1f}%",
            "Historical churn"
        )

    with cols[2]:
        kpi(
            "At-Risk Customers",
            f"{at_risk:,}",
            "Risk score ≥ 35%"
        )

    with cols[3]:
        kpi(
            "High / Critical",
            f"{high_critical:,}",
            "Priority customers"
        )

    with cols[4]:
        kpi(
            "Avg Model Risk",
            f"{avg_risk:.1f}%",
            "Average risk score"
        )

    st.markdown(
        '<div class="section-title">Retention Risk Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Customer risk distribution and contract-level churn behavior.</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

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

        fig.update_layout(
            height=390,
            margin=dict(l=20, r=20, t=55, b=20),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        if "Contract" in df.columns:

            contract_data = (
                df.groupby("Contract", as_index=False)
                ["ChurnFlag"]
                .mean()
            )

            contract_data["Churn Rate"] = (
                contract_data["ChurnFlag"] * 100
            )

            fig = px.bar(
                contract_data,
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
                height=390,
                margin=dict(l=20, r=20, t=55, b=20),
                plot_bgcolor="white",
                paper_bgcolor="white"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-title">
                ◆ Executive Insight
            </div>
            <div class="insight-text">
                Customers with short tenure, month-to-month contracts,
                higher monthly charges and electronic payment methods
                show stronger retention risk signals. These groups should
                receive proactive retention campaigns.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PAGE 2 — RISK ANALYTICS
# ============================================================

elif st.session_state.page == "Risk Analytics":

    page_header(
        "Risk Analytics",
        "Identify priority customers and understand the distribution of churn risk."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        kpi(
            "Critical",
            f"{(df['RiskLevel'] == 'Critical').sum():,}",
            "Immediate attention"
        )

    with c2:
        kpi(
            "High",
            f"{(df['RiskLevel'] == 'High').sum():,}",
            "Priority retention"
        )

    with c3:
        kpi(
            "Medium",
            f"{(df['RiskLevel'] == 'Medium').sum():,}",
            "Monitor closely"
        )

    st.markdown(
        '<div class="section-title">Risk Distribution</div>',
        unsafe_allow_html=True
    )

    fig = px.pie(
        df,
        names="RiskLevel",
        hole=0.55,
        title="Customer Risk Mix"
    )

    fig.update_layout(
        height=430,
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        '<div class="section-title">High-Risk Customer List</div>',
        unsafe_allow_html=True
    )

    high_risk = df[
        df["RiskLevel"].isin(
            ["Critical", "High"]
        )
    ].copy()

    high_risk["Risk Score"] = (
        high_risk["RiskScore"] * 100
    ).round(1)

    display_cols = [
        "customerID",
        "RiskLevel",
        "Risk Score"
    ]

    for col in [
        "Contract",
        "tenure",
        "MonthlyCharges",
        "Churn"
    ]:
        if col in high_risk.columns:
            display_cols.append(col)

    high_risk = high_risk.sort_values(
        "Risk Score",
        ascending=False
    )

    st.dataframe(
        high_risk[display_cols].head(100),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 3 — CUSTOMER SEGMENTS
# ============================================================

elif st.session_state.page == "Customer Segments":

    page_header(
        "Customer Segmentation",
        "Group customers into meaningful behavioral and value-based segments."
    )

    segment_summary = (
        df.groupby("Segment Name", as_index=False)
        .agg(
            Customers=("customerID", "count"),
            Avg_Tenure=("tenure", "mean")
            if "tenure" in df.columns
            else ("customerID", "count")
        )
    )

    # Fix duplicate aggregation issue if tenure missing

    if "tenure" not in df.columns:

        segment_summary["Avg_Tenure"] = 0

    segment_summary["Avg_Tenure"] = (
        pd.to_numeric(
            segment_summary["Avg_Tenure"],
            errors="coerce"
        )
        .fillna(0)
        .round(1)
    )

    c1, c2 = st.columns(2)

    with c1:

        fig = px.bar(
            segment_summary,
            x="Segment Name",
            y="Customers",
            text="Customers",
            title="Customers by Segment"
        )

        fig.update_layout(
            height=400,
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.bar(
            segment_summary,
            x="Segment Name",
            y="Avg_Tenure",
            text="Avg_Tenure",
            title="Average Tenure by Segment"
        )

        fig.update_layout(
            height=400,
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown(
        '<div class="section-title">Segment Summary</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        segment_summary,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 4 — CHURN DRIVERS
# ============================================================

elif st.session_state.page == "Churn Drivers":

    page_header(
        "Churn Drivers",
        "Key customer attributes associated with elevated churn and retention risk."
    )

    drivers = []

    # Contract

    if "Contract" in df.columns:

        temp = (
            df.groupby("Contract")["ChurnFlag"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        for _, row in temp.iterrows():

            drivers.append({
                "Driver": f"Contract: {row['Contract']}",
                "Churn Rate": row["ChurnFlag"] * 100
            })

    # Payment method

    if "PaymentMethod" in df.columns:

        temp = (
            df.groupby("PaymentMethod")["ChurnFlag"]
            .mean()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )

        for _, row in temp.iterrows():

            drivers.append({
                "Driver": f"Payment: {row['PaymentMethod']}",
                "Churn Rate": row["ChurnFlag"] * 100
            })

    # Internet service

    if "InternetService" in df.columns:

        temp = (
            df.groupby("InternetService")["ChurnFlag"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        for _, row in temp.iterrows():

            drivers.append({
                "Driver": f"Internet: {row['InternetService']}",
                "Churn Rate": row["ChurnFlag"] * 100
            })

    if len(drivers) > 0:

        drivers_df = pd.DataFrame(drivers)

        drivers_df = drivers_df.sort_values(
            "Churn Rate",
            ascending=False
        ).head(10)

        fig = px.bar(
            drivers_df,
            x="Churn Rate",
            y="Driver",
            orientation="h",
            text="Churn Rate",
            title="Highest Churn-Associated Customer Attributes"
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(
            height=500,
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-title">
                ◆ Model Interpretation
            </div>

            <div class="insight-text">
                The strongest retention risk signals are associated with
                <b>contract type</b>, <b>customer tenure</b>,
                <b>monthly charges</b>, and <b>payment method</b>.
                These variables should receive priority when designing
                customer retention strategies.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Tenure vs Monthly Charges</div>',
        unsafe_allow_html=True
    )

    if (
        "tenure" in df.columns
        and "MonthlyCharges" in df.columns
    ):

        fig = px.scatter(
            df,
            x="tenure",
            y="MonthlyCharges",
            color="RiskLevel",
            hover_data=["customerID"],
            title="Customer Risk by Tenure and Monthly Charges"
        )

        fig.update_layout(
            height=450,
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# PAGE 5 — CUSTOMER EXPLORER
# ============================================================

elif st.session_state.page == "Customer Explorer":

    page_header(
        "Customer Explorer",
        "Search and inspect individual customer profiles and retention risk."
    )

    customer_ids = (
        df["customerID"]
        .astype(str)
        .dropna()
        .unique()
        .tolist()
    )

    selected_customer = st.selectbox(
        "Select Customer ID",
        customer_ids,
        index=0
    )

    customer = df[
        df["customerID"].astype(str)
        == str(selected_customer)
    ]

    if len(customer) == 0:

        st.warning("Customer not found.")

    else:

        customer = customer.iloc[0]

        level = customer["RiskLevel"]

        st.markdown(
            f"""
            <div class="profile-card">
                <div class="page-eyebrow">
                    CUSTOMER PROFILE
                </div>

                <div class="profile-title">
                    Customer {customer["customerID"]}
                </div>

                {risk_badge(level)}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-title">Customer Metrics</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            value = customer.get(
                "tenure",
                0
            )

            kpi(
                "Tenure",
                f"{value}",
                "Months"
            )

        with c2:

            value = customer.get(
                "MonthlyCharges",
                0
            )

            kpi(
                "Monthly Charges",
                f"${float(value):,.2f}",
                "Monthly spend"
            )

        with c3:

            value = customer.get(
                "TotalCharges",
                0
            )

            try:
                formatted = f"${float(value):,.2f}"
            except:
                formatted = str(value)

            kpi(
                "Total Charges",
                formatted,
                "Customer lifetime value"
            )

        with c4:

            kpi(
                "Risk Score",
                f"{customer['RiskScore'] * 100:.1f}%",
                "Estimated retention risk"
            )

        st.markdown(
            '<div class="section-title">Customer Profile</div>',
            unsafe_allow_html=True
        )

        profile_fields = [
            "customerID",
            "Contract",
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
            "Churn",
            "Segment Name",
            "RiskLevel",
            "PaymentMethod",
            "InternetService"
        ]

        profile_data = []

        for field in profile_fields:

            if field in df.columns:

                profile_data.append({
                    "Attribute": field,
                    "Value": customer[field]
                })

        profile_df = pd.DataFrame(
            profile_data
        )

        st.dataframe(
            profile_df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown(
            """
            <div class="model-card">
                <div class="model-title">
                    Retention Recommendation
                </div>

                <br>

                <div class="model-text">
                    Customers classified as High or Critical Risk
                    should be prioritized for proactive retention
                    campaigns, personalized offers and customer
                    support follow-ups.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Customer Churn Intelligence &nbsp;•&nbsp;
        Data Science Portfolio Project &nbsp;•&nbsp;
        EDA + Segmentation + Churn Risk Analytics
    </div>
    """,
    unsafe_allow_html=True
)
