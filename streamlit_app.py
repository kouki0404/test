import streamlit as st
import random

st.title("10ゲーム")

if 'numbers' not in st.session_state:
    st.session_state.numbers = random.choices(range(1, 10), k=4) 

if 'siki' not in st.session_state:
    st.session_state.siki = ""

if 'right' not in st.session_state:
    st.session_state.right = 0

if 'used_numbers' not in st.session_state:
    st.session_state.used_numbers = []

col1, col2, col3, col4, col5, col6 = st.columns(6)
if col1.button("＋"):
    st.session_state.siki += "+"
if col2.button("－"):
    st.session_state.siki += "-"
if col3.button("×"):
    st.session_state.siki += "*"
if col4.button("÷"):
    st.session_state.siki += "/"
if col5.button("("):
    st.session_state.siki += "("
if col6.button(")"):
    st.session_state.siki += ")"

st.write("")  

col7, col8, col9, col10 = st.columns(4)
num_cols = [col7, col8, col9, col10]

for i, num in enumerate(st.session_state.numbers):
    button_label = f"{num} ({i})"  
    if i not in st.session_state.used_numbers: 
        if num_cols[i].button(button_label):
            st.session_state.siki += str(num)
            st.session_state.used_numbers.append(i) 

if st.button("削除"):
    if st.session_state.siki:
        last_char = st.session_state.siki[-1]
        st.session_state.siki = st.session_state.siki[:-1]

        if last_char.isdigit():
            if st.session_state.used_numbers:
                st.session_state.used_numbers.pop()

try:
    result = eval(st.session_state.siki) if st.session_state.siki else "?"
except:
    result = "エラー"

st.write(f"{st.session_state.siki} = {result}")

if st.button("次の問題へ"):
    if result == 10:
        st.session_state.right += 1  
    st.session_state.numbers = random.choices(range(1, 10), k=4) 
    st.session_state.siki = ""
    st.session_state.used_numbers = []  

st.subheader(f"スコア: {st.session_state.right}")
