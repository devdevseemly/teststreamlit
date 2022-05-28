import streamlit as st

st.info('Click Assess button below')

pregnant = st.sidebar.slider('pregnant', 0, 10, 5)
st.write('input pregnant', pregnant)