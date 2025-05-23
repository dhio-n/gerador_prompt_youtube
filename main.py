import streamlit as st
from googleapiclient.discovery import build
from openai import OpenAI
from youtube_api import get_video_info
from prompt_generator import generate_prompt

# Configurações iniciais
st.set_page_config(page_title="YouTube AI Generator", layout="wide")
st.title("🎥 YouTube IA Generator")
st.write("Este app usa a API do YouTube + OpenAI para gerar títulos e descrições otimizadas com base em um vídeo.")

# Pega a chave da API do YouTube e da OpenAI via st.secrets
YOUTUBE_API_KEY = st.secrets["youtube"]["api_key"]
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# Função para buscar dados do vídeo no YouTube
def get_video_info(youtube_url):
    video_id = youtube_url.split("v=")[-1]
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    if not response["items"]:
        return None
    item = response["items"][0]["snippet"]
    return {
        "title": item["title"],
        "description": item["description"],
        "tags": item.get("tags", [])
    }

# Interface do usuário
with st.form("youtube_form"):
    youtube_url = st.text_input("URL do vídeo do YouTube")
    publico_alvo = st.text_input("Público-alvo")
    objetivo = st.text_input("Objetivo do vídeo (atrair inscritos, vender algo, etc.)")
    submitted = st.form_submit_button("Gerar com IA")

if submitted:
    video_info = get_video_info(youtube_url)
    if not video_info:
        st.error("Não foi possível obter informações do vídeo. Verifique a URL.")
    else:
        prompt = generate_prompt(video_info, publico_alvo, objetivo)

        # Chamada à OpenAI para gerar a resposta com o novo método
        with st.spinner("Gerando com inteligência artificial..."):
            try:
                # Usando o cliente da OpenAI para criar a resposta
                response = client.responses.create(
                    model="gpt-4.1",  # Modelo GPT-4 ou outro de sua escolha
                    input=prompt
                )
                resultado = response.output_text.strip()
                st.text_area("📝 Resultado Gerado pela IA:", resultado, height=300)
            except Exception as e:
                st.error(f"Erro ao chamar a OpenAI: {e}")
