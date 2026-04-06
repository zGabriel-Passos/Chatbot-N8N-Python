 # 🤖 Chatbot Python + n8n

  Chatbot simples em Python que conecta um terminal a um workflow de IA n8n via webhook.

  ## ⚡ Fluxo

  Você (Terminal)  →  POST /webhook  →  n8n (Workflow + IA)  →  Resposta

  ## 🚀 Como Usar

  1. **Configure o webhook n8n** (veja abaixo)
  2. **Cole a URL do webhook** no lugar de `YOUR_API_N8N` no código
  3. **Execute:**

  ```bash
  pip install requests
  python main.py

  🔧 Montando o Workflow no n8n

  1. No n8n, crie um novo workflow e adicione um nó Webhook
  2. Configure o Webhook:
    - Method: POST
    - Path: qualquer nome (ex: chat)
    - Authentication: None (ou configure a seu critério)
    - Response Mode: `Last Node**`
  3. Adicione um nó de IA (qualquer LLM de sua escolha)
  4. Conecte o Webhook ao nó de IA
  5. Adicione um nó Respond to Webhook no final para enviar a resposta
  6. Ative o workflow e copie a URL de produção
  7. Cole a URL no lugar de YOUR_API_N8N no código

```

## 📝 Exemplo de Resposta
```bash

  --- Chatbot Simples (n8n + Python) ---
  Digite 'sair' para encerrar a conversa.

  Você: Olá, como vai?
  IA: Olá! Tudo bem, obrigado por perguntar! E você?

```
## 🔧 Configuração

```bash
  ┌─────────────┬──────────────────────────────┬───────────┐
  │  Variável   │          Descrição           │  Padrão   │
  ├─────────────┼──────────────────────────────┼───────────┤
  │ WEBHOOK_URL │ URL do webhook n8n           │ ""        │
  ├─────────────┼──────────────────────────────┼───────────┤
  │ MESSAGE_KEY │ Chave da mensagem no payload │ "message" │
  └─────────────┴──────────────────────────────┴───────────┘
```
