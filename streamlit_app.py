import streamlit as st
import random

st.title("10ゲーム")

# 数字の初期化（重複しないようにする）
if 'numbers' not in st.session_state:
    while True:
        st.session_state.numbers = random.sample(range(1, 10), 4)
        if len(set(st.session_state.numbers)) == 4:
            break

if 'siki' not in st.session_state:
    st.session_state.siki = ""

if 'right' not in st.session_state:
    st.session_state.right = 0

# 数式を作るボタン
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
operators = ["＋", "－", "×", "÷", "(", ")"]
real_ops = { "＋": "+", "－": "-", "×": "*", "÷": "/" }

for i, op in enumerate(operators):
    if st.columns(6)[i].button(op):
        st.session_state.siki += real_ops[op]

# 数字のボタン
for i, num in enumerate(st.session_state.numbers):
    if st.columns(4)[i].button(str(num)):
        st.session_state.siki += str(num)

# 削除ボタン
if st.button("削除"):
    st.session_state.siki = st.session_state.siki[:-1]

# 計算結果を表示
try:
    result = eval(st.session_state.siki) if st.session_state.siki else "?"
except:
    result = "エラー"

st.write(f"{st.session_state.siki} = {result}")

# 次の問題へ
if st.button("次の問題へ"):
    if result == 10:
        st.session_state.right += 1  # 正解ならスコア加算
    st.session_state.numbers = random.sample(range(1, 10), 4)
    st.session_state.siki = ""

# スコア表示
st.subheader(f"スコア: {st.session_state.right}")
