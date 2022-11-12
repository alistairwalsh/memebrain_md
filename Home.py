import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob
import itertools

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
    'Radioprotection',
    "Hemostatic"
    ]

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

cols = st.columns(4)

 
# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
 
# How many elements each
# list should have
n = 4
 
x = list(divide_chunks([(i,ii) for i,ii in zip(illness_images,illness_names)], n))


for i in x:
    for ii in i:
        st.write(ii)

for i,n in zip(illness_images, illness_names):
    st.image(cv2.imread(i), caption = n)

for k in st.session_state.keys():
    if st.session_state[k]:
        st.write(k)

option = st.selectbox(label = 'Select your illness', options = illness_names)

st.write('you have', option)
# st.write(illness_names)
# st.write(illness_images)

# img = image_select(
#     label="Select what ails you",
#     images=[cv2.imread(filename) for filename in illness_images],
#     captions=illness_names
# )
# st.write(img)
# st.image(img)
