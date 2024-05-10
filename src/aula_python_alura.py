import requests
import random

url = "https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json"

resposta = requests.get(url)

data = resposta.json()

valorSecreto = random.choice(data)
palavraSecreta = valorSecreto['palavra']
dica = valorSecreto['dica']

print("Bem-vindo ao jogo da forca!")
print(f"A palavra secreta tem {len(palavraSecreta)} letras.")
print("Dica:", dica)

acertou = False
enforcou = False
erros = 0
tentativas = []

while not acertou and not enforcou:
    chute = input("Digite seu chute: ")
    if chute == palavraSecreta:
        print("Você acertou seu chute!")
    else:
        print("Você errou seu chute!")
        tentativas.append(chute)
    enforcou = len(tentativas) == 3
    # acertou = set(palavraSecreta) == set(tentativas)
    acertou = palavraSecreta==chute

if acertou:
    print("Você acertou a palavra secreta!")
else:
    print("Você errou a palavra secreta!")
    print("A palavra secreta era:", palavraSecreta)
    print("Fim do jogo")

