import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob


with open('medicine_ampouls.txt', 'r') as infile:
        in_text = {}
        text = infile.read()

st.write(in_text)

# @st.experimental_singleton
# def get_text(filename):
#     with open(filename, 'r') as infile:
#         in_text = {}
#         text = infile.read()

#     in_text = {k:v.split(';') for k, v in [l.split('{', 1) for l in text.split('\n\n')]} # split on newline, split on '{' then split on ';'

#     clean_text = {}

#     for k, v in in_text.items():
#         clean_text[k.split(' ')[1]] = {kkk.replace('"','').strip():vvv.replace('"','').strip() for kkk,vvv in [vv.split('=') for vv in v if '=' in vv] if kkk.strip() not in ("model","hiddenSelections[]","scope","varQuantityInit","varQuantityMax")}

#     for k, v in clean_text.items():
#         if "hiddenSelectionsTextures[]" in clean_text[k].keys():
#             clean_text[k]['colour'] = clean_text[k]["hiddenSelectionsTextures[]"].split('\\')[-1].replace('.paa','').replace('}','').strip()
#             del clean_text[k]["hiddenSelectionsTextures[]"]

#     return clean_text

# clean_ampules_text = get_text('medicine_ampouls.txt')
# st.json(clean_ampules_text)