import streamlit as st
import google.generativeai as genai

# --- API キーの設定 ---
API_KEY = "AIzaSyD3sy0YJ_eyu4DO-iDGMd50wR_nYSoKL7s"  # ← ここに取得した API キーを入力
genai.configure(api_key=API_KEY)


# 利用可能なモデル一覧を取得
# models = genai.list_models()
# モデル名を表示
#for model in models:
#    st.write(model.name)

# --- Streamlit UI ---
st.title("🤖 BIPROGY チャットボット")

st.write("")
st.write("Google Gemini API(2.5 pro) を使用したチャットボット")

# ユーザーの入力
user_input = st.text_area("質問を入力してください:", "")

if st.button("送信"):
    if user_input:
        try:
            # ✅ 最新のモデル名を指定
            model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
            
            # ✅ generate_content() の修正
            response = model.generate_content([user_input])

            # ✅ レスポンスの取得方法を修正
            st.subheader("📝 AI の応答:")
            st.write(response.text if hasattr(response, 'text') else "応答が取得できませんでした。")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("質問を入力してください！")
