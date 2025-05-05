import openai

# Função para gerar o prompt de roteiro
def generate_prompt(video_info, publico_alvo, objetivo):
    titulo = video_info.get("title", "")
    transcricao = video_info.get("description", "")  # Considerando que aqui vem a transcrição

    prompt = f"""
    Você é um criador de conteúdo experiente no YouTube.

    Abaixo estão as informações de um vídeo já existente:
    Título do vídeo: {titulo}
    Transcrição do vídeo: {transcricao}
    Público-alvo: {publico_alvo}
    Objetivo: {objetivo}

    Com base nessas informações, crie um novo **roteiro de vídeo original** com cerca de 1 minuto de duração, pronto para ser usado em um novo vídeo de YouTube Shorts ou TikTok.

    Regras:
    - Use uma linguagem informal e engajante, voltada para jovens de 17 a 35 anos interessados em tecnologia, programação e cultura dev.
    - O roteiro deve ter uma introdução chamativa (gancho), desenvolvimento objetivo e um fechamento com CTA (ex: "curte e se inscreve").
    - Pode usar emojis, expressões populares e estilo de fala descontraído.

    Formato da resposta:
    [Introdução chamativa]
    [Desenvolvimento com storytelling curto]
    [Conclusão + Chamada para ação]
    """

    return prompt.strip()

# Função para obter resposta da IA
def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um roteirista especialista em vídeos curtos e virais para o YouTube e TikTok."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Erro ao chamar a OpenAI: {e}")
        return None
