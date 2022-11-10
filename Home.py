import streamlit as st

with open('medicine_tablets.hpp') as tablets:
    st.write(tablets.read())