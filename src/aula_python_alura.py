import requests
import random

url = "https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json"

resposta = requests.get(url)

data = resposta.json()

valorSecreto = random.choice(data)
palavraSecreta = valorSecreto['palavra']
dica = valorSecreto['dica']

print("Bem-vindo ao jogo da forca!")
print("A palavra secreta tem", len(palavraSecreta), "letras.")
print("Dica:", dica)

acertou = False
enforcou = False
erros = 0
letrasErradas = []

while not acertou and not enforcou:
    chute = input("Digite uma letra: ")
    if chute in palavraSecreta:
        print("Você acertou uma letra!")
    else:
        print("Você errou uma letra!")
        erros += 1
        letrasErradas.append(chute)
    enforcou = erros == 6
    acertou = set(palavraSecreta) == set(letrasErradas)

if acertou:
    print("Você acertou a palavra secreta!")
else:
    print("Você errou a palavra secreta!")
    print("A palavra secreta era:", palavraSecreta)
    print("Fim do jogo")

