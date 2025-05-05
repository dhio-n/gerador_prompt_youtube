import requests
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    query = urlparse(url).query
    return parse_qs(query).get("v", [None])[0]

def get_video_info(api_key, video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return {"titulo": "", "descricao": ""}

    endpoint = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet",
        "id": video_id,
        "key": api_key
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["items"]:
            snippet = data["items"][0]["snippet"]
            return {
                "titulo": snippet.get("title", ""),
                "descricao": snippet.get("description", "")
            }
    return {"titulo": "", "descricao": ""}
