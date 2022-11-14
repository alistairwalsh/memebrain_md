import pandas as pd
import streamlit as st

df = pd.read_csv('dat/stringtable.csv')

st.dataframe(df[['Language','original','englis',]])