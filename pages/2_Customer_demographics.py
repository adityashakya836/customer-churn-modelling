import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Customer Demographics")

# Custom HTML and CSS for styling
st.markdown(
    """
    <style>
    .custom-header {
        font-size: 30px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Display custom header
def distribution_by_customer():
    st.markdown('<div class="custom-header">Distribution of customers across different age groups:</div>', unsafe_allow_html=True)

    # st.write('Distribution of customers across different age groups:')

    col1, col2 = st.columns(2)

    with col1:
        st.write(st.session_state['Age-group'])

    with col2:
        fig = px.bar(
        st.session_state['Age-group'],
        x='Age-group',
        y='count',
        labels={'Age-Group': 'Age-Group', 'count': 'Count'},
        title='Age Group Distribution',
        color_discrete_sequence=['#ffaa00']
        )

        # Update layout for custom width and height
        fig.update_layout(
            width=800,  # Set the desired width
            height=400,  # Set the desired height
            xaxis_title='Age-Group',
            yaxis_title='Count'
        )

        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)
    st.markdown(
        """
        <ul>
            <li>The customer between the age-group 31-40 are more which is 4451</li>
            <li>No customers between the age 0-10</li>
            <li>Very less customers are in between 91-100</li>
            <li>The customers between the age 21-30 are 1879</li>
        </ul>
        """,
        unsafe_allow_html=True
    )


# Analyze the gender distribution of customers
def gender_distribution():
    st.markdown('<div class="custom-header">Gender distribution of Customers</div>', unsafe_allow_html=True)


    col3, col4 = st.columns(2)
    with col3:
        st.write(st.session_state['Gender'])

    with col4:
        fig = px.bar(
        st.session_state['Gender'],
        x='Gender',
        y='count',
        labels={'Gender': 'Gender', 'count': 'Count'},
        title='Gender Distribution',
        color_discrete_sequence=['#ffaa00']
        )

        # Update layout for custom width and height
        fig.update_layout(
            width=600,  # Set the desired width
            height=400,  # Set the desired height
            xaxis_title='Gender',
            yaxis_title='Count'
        )

        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)

    st.markdown(
        """
        <h5> Male Customers are more than female customers</h5>
        """,
        unsafe_allow_html=True
    )

s = st.selectbox(
    'Select Your Question',
    [
        None,
        'Distribution By Customer',
        'Distribution By Gender'
    ]
)

if s=='Distribution By Customer':
    distribution_by_customer()

if s == 'Distribution By Gender':
    gender_distribution()
