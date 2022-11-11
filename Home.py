import streamlit as st

with open('medicine_ampouls.txt', 'r') as infile:
    ampule_text = {}
    for line in infile.readlines():
        if line.strip().startswith(('class')):
            new_k = line.split()[1].replace('Ampoule','').strip()
            ampule_text[new_k] = []
        elif len(line) < 1 or line.startswith(('{','}')):
            pass
        else:
            ampule_text[new_k].append(line.strip())

st.write(ampule_text)

#for line in medicine_text:


# with open('medicine_injectors.txt', 'r') as infile:
#     injectors = infile.read()
#     st.write(injectors)

# with open('medicine_salves.txt', 'r') as infile:
#     salves = infile.read()
#     st.write(salves)

# with open('medicine_tablets.txt', 'r') as infile:
#     tablets = infile.read()
#     st.write(tablets)