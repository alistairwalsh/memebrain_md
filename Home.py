import streamlit as st
import cv2
from glob import glob

cures = ['UseSalve', 'Stomatchheal', 'Bandage1', 'Painkiller', 'Bandage2', 'Antidepresant', 'Adrenalin', 'Antibiotic', 'Disinfected', 'Radioprotection']
illness = []

st.title('Illness')
for filename in glob('images/*.png'):
    name = filename.split('/')[-1].split('.')[0]
    if name not in cures:
        st.write(name)
        st.image(cv2.imread(filename),caption = name, width=100)

st.title('Cured')
for filename in glob('images/*.png'):
    name = filename.split('/')[-1].split('.')[0]
    if name in cures:
        st.write(name)
        st.image(cv2.imread(filename),caption = name, width=100)


with open('medicine_ampouls.txt', 'r') as infile:
    ampule_text = {}
    for line in infile.readlines():
        line = line.strip()
        if line.startswith(('class')):
            new_k = line.split()[1].replace('Ampoule','')
            ampule_text[new_k] = []
        elif len(line) < 1 or line.startswith(('{','}')):
            pass
        else:
            if len(line) < 1 or line.startswith(('scope','model','hiddenSelections','ITEM_DAMAGE_SYSTEM','AMPOUL_ANIM_EVENT')):
                pass
            else:
                for bad_char in ('"','#syb_','_name',';'):
                    line = line.replace(bad_char, '')
                    line = line.split(' //')[0]
                ampule_text[new_k].append(line)

for k, v in ampule_text.items():
    ampule_text[k] = {val.split('=')[0]: val.split('=')[-1] for val in v}

st.json(ampule_text)

for k, v in ampule_text:
    for kk, vv in v:
        if kk.startswith('med') and not kk.endswith('TimeSec'):
            st.write(k, kk, vv)

#st.write(ampule_text)



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
