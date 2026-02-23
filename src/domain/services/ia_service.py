from together import Together


CLIENT_TOGETHER_KEY = "02169dc259fdc4414d3d22a2a6b469e88578624b7bfd69cb60e6be2879ca452a"
client_together = Together(api_key=CLIENT_TOGETHER_KEY)

class IAService():
    def __init__(self, error_message: str, error_traceback: str = None):
        self.client = client_together
        
    def ia_error_handler():
        prompt = (
            "Simplifique o erro abaixo"/
            "Erro: {error_message}"/
            "Traceback: {error_traceback}"
        )
        try:
            response = client_together.chat.completions.create(
                model="meta-llama/Llama-3-8b-chat-hf",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.9
            )
            error_simple = response.choices[0].message.content.strip()
            return error_simple
        except:
            
            return "Retornando uma resposta padrão, pois ocorreu um erro na IA."
