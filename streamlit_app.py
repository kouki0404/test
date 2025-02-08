import streamlit as st
import random

st.title("10ゲーム")

# 数字の初期化（重複しないようにする）
if 'numbers' not in st.session_state:
    st.session_state.numbers = random.sample(range(1, 10), 4)

if 'siki' not in st.session_state:
    st.session_state.siki = ""

if 'right' not in st.session_state:
    st.session_state.right = 0

if 'used_numbers' not in st.session_state:
    st.session_state.used_numbers = set()  # すでに使用した数字を記録

# 四則演算子
operators = ["＋", "－", "×", "÷", "(", ")"]
real_ops = { "＋": "+", "－": "-", "×": "*", "÷": "/" }

# ボタン配置
op_cols = st.columns(len(operators))  # 四則演算ボタンを1行で配置
for i, op in enumerate(operators):
    if op_cols[i].button(op):
        st.session_state.siki += real_ops[op]

st.write("")  # 余白を追加してレイアウトを整理

num_cols = st.columns(4)  # 数字ボタンを1行で配置
for i, num in enumerate(st.session_state.numbers):
    if num not in st.session_state.used_numbers:  # 未使用の数字のみボタンを押せる
        if num_cols[i].button(str(num)):
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
    st.session_state.numbers = random.sample(range(1, 10), 4)
    st.session_state.siki = ""
    st.session_state.used_numbers = set()  # 使用済みリストをリセット

# スコア表示
st.subheader(f"スコア: {st.session_state.right}")
