import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob


@st.experimental_singleton
def get_text(filename):
    with open(filename, 'r') as infile:
        injector_text = {}
        text = infile.read()

    in_text = {k:v.split(';')[1:-4] for k, v in [l.split('{', 1) for l in text.split('\n\n')]}

    clean_text = {}

    for k, v in in_text.items():
        clean_text[k.split(' ')[1]] = {kkk.replace('"','').strip():vvv.replace('"','').strip() for kkk,vvv in [vv.split('=') for vv in v] if kkk.strip() not in ("model","hiddenSelections[]",)}

    for k, v in clean_text.items():
        clean_text[k]['colour'] = clean_text[k]["hiddenSelectionsTextures[]"].split('\\')[-1].replace('.paa','').replace('}','').strip()
        del clean_iclean_textnjector_text[k]["hiddenSelectionsTextures[]"]

    return clean_text

clean_tablet_text = get_text('medicine_tablets.txt')
st.json(clean_injector_text)