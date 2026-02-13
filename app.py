import streamlit as st

st.title("英語クイズ")

score = 0

st.write("Q1. 梨 は英語で？")
q1 = st.text_input("答えを書いてください")

if q1.lower() == "pear":
    st.write("⭕ 正解！")
    score += 1
elif q1 != "":
    st.write("❌ 不正解")

st.write("Q2. キリン は英語で？")
q2 = st.text_input("答えを書いてください ", key="q2")

if q2.lower() == "giraffe":
    st.write("⭕ 正解！")
    score += 1
elif q2 != "":
    st.write("❌ 不正解")

st.write("Q3. 羊 は英語で？")
q3 = st.text_input("答えを書いてください  ", key="q3")

if q3.lower() == "sheep":
    st.write("⭕ 正解！")
    score += 1
elif q3 != "":
    st.write("❌ 不正解")

if st.button("結果を見る"):
    st.write("あなたの点数は", score, "点です！")
