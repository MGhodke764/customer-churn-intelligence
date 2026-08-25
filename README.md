# customer-churn-intelligence
AI-powered customer churn prediction, segmentation and retention analytics
CHURNIQ – Customer Churn Intelligence Platform
###📌 Overview
CHURNIQ is an interactive customer churn intelligence platform designed to help businesses identify customers who are likely to churn and take proactive retention actions.

The platform combines Machine Learning, Customer Segmentation, Model Explainability, and Data Visualization into a single Streamlit dashboard.

It provides insights at both the business level and individual customer level, helping identify high-risk customers, understand churn drivers, and prioritize retention efforts.

🎯 Objectives
Predict the probability of customer churn.

Identify high-risk and at-risk customers.

Segment customers based on behavioral characteristics.

Understand the factors influencing churn predictions.

Provide actionable customer retention recommendations.

Build an interactive dashboard for business decision-making.

🚀 Key Features
📊 Executive Overview
Total customer count

Overall churn rate

At-risk customer count

High/Critical risk customers

Average model risk

Customer risk distribution

Churn rate by contract type

Executive-level retention insights

⚠️ Risk Analytics
Filter customers by risk level.

Filter by contract type.

Set a minimum churn probability.

Interactive customer risk map.

Analyze tenure, monthly charges, and churn probability.

👥 Customer Segmentation
Customers are grouped into behavioral segments:

New / Low-Engagement

High-Value Loyal

Long-Term Low-Spend

High-Risk / At-Risk

The dashboard compares customer distribution, average tenure, monthly charges, and churn rate across segments.

🔍 Churn Drivers
Uses SHAP (SHapley Additive exPlanations) to visualize the most influential factors affecting churn predictions.

The dashboard provides:

Top 15 churn-influencing features

SHAP feature importance visualization

Feature importance table

👤 Customer Explorer
Allows users to select a specific customer ID and view:

Predicted churn probability

Risk level

Customer tenure

Monthly charges

Contract type

Internet service

Retention recommendation

Priority customer list

High-risk customers can also be filtered directly through the Quick Actions section.

🤖 Machine Learning
The project uses an XGBoost Classifier for customer churn prediction.

Model Information
Algorithm: XGBoost Classifier

ROC-AUC: 0.841

Intervention Threshold: 35%

Explainability: SHAP

Customers with a predicted churn probability of 35% or higher are treated as an intervention/at-risk population.

👥 Customer Segmentation
K-Means clustering is used to identify customer groups based on customer characteristics.

The resulting segments help distinguish different customer behaviors and enable more targeted retention strategies.

🧠 Model Explainability
SHAP is used to understand how individual features contribute to the model's churn predictions.

This makes the ML model more interpretable and helps translate model results into business insights.

