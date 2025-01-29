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
col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
sisoku = ["+","-","×","÷","(",")"]
answer = []
if st.session_state.a == st.session_state.b:
    col1.button(f"{str(st.session_state.a)}")
    col2.button(f"{str(st.session_state.b)} ")
    if st.session_state.a == st.session_state.c:
        col3.button(f"{str(st.session_state.c)}  ")
        if st.session_state.a == st.session_state.d:
            col4.button(f"{str(st.session_state.d)}   ")
        else:
            col4.button(f"{str(st.session_state.d)}")
    else:
        if st.session_state.c == st.session_state.d:
            col3.button(f"{str(st.session_state.c)} ")
            col4.button(f"{str(st.session_state.d)}")
        else:
            col3.button(f"{str(st.session_state.c)}")
            col4.button(f"{str(st.session_state.d)}")
elif st.session_state.a == st.session_state.c :
    col1.button(f"{str(st.session_state.a)}")
    col2.button(f"{str(st.session_state.b)} ")
    col3.button(f"{str(st.session_state.c)} ")
    col4.button(f"{str(st.session_state.d)}")
elif st.session_state.a == st.session_state.d:
    col1.button(f"{str(st.session_state.a)}")
    col2.button(f"{str(st.session_state.b)}")
    col3.button(f"{str(st.session_state.c)} ")
    col4.button(f"{str(st.session_state.d)} ")
elif st.session_state.b == st.session_state.c and st.session_state.b != st.session_state.d:
    col1.button(f"{str(st.session_state.a)}")
    col2.button(f"{str(st.session_state.b)}")
    col3.button(f"{str(st.session_state.c)} ")
    col4.button(f"{str(st.session_state.d)}")
elif st.session_state.b == st.session_state.d:
    col1.button(f"{str(st.session_state.a)}")
    col2.button(f"{str(st.session_state.b)} ")
    col3.button(f"{str(st.session_state.c)}")
    col4.button(f"{str(st.session_state.d)}")
elif st.session_state.c == st.session_state.d:
    col1.button(f"{str(st.session_state.a)}")
    col2.button(f"{str(st.session_state.b)}")
    col3.button(f"{str(st.session_state.c)} ")
    col4.button(f"{str(st.session_state.d)}")
else:
    col1.button(f"{str(st.session_state.a)}")
    col2.button(f"{str(st.session_state.b)}")
    col3.button(f"{str(st.session_state.c)}")
    col4.button(f"{str(st.session_state.d)}")
col1.button(str(sisoku[0]))