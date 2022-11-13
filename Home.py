import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob
import itertools
import re

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
    'Radioprotection',
    "Hemostatic"
    ]


st.title('Illness')
illness_images = []
illness_names = []
for filename in glob('images/*.png'):
    name = filename.split('/')[-1].split('.')[0]
    if name not in cures:
        illness_images.append(filename)
        illness_names.append(name)

st.write(illness_names)

dict_ill_2_cure = {
"Influenza":"medAntibioticLevel",
"RadiationSickness":"medRadioprotectionLevel",
"Pain":"medPainkillerLevel",
"Hematopoiesis":"medBloodHematopoiesis",
"ZVirus":"medRemoveZVirus",
"Sepsis":"medRemoveSepsis",
"Hematoma":"medHematomaHeal",
"Concussion":"medConcussionHeal",
"Stomatchpoison":"medStomatchhealLevel",
"VisceraDamage":'',
"Bullethit":'',
"KnifeHit":'',
"Overdosed":''
}


# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
 
# How many elements each
# list should have
n = 5
 
x = list(divide_chunks([(i,ii) for i,ii in zip(illness_images,illness_names)], n))

cols = st.columns(5)
for i in x:
    for c, ii in zip(cols,i):
        c.image(cv2.imread(ii[0]), caption = ii[-1],use_column_width = 'always')

option = st.selectbox(label = 'Select your illness', options = illness_names)

st.write('you should do',dict_ill_2_cure[option])

@st.experimental_singleton
def get_text(filename):
    with open(filename, 'r') as infile:
        in_text = {}
        text = infile.read()

    in_text = {k:v.split(';') for k, v in [l.split('{', 1) for l in text.split('\n\n') if len(l) > 0 ]} # split on newline, split on '{' then split on ';'

    clean_text = {}

    for k, v in in_text.items():
        clean_text[k.split(' ')[1]] = {kkk.replace('"','').strip():vvv.replace('"','').strip() for kkk,vvv in [vv.split('=') for vv in v if '=' in vv] if kkk.strip() not in ("model","hiddenSelections[]","scope","varQuantityInit","varQuantityMax")}

    for k, v in clean_text.items():
        if "hiddenSelectionsTextures[]" in clean_text[k].keys():
            clean_text[k]['colour'] = clean_text[k]["hiddenSelectionsTextures[]"].split('\\')[-1].replace('.paa','').replace('}','').strip()
            del clean_text[k]["hiddenSelectionsTextures[]"]

    return clean_text

clean_injectors_text = get_text('medicine_injectors.txt')

clean_ampules_text = get_text('medicine_ampouls.txt')

clean_salve_text = get_text('medicine_salves.txt')

clean_tablet_text = get_text('medicine_tablets.txt')

cures = {}



def get_relevant(text_dict):  

    r_list = []

    for med_type_k in text_dict.keys():
        treatments = [k for k in text_dict[med_type_k].keys() if k == dict_ill_2_cure[option]]
        if treatments:
            for treatment in treatments:
                r = re.findall('([A-Z][a-z]+)', med_type_k)
                r_list.append(r)
        return r_list 

# r[1], text_dict[med_type_k]['colour'].split('_')[-2], text_dict[med_type_k][dict_ill_2_cure[option]]

# just returns one - need all

injectors = get_relevant(clean_injectors_text)

ampules = get_relevant(clean_ampules_text) 

salves = get_relevant(clean_salve_text) 

tablets = get_relevant(clean_tablet_text) 

if injectors:
    st.header('Injectors')
    st.write(injectors)
if ampules:
    st.header('Ampules')
    st.write(ampules)
if salves:
    st.header('Salves')
    st.write(salves)
if tablets:
    st.header('Tablets')
    st.write(tablets)





# st.write(illness_names)
# st.write(illness_images)

# img = image_select(
#     label="Select what ails you",
#     images=[cv2.imread(filename) for filename in illness_images],
#     captions=illness_names
# )
# st.write(img)
# st.image(img)

# Hematopoiesis (pronounced “heh-ma-tuh-poy-EE-sus”) is blood cell production
# Hemostasis refers to normal blood clotting in response to an injury
# HemologicShock (Hypovolemic shock) is an emergency condition in which severe blood or other fluid loss makes the heart unable to pump enough blood to the body.
# Hematoma is a bad bruise. It happens when an injury causes blood to collect and pool under the skin.
# Visceral injuries are injuries to all internal organs

# cures = [
#     'UseSalve', 
#     'Stomatchheal', 
#     'Bandage1', 
#     'Painkiller', 
#     'Bandage2', 
#     'Antidepresant', 
#     'Adrenalin', 
#     'Antibiotic', 
#     'Disinfected', 
#     'Radioprotection',
#     "Hemostatic"
#     ]

# illness = [
#   "Influenza",
#   "RadiationSickness",
#   "Pain",
#   "Hematopoiesis",
#   "ZVirus",
#   "Sepsis",
#   "Hematoma",
#   "Concussion",
#   "Stomatchpoison",
#   "VisceraDamage",
#   "Bullethit",
#   "KnifeHit",
#   "Overdosed",
#   ]

#medAntibioticLevel Influenza
#medRemoveSepsis Sepsis
#medRemoveZVirus ZVirus
#medConcussionHeal Concussion
