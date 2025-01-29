import streamlit as st
import random
st.title("10ゲーム")
if 'a' not in  st.session_state:
    st.session_state.a = random.randint(1,9)
if 'b' not in st.session_state:
    st.session_state.b = random.randint(1,9)
if 'c' not in st.session_state:
    st.session_state.c = random.randint(1,9)
if 'd' not in st.session_state:
    st.session_state.d = random.randint(1,9)
col1,col2,col3,col4,col5,col6 = st.columns(6)
sisoku = ["+","-","×","÷","(",")"]
answer = []
col1.button(str(st.session_state.a))
col2.button(str(st.session_state.b))
col3.button(str(st.session_state.c))
col4.button(str(st.session_state.d))
col1.button(str(sisoku[0]))