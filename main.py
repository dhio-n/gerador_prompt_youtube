import streamlit as st
from youtube_api import get_video_info
from prompt_generator import generate_prompt

st.title("Gerador Inteligente de Prompt para YouTube")

api_key = st.text_input("🔑 Sua API Key do YouTube", type="password")
video_url = st.text_input("📺 Cole a URL do vídeo aqui")

publico_alvo = st.text_input("🎯 Público-alvo (ex: jovens gamers)")
objetivo = st.text_area("🧠 Objetivo do conteúdo (ex: viralizar, ensinar algo...)")

if st.button("Gerar Prompt"):
    if not all([api_key, video_url, publico_alvo, objetivo]):
        st.warning("Por favor, preencha todos os campos.")
    else:
        video_info = get_video_info(api_key, video_url)
        prompt = generate_prompt(video_info, publico_alvo, objetivo)
        st.text_area("📝 Prompt Gerado:", prompt, height=300)
