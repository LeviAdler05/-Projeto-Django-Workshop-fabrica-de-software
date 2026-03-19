from django.test import TestCase
import requests

cep = '68627534'

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

dados = resposta.json()

print(dados)
