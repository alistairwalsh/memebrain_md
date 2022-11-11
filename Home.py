import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob

# Hematopoiesis (pronounced “heh-ma-tuh-poy-EE-sus”) is blood cell production
# Hemostasis refers to normal blood clotting in response to an injury
# HemologicShock (Hypovolemic shock) is an emergency condition in which severe blood or other fluid loss makes the heart unable to pump enough blood to the body.
# Hematoma is a bad bruise. It happens when an injury causes blood to collect and pool under the skin.
# Visceral injuries are injuries to all internal organs

cures = [
    'UseSalve', 
    'Stomatchheal', 
    'Bandage1', 
    'Painkiller', 
    'Bandage2', 
    'Antidepresant', 
    'Adrenalin', 
    'Antibiotic', 
    'Disinfected', 
    'Radioprotection']

illness = [
  "Influenza",
  "RadiationSickness",
  "Pain",
  "Hematopoiesis",
  "ZVirus",
  "Sepsis",
  "Hematoma",
  "Concussion",
  "Stomatchpoison",
  "VisceraDamage",
  "Bullethit",
  "KnifeHit",
  "Overdosed",
  "Hemostatic"
]

#medAntibioticLevel Influenza
#medRemoveSepsis Sepsis
#medRemoveZVirus ZVirus
#medConcussionHeal Concussion

st.title('Illness')
illness_images = []
illness_names = []
for filename in glob('images/*.png'):
    name = filename.split('/')[-1].split('.')[0]
    if name not in cures:
        illness_images.append(filename)
        illness_names.append(name)
        
st.write(illness_names)

img = image_select(
    label="Select what ails you",
    images=[cv2.imread(filename) for filename in illness_images],
    captions=illness_names
)

st.image(img)

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
            if len(line) < 1 or line.startswith(('scope','model','ITEM_DAMAGE_SYSTEM','AMPOUL_ANIM_EVENT')):
                pass
            else:
                for bad_char in ('"','#syb_','_name',';'):
                    line = line.replace(bad_char, '')
                    line = line.split(' //')[0]
                ampule_text[new_k].append(line)

for k, v in ampule_text.items():
    ampule_text[k] = {val.split('=')[0]: val.split('=')[-1] for val in v}

st.json(ampule_text)

for k, v in ampule_text.items():
    st.header(k)
    for kk, vv in v.items():
        if kk.startswith('med') and not kk.endswith('TimeSec') and not kk.startswith('overdosed') and not kk.endswith('Strength'):
            kk = kk.replace('med','').replace('Level','')
            st.write( f"type: {kk}")
            st.write(f"strength: {vv}")

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
