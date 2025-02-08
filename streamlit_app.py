import streamlit as st
import random

st.title("10ゲーム")

# 数字の初期化（重複OK）
if 'numbers' not in st.session_state:
    st.session_state.numbers = random.choices(range(1, 10), k=4)

if 'siki' not in st.session_state:
    st.session_state.siki = ""

if 'right' not in st.session_state:
    st.session_state.right = 0

if 'used_numbers' not in st.session_state:
    st.session_state.used_numbers = set()  # 使用した数字を記録

# 四則演算ボタン (個別に配置)
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

st.write("")  # 余白を追加

# 数字ボタン (個別に配置) ※ボタン名が重複しないようにする
col7, col8, col9, col10 = st.columns(4)
num_cols = [col7, col8, col9, col10]

for i, num in enumerate(st.session_state.numbers):
    if num not in st.session_state.used_numbers:  # 未使用の数字のみボタンを押せる
        if num_cols[i].button(str(num) + " " + str(i)):  # ラベルに空白 + インデックス追加
            st.session_state.siki += str(num)
            st.session_state.used_numbers.add(num)  # 使った数字を記録

# 削除ボタン
if st.button("削除"):
    if st.session_state.siki:
        last_char = st.session_state.siki[-1]
        st.session_state.siki = st.session_state.siki[:-1]
        
        # 削除したのが数字なら、使用済みリストから削除
        if last_char.isdigit():
            st.session_state.used_numbers.discard(int(last_char))

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
    st.session_state.numbers = random.choices(range(1, 10), k=4)  # 重複ありの数字生成
    st.session_state.siki = ""
    st.session_state.used_numbers = set()  # 使用済みリストをリセット

# スコア表示
st.subheader(f"スコア: {st.session_state.right}")
