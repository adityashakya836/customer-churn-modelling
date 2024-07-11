import streamlit as st
st.title("Product Usage")

st.markdown('<h2>Most commonly used products or services</h2>', unsafe_allow_html=True)

p1, p2 = st.columns(2)
with p1:
    st.session_state['product_counts']
    st.write('The NumOfProducts ‘1’ is used by customer more. Means only 1 product is purchased more.')
with p2:
    st.bar_chart(st.session_state['product_counts'], x = 'NumOfProducts', y = 'count', color = '#ffaa00')

st.markdown('<h2>The usage patterns of different customer segments</h2>', unsafe_allow_html=True)

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

col1, col2 = st.columns(2)

with col1:
    d = st.session_state['pattern'][[s,'NumOfProducts']]
    d
with col2:
    st.bar_chart(d, x = s, y = 'NumOfProducts', color = '#ffaa00')

