import streamlit as st

with open('medicine_ampouls.txt', 'r') as infile:
    medicine_text = ''
    for line in infile.readlines():
        if line.strip().startswith(('class','scope','model','hiddenSelections','ITEM_DAMAGE_SYSTEM','{','}','AMPOUL_ANIM_EVENT')):
            pass
        else:
            medicine_text = medicine_text.split(' //')[0]
            medicine_text += line.strip() + '\n'

st.write(medicine_text.split('\n'))

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