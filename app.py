#!/usr/bin/env python3
from typing import List, Tuple

import codefast as cf
import streamlit as st

cmd = st.text_input('exec', 'ls')
resp = cf.shell(cmd)
st.text_area('resp', resp)

