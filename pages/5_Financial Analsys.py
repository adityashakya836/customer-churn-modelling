import streamlit as st
import matplotlib.pyplot as plt
st.title("Financial Analysis")

st.markdown("<h4>The average account balance of customers : 76485.89</h4>", unsafe_allow_html=True)
st.markdown("<h2>Comparison of the financial characteristics of churned vs. non-churned customers.</h2>", unsafe_allow_html=True)
st.markdown('<h3>Churned Statistics<h3>', unsafe_allow_html=True)
st.table(st.session_state['churned_stats']) 
st.markdown('<h3>Non Churned Statistics<h3>', unsafe_allow_html=True)
st.table(st.session_state['non_churned_stats']) 


def plot_comparison():
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 6))

    # Plot for CreditScore
    st.session_state['churned_stats'] .plot(x='index', y='CreditScore', kind='bar', ax=axes[0], color='blue', alpha=0.7, label='Churned')
    st.session_state['non_churned_stats'].plot(x='index', y='CreditScore', kind='bar', ax=axes[0], color='orange', alpha=0.7, label='Non-Churned', width=0.4, position=1)
    axes[0].set_title('CreditScore Comparison')
    axes[0].set_ylabel('Values')

    # Plot for Balance
    st.session_state['churned_stats'] .plot(x='index', y='Balance', kind='bar', ax=axes[1], color='blue', alpha=0.7, label='Churned')
    st.session_state['non_churned_stats'].plot(x='index', y='Balance', kind='bar', ax=axes[1], color='orange', alpha=0.7, label='Non-Churned', width=0.4, position=1)
    axes[1].set_title('Balance Comparison')

    # Plot for EstimatedSalary
    st.session_state['churned_stats'] .plot(x='index', y='EstimatedSalary', kind='bar', ax=axes[2], color='blue', alpha=0.7, label='Churned')
    st.session_state['non_churned_stats'].plot(x='index', y='EstimatedSalary', kind='bar', ax=axes[2], color='orange', alpha=0.7, label='Non-Churned', width=0.4, position=1)
    axes[2].set_title('EstimatedSalary Comparison')

    # Set a common legend
    plt.legend(['Churned', 'Non-Churned'], loc='upper center', bbox_to_anchor=(-0.1, 1.15), ncol=2)
    plt.tight_layout()
    return fig

# Streamlit app
st.title('Comparison of Two Datasets')

st.write("Comparison two datasets across three variables: CreditScore, Balance, and EstimatedSalary.")

st.pyplot(plot_comparison())

