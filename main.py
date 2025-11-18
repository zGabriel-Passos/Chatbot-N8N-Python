import requests
import json
import time

WEBHOOK_URL = "YOUR_API_N8N"
MESSAGE_KEY = "message"


def enviar_mensagem(mensagem_usuario):
    """Envia a mensagem para o n8n e imprime a resposta BRUTA recebida."""

    payload = {
        "user_id": "python_user_123",
        MESSAGE_KEY: mensagem_usuario,
    }

    headers = {"Content-Type": "application/json"}

    start_time = time.time()

    try:
        response = requests.post(
            WEBHOOK_URL,
            data=json.dumps(payload),
            headers=headers,
            timeout=60,
        )

        response.raise_for_status()

        raw_response_text = response.text

        if raw_response_text:
            print(f"IA: {raw_response_text}")

    except requests.exceptions.HTTPError as http_err:
        print(
            f"<- Chatbot: [ERRO HTTP {http_err.response.status_code}] Falha no n8n. Verifique o log e as credenciais da IA."
        )
    except requests.exceptions.RequestException as e:
        print(
            f"<- Chatbot: [ERRO DE CONEXÃO] Verifique a URL e a conexão de internet. Detalhe: {e}"
        )


if __name__ == "__main__":
    if WEBHOOK_URL == "SUA_URL_DO_WEBHOOK_DO_N8N":
        print(
            "ERRO: Por favor, substitua a variável WEBHOOK_URL pela URL real do seu fluxo n8n ATIVO."
        )
    else:
        print("--- Chatbot Simples (n8n + Python) ---")
        print("Digite 'sair' para encerrar a conversa.")

        while True:
            user_input = input("Você: ")

            if user_input.lower() in ["sair", "exit", "quit"]:
                print("Encerrando a sessão.")
                break

            if user_input.strip():
                enviar_mensagem(user_input)

