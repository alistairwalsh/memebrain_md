import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob


@st.experimental_singleton
def get_text(filename):
    with open(filename, 'r') as infile:
        in_text = {}
        text = infile.read()

    in_text = {k:v.split(';') for k, v in [l.split('{', 1) for l in text.split('\n\n')]} # split on newline, split on '{' then split on ';'

    clean_text = {}

    for k, v in in_text.items():
        clean_text[k.split(' ')[1]] = {kkk.replace('"','').strip():vvv.replace('"','').strip() for kkk,vvv in [vv.split('=') for vv in v if '=' in vv] if kkk.strip() not in ("model","hiddenSelections[]","scope","varQuantityInit","varQuantityMax")}

    for k, v in clean_text.items():
        if "hiddenSelectionsTextures[]" in clean_text[k].keys():
            clean_text[k]['colour'] = clean_text[k]["hiddenSelectionsTextures[]"].split('\\')[-1].replace('.paa','').replace('}','').strip()
            del clean_text[k]["hiddenSelectionsTextures[]"]

    return clean_text

clean_injectors_text = get_text('medicine_injectors.txt')
st.json(clean_salve_text)
#st.write(injector_text)

    # for line in infile.readlines():
    #     line = line.strip()
    #     if line.startswith(('class')):
    #         new_k = line.split()[1].replace('Ampoule','')
    #         injector_text[new_k] = []
    #     elif len(line) < 1 or line.startswith(('{','}')):
    #         pass
    #     else:
    #         if len(line) < 1 or line.startswith(('scope','model','ITEM_DAMAGE_SYSTEM','AMPOUL_ANIM_EVENT')):
    #             pass
    #         else:
    #             for bad_char in ('"','#syb_','_name',';'):
    #                 line = line.replace(bad_char, '')
    #                 line = line.split(' //')[0]
    #             injector_text[new_k].append(line)