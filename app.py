import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Travel AI Assistant", page_icon="✈️", layout="centered")

# GANTI DENGAN API KEY ANDA!
API_KEY = "MASUKKAN_API_KEY_ANDA"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
  model_name="gemini-3.6-flash",
  system_instruction="Kamu adalah Travel AI Assistant. Jawablah dengan gaya bahasa santai."
)

st.title("✈️ Travel AI Assistant")
st.caption("Tanya apa saja soal traveling, aku siap bantu 🗺️")

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown("Halo! Mau liburan ke mana nih?")
        st.session_state.messages.append({"role": "assistant", "content": "Halo! Mau liburan ke mana nih?"})

for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🧑"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input("Mau nanya apa?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
