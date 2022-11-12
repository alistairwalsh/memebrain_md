import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob


@st.experimental_singleton
def get_text(filename):
    with open(filename, 'r') as infile:
        injector_text = {}
        text = infile.read()

    injector_text = {k:v.split(';')[1:-4] for k, v in [l.split('{', 1) for l in text.split('\n\n')]}

    clean_injector_text = {}

    for k, v in injector_text.items():
        clean_injector_text[k.split(' ')[1]] = {kkk.replace('"','').strip():vvv.replace('"','').strip() for kkk,vvv in [vv.split('=') for vv in v] if kkk.strip() not in ("model","hiddenSelections[]",)}

    for k, v in clean_injector_text.items():
        clean_injector_text[k]['colour'] = clean_injector_text[k]["hiddenSelectionsTextures[]"].split('\\')[-1].replace('.paa','').replace('}','').strip()
        del clean_injector_text[k]["hiddenSelectionsTextures[]"]

    return clean_injector_text

clean_injector_text = get_text('medicine_injectors.txt')
st.json(clean_injector_text)

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