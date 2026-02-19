import streamlit as st

st.set_page_config(page_title="英語クイズ", page_icon="📘")

st.markdown("<h1 style='text-align: center;'>📘　英語クイズ</h1>", unsafe_allow_html= True)       
st.write("5問の英語クイズに答えてください　✏")
score = 0

#--- Q1 ---
st.subheader("Q1. 梨 は英語で？")
q1 = st.text_input("ここに入力してください", key="q1")

# --- Q2 ---
st.subheader("Q2. キリン は英語で？")
q2 = st.text_input("ここに入力してください", key="q2")

# ---Q3 ---
st.subheader("Q3. 羊は 英語で？")
q3 = st.text_input("ここに入力してください", key="q3")

# ---Q4 ---
st.subheader("Q4. 虎は 英語で？")
q4 = st.text_input("ここに入力してください", key="q4")
 
# ---Q5 ---
st.subheader("Q5. りんごは 英語で？")
q5 = st.text_input("ここに入力してください", key="q5")

if st.button("結果をみる"):

  # Q1
  if q1.strip().lower() == "pear":
     score += 1
     st.success("Q1 ⭕ 正解！")
  else :
     st.error("Q1 ❌ 不正解(正解はpear)")

  # Q2
  if q2.strip().lower() == "giraffe":
      score += 1
      st.success ("Q2⭕ 正解！")
  else:
      st.error("Q2 ❌不正解（正解はgiraffe)")

  # Q3 
  if q3.strip().lower() == "sheep":
        score += 1
        st.success(" Q3 ⭕正解！")
  else: 
        st.error("Q3 ❌不正解（正解はsheep)")

  # Q4
  if q4.strip().lower() ==  "tiger":
        score += 1  
        st.success("Q4 ⭕正解！")
  else:
       st.error("Q4 ❌不正解（正解はtiger)")

  # Q5
  if q5.strip().lower() == "apple":
        score += 1
        st.success("Q5 ⭕正解！")
  else:
        st.error("Q5 ❌不正解（正解はapple)")

 st.markdown("---")
 st.markdown(f"## 🎉 あなたの点数は {score} / 5 点です！")





 

    


  
