import streamlit as st

with open('medicine_ampouls.txt', 'r') as infile:
    ampouls = infile.read()
    for line in ampouls:
        st.write(line)

# with open('medicine_injectors.txt', 'r') as infile:
#     injectors = infile.read()
#     st.write(injectors)

# with open('medicine_salves.txt', 'r') as infile:
#     salves = infile.read()
#     st.write(salves)

# with open('medicine_tablets.txt', 'r') as infile:
#     tablets = infile.read()
#     st.write(tablets)