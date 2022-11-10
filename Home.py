import streamlit as st

with open('medicine_tablets.txt', 'r') as tablets:
    st.write(tablets.read().str.splitlines(keepends=False))