import requests
from urllib.parse import urlparse, parse_qs

# Função para extrair o ID do vídeo da URL
def extract_video_id(url):
    query = urlparse(url).query
    return parse_qs(query).get("v", [None])[0]

# Função para obter informações do vídeo no YouTube com a API
def get_video_info(api_key, video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return {"title": "", "description": ""}

    # Endpoint da API do YouTube
    endpoint = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet",  # Solicitando a parte "snippet" para título, descrição, etc.
        "id": video_id,
        "key": api_key
    }

    # Fazendo a requisição à API
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["items"]:
            snippet = data["items"][0]["snippet"]
            return {
                "title": snippet.get("title", ""),
                "description": snippet.get("description", "")
            }
    return {"title": "", "description": ""}
