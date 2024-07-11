import streamlit as st
import plotly.express as px
st.title("Churn Analysis")
def percentage_customer():
    st.markdown(
        """
        <h1>Percentage of customers have churned:</h1>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state['churn_count'])
        st.bar_chart(st.session_state['churn_count'],x = 'churned', y = 'count', color='#ffaa00')

        

    with col2:
        st.write(f"Total number of customers : {st.session_state['total_customers']}")
        st.write(f"Churned Customers : {st.session_state['churned_customers']}")
        st.write(f"Percentage of customers have churned : {format(st.session_state['percentage'], '.2f')}%")
# What are the main reasons for customer churn?
def main_reason_for_churn():

    st.markdown(
        '''
        - 31-40 age-group has the highest churn rate, possibly due to career transitions, family growth.
        - Germany has the highest churn rate despite high balances and salaries, the high churn rate due to dissatisfaction with services or better competitor offers.
        - Churn rate for female customers is high, this can be due to unmet expectations or lack of targeted services. 
        - High product usage may lead to churn if needs are not met.
        - In the age-group, financial flexibility may lead to switching banks for better terms or rewards.
        - Age 91-100 are less likely to churn due to established trust and satisfaction.
        - Higher product usage, possibly leading to higher susceptibility to churn if better alternatives are found.
        '''
    )

#Identify any patterns or trends among customers who have churned.
def pattern():
    st.markdown(
        "<h2>Patterns or trends among customers who have churned.</h2>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    #Product Usage Counts
    with col1:
        st.markdown('<h6> Product Usage Counts</h6>', unsafe_allow_html = True)
        st.session_state['product_usage_counts']

        st.markdown(
            """
            <ul>
                <li> 7055 customers have own credit card.</li>
                <li> 2946 customers have not own credit card.</li>
            </ul>
            """,
            unsafe_allow_html=True
        )

    # Credit Card usage counts
    with col2:
        st.markdown('<h6> Credit card Usage Counts</h6>', unsafe_allow_html = True)
        st.session_state['credit_card_usage_counts']

        fig = px.bar(
        st.session_state['credit_card_usage_counts'],
        x='HasCrCard',
        y='count',
        labels={'HasCrCard': 'HascrCard', 'count': 'Count'},
        title='Credit card usage counts',
        color_discrete_sequence=['#ffaa00']
        )

        # Update layout for custom width and height
        fig.update_layout(
            width=800,  # Set the desired width
            height=400,  # Set the desired height
            xaxis_title='HasCrCard',
            yaxis_title='Count'
        )

        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)

    # How would you like to find the pattern

    s = st.selectbox(
        'How would you like to be Find Pattern?',
        ['Age-group', 'Geography', 'Gender']
    )
    st.write(s)

    st.session_state["pattern"] = st.session_state['df'].groupby(s).agg({
        'NumOfProducts': 'sum',
        'HasCrCard': 'sum',
        'Balance': 'mean',
        'EstimatedSalary': 'mean',
        'churned': 'sum'
    }).reset_index()

    st.session_state['pattern']

    num_product_column, churned_col, hascrcard_col = st.columns(3)

    with num_product_column:
        st.write(f'Number of Products Used by {s}')
        fig = px.bar(
        st.session_state['pattern'],
        x=s,
        y='NumOfProducts',
        labels={s: s, 'NumOfProducts': 'NumOfProducts'},
        color_discrete_sequence=['#ffaa00']
        )

        # Update layout for custom width and height
        fig.update_layout(
            width=800,  # Set the desired width
            height=400,  # Set the desired height
            xaxis_title=s,
            yaxis_title='NumOfProducts'
        )

        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)

    with churned_col:
        st.write(f'Number of Customer Churned by {s}')
        fig = px.bar(
        st.session_state['pattern'],
        x=s,
        y='churned',
        labels={s: s, 'churned': 'churned'},
        color_discrete_sequence=['#ffaa00']
        )

        # Update layout for custom width and height
        fig.update_layout(
            width=800,  # Set the desired width
            height=400,  # Set the desired height
            xaxis_title=s,
            yaxis_title='Churned'
        )

        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)

    with hascrcard_col:
        st.write(f'Number of Customer Churned by {s}')
        fig = px.bar(
        st.session_state['pattern'],
        x=s,
        y='HasCrCard',
        labels={s: s, 'HasCrCard': 'HasCrCard'},
        color_discrete_sequence=['#ffaa00']
        )

        # Update layout for custom width and height
        fig.update_layout(
            width=800,  # Set the desired width
            height=400,  # Set the desired height
            xaxis_title=s,
            yaxis_title='HasCrCard'
        )

        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)

s = st.selectbox(
    'Select Your Question',
    [
        None,
        'Percentage of customers have churned',
        "What are the main reasons for customer churn?",
        'Identify any patterns or trends among customers who have churned.'
    ]
)

if s=='Percentage of customers have churned':
    percentage_customer()

if s == 'What are the main reasons for customer churn?':
    main_reason_for_churn()

if s == "Identify any patterns or trends among customers who have churned.":
    pattern()