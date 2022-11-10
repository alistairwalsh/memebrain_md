import streamlit as st

with open('medicine_ampouls.txt', 'r') as infile:
    ampouls = infile.read().splitlines(keepends=False)
    st.write(ampouls)

with open('medicine_injectors.txt', 'r') as infile:
    injectors = infile.read().splitlines(keepends=False)
    st.write(injectors)

with open('medicine_salves.txt', 'r') as infile:
    salves = infile.read().splitlines(keepends=False)
    st.write(salves)

with open('medicine_tablets.txt', 'r') as infile:
    tablets = infile.read().splitlines(keepends=False)
    st.write(tablets)