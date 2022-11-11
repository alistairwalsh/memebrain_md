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


'UseSalve', 'Stomatchheal', 'Bandage1', 'Painkiller', 'Bandage2', 'Antidepresant', 'Adrenalin', 'Antibiotic', 'Disinfected', 'Radioprotection'
# st.write("""Hemostatic""")

# st.image(cv2.imread('images/Hemostatic.png'), caption = 'Hemostatic')

# st.write("""Hematopoiesis""")

# st.image(cv2.imread('images/Hematopoiesis.png'), caption = 'Hematopoiesis')

# st.write("""Hematoma""")

# st.image(cv2.imread('images/Hematoma.png'), caption = 'Hematoma')

# st.write("""pain""")

# st.image(cv2.imread('images/Pain.png'), caption = 'Pain')

# st.write("""Stomatchpoison""")

# st.image(cv2.imread('images/Stomatchpoison.png'), caption = 'Stomatchpoison')

# st.write("""Antibiotic""")

# st.image(cv2.imread('images/Antibiotic.png'), caption = 'Antibiotic')

# st.write("""ZVirus""")

# st.image(cv2.imread('images/ZVirus.png'), caption = 'ZVirus')

# st.write("""Concussion""")

# st.image(cv2.imread('images/Concussion.png'), caption = 'Concussion')

# st.write("""KnifeHit""")

# st.image(cv2.imread('images/KnifeHit.png'), caption = 'KnifeHit')

# st.write("""Bullethit""")

# st.image(cv2.imread('images/Bullethit.png'), caption = 'Bullethit')






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
    st.write(k, {val.split('=')[0]: val.split('=')[-1] for val in v})
for name in glob('images/*'):
    img = cv2.imread(name)
    st.image(img, name)
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
