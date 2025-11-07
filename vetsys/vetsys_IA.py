import os
from dotenv import load_dotenv
import google.generativeai as genai

#Carregar variáveis de ambiente e configurar API
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY_IA"))

#treino
instrucoes_sistema = (
    "Você é um chatbot veterinário chamado VetSys. Extremamente qualificado, científico e profissional; mas com um linguajar e idioma local, para geração de empatia na experiência dos principais usuários (donos de PETs)"
    "Seu papel é ajudar usuários com dúvidas sobre a saúde e o comportamento de seus animais. "
    "Responda perguntas simples como 'meu cachorro não quer comer' ou 'meu gato está dormindo muito', "
    "de forma clara, empática e educativa. "
    "Evite dar diagnósticos exatos e sempre recomende que o tutor procure um veterinário quando necessário. "
    "Você faz parte de um futuro aplicativo que permitirá ver clínicas e marcar consultas, "
    "mas no momento apenas responde dúvidas básicas."
     "P.S.: Seja extremamente profissioal. Em suas respostas, baseie-se em dados reais e consistentes. NÃO alucine dados e nem informações; tudo deve ser consistente, validado e profissional. Deixe claro, em suas respostas, de onde vieram as fontes que a formularam. De forma consistente, real e validada."
     "faça respostas bem resumidas, no máximo 5 linhas e básicas, diga oque pode ser de forma bem curta, indique e indique ir ao veterinário"
)

#Inicializar o modelo Gemini com as instruções
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=instrucoes_sistema
)
chat = model.start_chat(history=[])

#Função para obter resposta do modelo
def obter_resposta(pergunta):
    try:
        resposta = chat.send_message(pergunta, stream=True)
        texto_final = ""
        print("🤖 VetSys: ", end="", flush=True)
        for chunk in resposta:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                texto_final += chunk.text
        print()
        return texto_final
    except Exception as e:
        print("\n⚠️ Erro durante o streaming:", e)
        return "Desculpe, ocorreu um problema na conexão."

#Loop principal no terminal
print("🐾 VetSys - Chatbot Veterinário iniciado! Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("👤 Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chatbot...")
        break
    obter_resposta(pergunta)
