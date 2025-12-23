import streamlit as st
import os

# 這裡放入 ChatGPT 幫你寫的那兩個生成函式 (generate_style_a, generate_style_b)
# 或是你直接把 ChatGPT 給你的整段 code 整理進來

st.title("Q3: AI 自動生成 PPT 換版型")

topic = st.text_input("請輸入 PPT 主題", "珍珠奶茶")

col1, col2 = st.columns(2)

with col1:
    if st.button("生成：科技深色風"):
        # 呼叫你的函式產生 PPT
        # generate_ppt_style_a(topic) 
        st.success(f"已生成 {topic} - 深色版！")
        # 讀取檔案讓使用者下載
        with open("style_a.pptx", "rb") as file:
            st.download_button("下載 PPT (Style A)", file, "style_a.pptx")

with col2:
    if st.button("生成：文青簡約風"):
        # generate_ppt_style_b(topic)
        st.success(f"已生成 {topic} - 簡約版！")
        with open("style_b.pptx", "rb") as file:
            st.download_button("下載 PPT (Style B)", file, "style_b.pptx")