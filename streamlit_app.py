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
if st.session_state.a == st.session_state.b and st.session_state.c == st.session_state.d and st.session_state.a == st.session_state.c and st.session_state.a == 1:
    st.session_state.a = random.randint(1,9)
    st.session_state.b = random.randint(1,9)
    st.session_state.c = random.randint(1,9)
    st.session_state.d = random.randint(1,9)
col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
sisoku = ["＋","－","×","÷","（","）"]
answer = []
if 'siki' not in st.session_state:
    st.session_state.siki = ""
choice = ""
solve = 0
if col1.button(str(sisoku[0])):
    st.session_state.siki += str(sisoku[0])
    choice = str(sisoku[0])
if col2.button(str(sisoku[1])):
    st.session_state.siki += str(sisoku[1])
    choice = str(sisoku[1])
if col3.button(str(sisoku[2])):
    st.session_state.siki += str(sisoku[2])
    choice = str(sisoku[2])
if col4.button(str(sisoku[3])):
    st.session_state.siki += str(sisoku[3])
    choice = str(sisoku[3])
if col5.button(str(sisoku[4])):
    st.session_state.siki += str(sisoku[4])
    choice = str(sisoku[4])
if col6.button(str(sisoku[5])):
    st.session_state.siki += str(sisoku[5])
    choice = str(sisoku[5])
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
if col5.button(f"一文字消す"):
    st.session_state.siki = st.session_state.siki[:-1]
st.write(f"{st.session_state.siki}={solve}")
if st.button("次の問題へ"):
    st.session_state.a = random.randint(1,9)
    st.session_state.b = random.randint(1,9)
    st.session_state.c = random.randint(1,9)
    st.session_state.d = random.randint(1,9)