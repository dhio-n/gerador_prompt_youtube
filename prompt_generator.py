import openai

# Função para gerar o prompt
def generate_prompt(video_info, publico_alvo, objetivo):
    titulo = video_info.get("title", "")
    descricao = video_info.get("description", "")

    prompt = f"""
    Você é um criador de conteúdo especializado em vídeos virais para YouTube Shorts e TikTok, com foco em tecnologia, mercado dev e cultura jovem.

    Informações do vídeo original:
    - Título: {titulo}
    - Descrição: {descricao}

    Público-alvo: {publico_alvo}
    Objetivo do vídeo: {objetivo}

    Com base nessas informações, faça o seguinte:

    1. Liste as regras que você usará para otimizar o conteúdo para engajamento, usando uma linguagem jovem, memes, ganchos, emojis e CTAs eficazes.
    2. Gere um **novo título sugerido** (máx. 60 caracteres).
    3. Gere uma **nova descrição sugerida** (com tom provocativo e divertido, incluindo CTA e emojis).
    4. Crie um **roteiro curto (até 1 minuto)** para um vídeo estilo Shorts, com a seguinte estrutura:
       - Gancho provocativo
       - Desenvolvimento com storytelling rápido
       - Revelação ou punchline
       - Encerramento com chamada para ação

    Formato de resposta:
    Regras:
    - Regra 1
    - Regra 2
    (...)

    Título sugerido:
    [Título aqui]

    Descrição sugerida:
    [Descrição aqui]

    Roteiro sugerido:
    [Roteiro com emoji, tom leve e divertido]
    """
    return prompt.strip()

# Função para obter resposta da IA
def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um especialista em marketing, roteiro e engajamento para vídeos curtos e virais."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.8
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Erro ao chamar a OpenAI: {e}")
        return None
