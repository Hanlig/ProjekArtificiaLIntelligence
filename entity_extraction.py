# entity_extraction.py

import re
from menu_kue import menu_kue

def ekstrak_entitas(user_input):
    user_input = user_input.lower()
    jumlah = re.findall(r'\b\d+\b', user_input)

    kue_dipesan = []
    for kue in menu_kue:
        if kue in user_input:
            kue_dipesan.append(kue)

    return {
        "kue": kue_dipesan,
        "jumlah": jumlah[:len(kue_dipesan)]
    }
