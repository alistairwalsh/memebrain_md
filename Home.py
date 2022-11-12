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


lst = range(1,5)
st.write(list(itertools.chain.from_iterable(itertools.repeat(x, 3) for x in lst)))



st.title('Illness')
illness_images = []
illness_names = []
for filename in glob('images/*.png'):
    name = filename.split('/')[-1].split('.')[0]
    if name not in cures:
        illness_images.append(filename)
        illness_names.append(name)

st.write(len(illness_images)//4)


st.write(illness_names)
st.write(illness_images)

# img = image_select(
#     label="Select what ails you",
#     images=[cv2.imread(filename) for filename in illness_images],
#     captions=illness_names
# )
# st.write(img)
# st.image(img)
