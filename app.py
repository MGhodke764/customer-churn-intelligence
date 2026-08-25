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

/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background: #0b1220;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
}

/* ============================================================
   BRAND
   ============================================================ */

.brand-wrapper {
    padding: 10px 18px 30px 18px;
}

.brand-mark {
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
}

.brand-name {
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    margin-left: 8px;
}

.brand-sub {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 8px;
    line-height: 1.5;
}

/* ============================================================
   SIDEBAR SECTION TITLES
   ============================================================ */

.sidebar-title {
    color: #64748b;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin: 22px 18px 12px 18px;
}

/* ============================================================
   SIDEBAR BUTTONS
   ============================================================ */

[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border: none;
    background: transparent;
    color: #e2e8f0;
    text-align: left;
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #172033;
    color: #ffffff;
    border: none;
}

/* ============================================================
   QUICK ACTIONS
   ============================================================ */

.quick-action {
    padding: 8px 18px;
    font-size: 13px;
    font-weight: 600;
    color: #f8fafc;
}

.quick-action-high {
    color: #f87171;
}

.quick-action-reset {
    color: #94a3b8;
}

/* ============================================================
   MAIN HEADER
   ============================================================ */

.page-header {
    padding: 12px 0 28px 0;
}

.eyebrow {
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}

.main-title {
    color: #0f172a;
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 8px;
}

.main-subtitle {
    color: #64748b;
    font-size: 14px;
}

.status-pill {
    display: inline-block;
    background: #ecfdf5;
    color: #059669;
    padding: 7px 12px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}

/* ============================================================
   KPI CARDS
   ============================================================ */

.kpi-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px;
    min-height: 120px;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
}

.kpi-title {
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 12px;
}

.kpi-value {
    color: #0f172a;
    font-size: 26px;
    font-weight: 800;
}

.kpi-icon {
    color: #64748b;
    font-size: 20px;
    margin-top: 8px;
}

/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: #0f172a;
    font-size: 20px;
    font-weight: 750;
    margin-top: 28px;
    margin-bottom: 14px;
}

.section-subtitle {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 18px;
}

/* ============================================================
   INSIGHT CARD
   ============================================================ */

.insight-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 22px;
    margin-top: 10px;
}

.insight-title {
    color: #0f172a;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 10px;
}

.insight-text {
    color: #475569;
    font-size: 13px;
    line-height: 1.7;
}

/* ============================================================
   RISK CARDS
   ============================================================ */

.risk-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px;
}

.risk-title {
    color: #0f172a;
    font-size: 14px;
    font-weight: 700;
}

.risk-value {
    color: #0f172a;
    font-size: 24px;
    font-weight: 800;
    margin-top: 8px;
}

.risk-critical {
    display: inline-block;
    background: #fee2e2;
    color: #dc2626;
    padding: 6px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}

.risk-high {
    display: inline-block;
    background: #ffedd5;
    color: #ea580c;
    padding: 6px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}

.risk-medium {
    display: inline-block;
    background: #fef3c7;
    color: #d97706;
    padding: 6px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}

.risk-low {
    display: inline-block;
    background: #dcfce7;
    color: #16a34a;
    padding: 6px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}

/* ============================================================
   CUSTOMER PROFILE
   ============================================================ */

.profile-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 24px;
    margin-top: 12px;
}

.profile-title {
    color: #0f172a;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 12px;
}

.profile-label {
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.7px;
    margin-top: 12px;
}

.profile-value {
    color: #0f172a;
    font-size: 14px;
    font-weight: 600;
    margin-top: 4px;
}

/* ============================================================
   MODEL TEXT
   ============================================================ */

.model-text {
    color: #475569;
    font-size: 13px;
    line-height: 1.7;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 18px 20px;
    margin-top: 8px;
}

/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

/* ============================================================
   SELECTBOX
   ============================================================ */

.stSelectbox label {
    color: #334155;
    font-weight: 600;
}

/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 11px;
    padding: 30px 0 15px 0;
}

</style>
""", unsafe_allow_html=True)
