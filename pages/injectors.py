import streamlit as st
from streamlit_image_select import image_select
import cv2
from glob import glob

with open('medicine_injectors.txt', 'r') as infile:
    injector_text = {}
    text = infile.read()

st.write({k:v.split(';')[1:-4] for k, v in [l.split('{', 1) for l in text.split('\n\n')]})

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