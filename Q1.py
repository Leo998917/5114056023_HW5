import streamlit as st
from transformers import pipeline

# 設定頁面
st.title("🤖 AI vs Human Text Detector")
st.write("請輸入一段英文文本，AI 將判斷其為機器生成或人類撰寫的機率。")

# 載入模型 (使用快取避免重複載入)
@st.cache_resource
def load_pipeline():
    # 這裡使用一個常見的偵測模型，也可以換成其他公開模型
    return pipeline("text-classification", model="roberta-base-openai-detector")

pipe = load_pipeline()

# 使用者輸入
text_input = st.text_area("在此輸入文字...", height=200)

if st.button("開始偵測"):
    if text_input:
        with st.spinner("分析中..."):
            result = pipe(text_input)
            # result 格式通常為 [{'label': 'Real/Fake', 'score': 0.99}]
            label = result[0]['label']
            score = result[0]['score']
            
            # 顯示結果
            st.subheader("分析結果：")
            if label == 'Real':
                st.success(f"👨‍💻 人類撰寫 (Human) - 信心度: {score:.2%}")
            else:
                st.error(f"🤖 AI 生成 (Fake) - 信心度: {score:.2%}")
    else:
        st.warning("請先輸入文字！")