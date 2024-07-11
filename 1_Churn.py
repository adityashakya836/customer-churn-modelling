import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Multipage App",
    page_icon="🙂"
)
st.title('Churn Modelling')

# reading the excel file
df = pd.read_excel("P3- Churn-Modelling Data.xlsx", engine = 'openpyxl')
st.session_state['df'] = df
st.write(st.session_state['df'])

st.table(df.describe())

st.write(df.info())

st.write(f"There are {df.shape[0]} rows")
st.write(f"There are {df.shape[1]} column")
# for the distribution of customers across different age groups let's make the age groups
bins = [0,10,20,30,40,50,60,70,80,90,100]
labels = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100']
df['Age-group'] = pd.cut(df['Age'], bins = bins, labels = labels)

# counting the value of each age groups
age_groups = df['Age-group'].value_counts().reset_index()
st.session_state['Age-group'] = age_groups

# counting the value of each gender
gender = df['Gender'].value_counts().reset_index()
st.session_state['Gender'] = gender

# Churn Analysis
#percentage of customers have churned
churn_count = df['churned'].value_counts().reset_index()
st.session_state['churn_count'] = churn_count

total_customers = df.shape[0]
st.session_state['total_customers'] = total_customers

churned_customers = df['churned'].sum()
st.session_state['churned_customers'] = churned_customers

percentage = (churned_customers/total_customers) * 100
st.session_state['percentage'] = percentage

#What are the main reasons for customer churn?
churned_stats = df[df['churned'] == 1].describe()
non_churned_stats = df[df['churned'] == 0].describe()
st.session_state['churned_stats'] = churned_stats
st.session_state['non_churned_stats'] = non_churned_stats

# Identify any patterns or trends among customers who have churned.
# Count the number of products used by customers
product_usage_counts = df['NumOfProducts'].value_counts().reset_index()

# Count the number of customers with credit cards
credit_card_usage_counts = df['HasCrCard'].value_counts().reset_index()



st.session_state['product_usage_counts'] = product_usage_counts
st.session_state['credit_card_usage_counts'] = credit_card_usage_counts


product_counts = df['NumOfProducts'].value_counts().reset_index()
st.session_state['product_counts'] = product_counts

churned_stats = df[df['churned'] == 1][['CreditScore', 'Balance', 'EstimatedSalary']].describe()
churned_stats = churned_stats.reset_index()
st.session_state['churned_stats'] = churned_stats

non_churned_stats = df[df['churned'] == 0][['CreditScore', 'Balance', 'EstimatedSalary']].describe()
non_churned_stats = non_churned_stats.reset_index()
st.session_state['non_churned_stats'] = non_churned_stats

# Data for the DataFrame
feature_data = {
    "Feature": ["Age", "EstimatedSalary", "CreditScore", "Balance", "NumOfProducts", "Tenure", "IsActiveMember", "HasCrCard"],
    "Importance": [0.248300, 0.167262, 0.161797, 0.148759, 0.131229, 0.083798, 0.042137, 0.016718]
}

# Creating the DataFrame
feature_data = pd.DataFrame(feature_data)
st.session_state['feature_data'] = feature_data
st.write('Factors which are most significant predictors of customer churn')
st.table(st.session_state['feature_data'])

models = {
    'Models': ['Random Forest', 'Logistic Regression', 'MLP'],
    'Accuracy%' : [80,64,58],
    'Precision%' : [61, 30, 55.9],
    'Recall%': [49.5, 30.1, 25.1]
}
model_data = pd.DataFrame(models)
st.table(model_data)