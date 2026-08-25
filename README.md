# CHURNIQ — Customer Churn Intelligence
### Overview
CHURNIQ is a customer churn intelligence and retention analytics application built with Python, Streamlit, XGBoost, K-Means, SHAP, Pandas, and Plotly.

The application analyzes customer behavior and churn probability to help identify customers who are at risk of leaving and support proactive retention decisions.

## Key Features
### Executive Overview

Total customers

Overall churn rate

At-risk customers

High/Critical-risk customers

Average predicted churn probability

### Risk Analytics

Filter customers by risk level

Filter by contract type

Set minimum churn probability

Analyze customer risk based on tenure and monthly charges

### Customer Segmentation

New / Low-Engagement

High-Value Loyal

Long-Term Low-Spend

High-Risk / At-Risk

Segment-level customer and churn analysis

### Churn Drivers

SHAP-based model explainability

Identifies the strongest factors influencing churn predictions

Feature importance analysis

### Customer Explorer

Select customers using Customer ID

View individual churn probability

View risk level

View tenure, contract, monthly charges, and internet service

Receive retention recommendations

View priority customers

Export priority customer data as CSV

### Machine Learning
The project uses an XGBoost Classifier to predict customer churn probability.

Model information displayed in the application:

Model: XGBoost Classifier

ROC-AUC: 0.841

Intervention Threshold: 35%

Explainability: SHAP

Customers with a predicted churn probability of 35% or higher are considered part of the at-risk population.

### Customer Risk Classification
Churn Probability	Risk Classification
< 35%	Low
35% – 49%	Medium
50% – 69%	High
≥ 70%	Critical

### Technology Stack
Python
  |
Pandas
  |
Streamlit
  |
Plotly
  |
XGBoost
  |
SHAP
  |
K-Means
  |
HTML/CSS
  |
GitHub
  
### Project Files

customer-churn-project/
│
├── app.py
├── telco_churn_powerbi.csv
├── shap_feature_importance.csv
├── requirements.txt
└── README.md


### Dataset
The application uses:


telco_churn_powerbi.csv
The dataset contains customer information, churn status, churn probability, risk level, contract information, tenure, monthly charges, customer segments, and retention recommendations.

### SHAP Feature Importance
The application reads:


shap_feature_importance.csv
This file contains:

Feature

MeanAbsSHAP

These values are used to explain the relative importance of features in the churn prediction model.

### Running the Application
Install the required dependencies:

Bash

pip install -r requirements.txt
Run the Streamlit application:

Bash

streamlit run app.py
The application can also be deployed directly through GitHub + Streamlit Community Cloud, with app.py, requirements.txt, and the required CSV files stored in the same repository.

### Business Objective
The primary objective of CHURNIQ is to transform customer data into actionable retention insights by:

1.Identifying customers likely to churn.

2.Categorizing customers according to risk.

3.Understanding the factors influencing churn.

4.Identifying important customer segments.

5.Prioritizing high-risk customers.

6.Supporting targeted retention strategies.

## Author
### Mayuri Ghodke

