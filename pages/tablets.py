import streamlit as st

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
clean_tablet_text = get_text('medicine_tablets.txt')
st.json(clean_tablet_text)