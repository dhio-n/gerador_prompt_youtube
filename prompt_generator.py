import openai

def generate_prompt(video_info, publico_alvo, objetivo):
    titulo = video_info.get("titulo", "")
    descricao = video_info.get("descricao", "")

    prompt = f"""
    Você é um especialista em criação de conteúdo viral no YouTube.

    Título do vídeo: {titulo}
    Descrição do vídeo: {descricao}
    Público-alvo: {publico_alvo}
    Objetivo: {objetivo}

    Com base nessas informações, crie um prompt para que um modelo de IA gere um título e descrição otimizados, criativos, cativantes e que maximizem o engajamento no YouTube. O prompt deve ser claro e direto para a IA.

    Formato desejado:
    Título sugerido:
    Descrição sugerida:
    """
    return prompt.strip()

# Chamada para a OpenAI com a nova API
def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Ou outro modelo que você esteja utilizando
            messages=[
                {"role": "system", "content": "Você é um especialista em marketing e YouTube."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        resultado = response['choices'][0]['message']['content'].strip()
        return resultado
    except Exception as e:
        print(f"Erro ao chamar a OpenAI: {e}")
        return None
