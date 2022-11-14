import pandas as pd
import streamlit as st

df = pd.read_csv('data/stringtable.csv')

st.dataframe(df[['Language','original']])