import google.generativeai as genai
import json
import base64
import pathlib
import pprint
import requests
import mimetypes
# from IPython.display import Markdown

# pega a API_KEY do .env
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

historico = []

with open('./src/historico.json', 'r') as f:
    historico = json.load(f)

convo = model.start_chat(history=historico)

def addHistorico(tipo, texto):
    with open('./src/historico.json', 'r') as f:
        historico = json.load(f)
    historico.append({"role": tipo, "parts": [texto]})
    with open('./src/historico.json', 'w') as f:
        json.dump(historico, f)

while True:
    mensagem = input("Digite a mensagem: ")

    if mensagem == 'sair':
        break

    addHistorico('user', mensagem)

    convo.send_message(mensagem)

    print('-------------------------')
    print(convo.last.text)
    print('-------------------------')

    addHistorico('model', convo.last.text)