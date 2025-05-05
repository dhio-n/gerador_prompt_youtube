import openai

# Função para gerar o prompt com base nas informações do vídeo e objetivos
def generate_prompt(video_info, publico_alvo, objetivo):
    titulo = video_info.get("title", "")
    descricao = video_info.get("description", "")

    prompt = f"""
Você é um especialista em criação de conteúdo viral no YouTube.

Título do vídeo: {titulo}
Descrição do vídeo: {descricao}
Público-alvo: {publico_alvo}
Objetivo: {objetivo}

Com base nessas informações, crie um título e descrição otimizados, criativos, cativantes e que maximizem o engajamento no YouTube. O prompt deve ser claro e direto para a IA.

Formato desejado:
Título sugerido:
Descrição sugerida:
"""

    return prompt.strip()

# Função para chamar a OpenAI e gerar o título e descrição otimizados
def generate_optimized_content(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        resultado = response.choices[0].text.strip()
        return resultado
    except Exception as e:
        return f"Erro ao chamar a OpenAI: {e}"
