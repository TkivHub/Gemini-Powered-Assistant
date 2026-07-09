import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-flash-latest"

SYSTEM_PROMPT = (
    "Eres un asistente virtual general, amigable y util. "
    "Respondes de forma clara y concisa a cualquier tipo de pregunta."
)

MENSAJE_API_KEY_FALTANTE = (
    "Error: no se encontro GEMINI_API_KEY. "
    "Agrega tu API key gratuita en el archivo .env "
    "(consiguela en https://aistudio.google.com/app/apikey)."
)

MENSAJE_API_KEY_INVALIDA = (
    "Error: la API key no es valida. "
    "Verifica que la copiaste completa y correctamente en el archivo .env "
    "(consiguela en https://aistudio.google.com/app/apikey)."
)


def generar_respuesta(historial_mensajes: list) -> str:
    """
    historial_mensajes: lista de dicts {'role': 'user'|'assistant', 'content': str}
    Convierte el historial al formato que espera Gemini y genera respuesta.
    """
    if not GEMINI_API_KEY:
        return MENSAJE_API_KEY_FALTANTE

    try:
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=SYSTEM_PROMPT,
        )

        historial_gemini = []
        for msg in historial_mensajes[:-1]:
            rol = "model" if msg["role"] == "assistant" else "user"
            historial_gemini.append({"role": rol, "parts": [msg["content"]]})

        chat = model.start_chat(history=historial_gemini)
        ultimo_mensaje = historial_mensajes[-1]["content"]
        respuesta = chat.send_message(ultimo_mensaje)
        return respuesta.text

    except Exception as e:
        error_texto = str(e)
        if "API_KEY_INVALID" in error_texto or "API key not valid" in error_texto:
            return MENSAJE_API_KEY_INVALIDA
        return f"Ocurrio un error al generar la respuesta: {error_texto}"