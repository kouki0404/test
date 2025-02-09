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
tabs = st.tabs(["使い方","メイン画面"])
with tabs[0]:
    st.subheader("このアプリについて")
    st.write("  このアプリでは4つの数字と四則演算を使って10を作るパズルゲームです")
    st.write("  パソコン、タブレット等の端末で使用することをおすすめします")
    st.write("数字ボタンについている[0]などはボタンを識別するためなので気にしないでください")
    st.write("")
    st.subheader("やり方")
    st.write("例")
    st.write("1,2,3,4の数字を与えらたら")
    st.write("1+2+3+4=10となります")
    st.write("")
    st.write("回答が10になった場合のみスコアが増えます")

with tabs[1]:
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
        button_label = f"{num} ({i})"  # ボタンの識別のためにインデックスを追加
        if i not in st.session_state.used_numbers:  # 押されたボタンのみを管理
            if num_cols[i].button(button_label):
                st.session_state.siki += str(num)
                st.session_state.used_numbers.append(i)  # 押したボタンのインデックスを記録

    # 削除ボタン
    if st.button("削除"):
        if st.session_state.siki:
            last_char = st.session_state.siki[-1]
            st.session_state.siki = st.session_state.siki[:-1]

            # 削除したのが数字なら、最後に押されたボタンを復活
            if last_char.isdigit():
                if st.session_state.used_numbers:
                    st.session_state.used_numbers.pop()

    # 計算結果を表示
    try:
        result = eval(st.session_state.siki) if st.session_state.siki else "?"
    except:
        result = "エラー"

    st.write(f"{st.session_state.siki} = {result}")

    # 次の問題へ（すべての数字ボタンが押され、計算結果が10のときのみスコア加算）
    if st.button("次の問題へ"):
        if result == 10 and len(st.session_state.used_numbers) == 4:  # 全ての数字ボタンが押されたか確認
            st.session_state.right += 1  # 正解ならスコア加算

        # 次の問題の準備
        st.session_state.numbers = random.choices(range(1, 10), k=4)  # 1~9 のみ
        st.session_state.siki = ""
        st.session_state.used_numbers = []  # 使用済みリストをリセット
    st.write("注意:次の問題を遊びたいときは上のボタンを押した後任意のボタンを押してください")
    st.subheader(f"スコア: {st.session_state.right}")
