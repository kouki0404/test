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
answer = 0
keisan = []
if 'choice_sisoku' not in st.session_state:
    st.session_state.choice_sisoku = ""
if 'siki' not in st.session_state:
    st.session_state.siki = ""
choice = ""
if 'right' not in st.session_state:
    st.session_state.right = 0
solve = 0
count = 0
if 'number_a' not in st.session_state:
    st.session_state.number_a = True
if 'number_b' not in st.session_state:
    st.session_state.number_b = True
number_c = 0
number_d = 0
if col1.button(str(sisoku[0])):
    st.session_state.siki += "+"
    count += 1
if col2.button(str(sisoku[1])):
    st.session_state.siki += "-"
    count += 1
if col3.button(str(sisoku[2])):
    st.session_state.siki += "*"
    count += 1
if col4.button(str(sisoku[3])):
    st.session_state.siki += "/"
    count += 1
if col5.button(str(sisoku[4])):
    st.session_state.siki += "("
    count += 1
if col6.button(str(sisoku[5])):
    st.session_state.siki += ")"
    count += 1
if col1.button(f"{str(st.session_state.a)}"):
    if st.session_state.number_a:
        st.session_state.siki += str(f"{st.session_state.a}")
        st.session_state.number_a = False
    else:
        st.error(f"同じ数字を使うことはできません")

col2.button(f"{str(st.session_state.b)} ")
col3.button(f"{str(st.session_state.c)}  ")
col4.button(f"{str(st.session_state.d)}   ")
if col5.button(f"削除"):
    if st.session_state.siki != "":
        last = keisan[-1]
        if last == st.session_state.a:
            st.session_state.number_a = True
            
        st.session_state.siki = st.session_state.siki[:-1]
        count -= 1
if answer != 0:
    if keisan[count-1] == "＋":
        st.session_state.choice_sisoku = "＋"
    elif keisan[count-1] == "－":
        st.session_state.choice_sisoku = "－"
else:
    answer = 0
st.write(f"{st.session_state.siki}={eval(st.session_state.siki)}")
if st.button("次の問題へ"):
    if count >= 7 and eval(st.session_state.siki) == 10:
        st.session_state.a = random.randint(1,9)
        st.session_state.b = random.randint(1,9)
        st.session_state.c = random.randint(1,9)
        st.session_state.d = random.randint(1,9)
        st.session_state.siki = ""
        answer = 0
        solve = 0
        st.session_state.right += 1
    else:
        st.session_state.a = random.randint(1,9)
        st.session_state.b = random.randint(1,9)
        st.session_state.c = random.randint(1,9)
        st.session_state.d = random.randint(1,9)
        st.session_state.number_a = True
        st.session_state.siki = ""
        answer = 0
        solve = 0

st.subheader(f"スコア:{st.session_state.right}")